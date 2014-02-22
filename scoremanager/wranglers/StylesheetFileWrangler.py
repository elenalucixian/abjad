# -*- encoding: utf-8 -*-
import os
from abjad.tools import sequencetools
from abjad.tools import stringtools
from scoremanager.wranglers.Wrangler import Wrangler


class StylesheetFileWrangler(Wrangler):
    r'''Stylesheet file wrangler.

    ..  container:: example

        ::

            >>> wrangler = scoremanager.wranglers.StylesheetFileWrangler()
            >>> wrangler
            StylesheetFileWrangler()

    '''

    ### INITIALIZER ###

    def __init__(self, session=None):
        from scoremanager import managers
        superclass = super(StylesheetFileWrangler, self)
        superclass.__init__(session=session)
        self._asset_manager_class = managers.FileManager
        self.abjad_storehouse_directory_path = \
            self.configuration.abjad_stylesheets_directory_path
        self.user_storehouse_directory_path = \
            self.configuration.user_library_stylesheets_directory_path
        self.score_storehouse_path_infix_parts = ('stylesheets',)

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        if self._session.is_in_score:
            return 'stylesheets'
        else:
            return 'stylesheet library'

    @property
    def _temporary_asset_name(self):
        return '__temporary_stylesheet.ily'

    ### PRIVATE METHODS ###

    def _filesystem_path_to_annotation(self, filesystem_path):
        from scoremanager import managers
        annotation = None
        if filesystem_path.startswith(
            self.configuration.abjad_score_packages_directory_path) or \
            filesystem_path.startswith(
            self.configuration.user_score_packages_directory_path):
            tmp = os.path.join('stylesheets')
            score_filesystem_path = filesystem_path.rpartition(tmp)[0]
            package_path = \
                self.configuration.filesystem_path_to_package_path(
                score_filesystem_path)
            score_package_manager = managers.ScorePackageManager(
                package_path=package_path)
            annotation = score_package_manager._get_title()
        elif filesystem_path.startswith(
            self.configuration.abjad_stylesheets_directory_path):
            annotation = 'Abjad'
        elif filesystem_path.startswith(
            self.configuration.user_library_stylesheets_directory_path):
            annotation = 'library'
        return annotation

    def _get_current_directory(self):
        if self._session.current_score_directory_path:
            parts = (self._session.current_score_directory_path,)
            parts += self.score_storehouse_path_infix_parts
            return os.path.join(*parts)
    
    def _get_header_stylesheet_file_path(self):
        for directory_entry in sorted(os.listdir(
            self._get_current_directory())):
            if directory_entry.endswith('header.ily'):
                file_path = os.path.join(
                    self._get_current_directory(),
                    directory_entry,
                    )
                return file_path
    
    def _get_layout_stylesheet_file_path(self):
        for directory_entry in sorted(os.listdir(
            self._get_current_directory())):
            if directory_entry.endswith('layout.ily'):
                file_path = os.path.join(
                    self._get_current_directory(),
                    directory_entry,
                    )
                return file_path
    
    def _get_paper_stylesheet_file_path(self):
        for directory_entry in sorted(os.listdir(
            self._get_current_directory())):
            if directory_entry.endswith('paper.ily'):
                file_path = os.path.join(
                    self._get_current_directory(),
                    directory_entry,
                    )
                return file_path
    
    def _handle_main_menu_result(self, result):
        if result in self._user_input_to_action:
            self._user_input_to_action[result](self)
        else:
            self.interactively_edit_asset(result)

    def _is_valid_directory_entry(self, directory_entry):
        superclass = super(StylesheetFileWrangler, self)
        if superclass._is_valid_directory_entry(directory_entry):
            if directory_entry.endswith('.ily'):
                return True
        return False

    def _make_asset_menu_entries(self, head=None, include_extension=False):
        filesystem_paths = self.list_asset_filesystem_paths(head=head)
        display_strings = []
        for filesystem_path in filesystem_paths:
            display_string = os.path.basename(filesystem_path)
            annotation = self._filesystem_path_to_annotation(filesystem_path)
            if annotation:
                display_string = '{} ({})'.format(display_string, annotation)
            display_strings.append(display_string)
        menu_entries = []
        if display_strings:
            sequences = (display_strings, [None], [None], filesystem_paths)
            menu_entries = sequencetools.zip_sequences(sequences, cyclic=True)
        return menu_entries

    def _make_main_menu(self, head=None):
        main_menu = self._session.io_manager.make_menu(where=self._where)
        self._main_menu = main_menu
        asset_section = main_menu.make_asset_section()
        main_menu._asset_section = asset_section
        menu_entries = self._make_asset_menu_entries(
            head=head,
            include_extension=True,
            )
        asset_section.menu_entries = menu_entries
        if self._session.current_score_directory_path:
            command_section = main_menu.make_command_section()
            if self._get_header_stylesheet_file_path():
                command_section.append(('header stylesheet - edit', 'h'))
            if self._get_layout_stylesheet_file_path():
                command_section.append(('layout stylesheet - edit', 'l'))
            if self._get_paper_stylesheet_file_path():
                command_section.append(('paper stylesheet - edit', 'p'))
        command_section = main_menu.make_command_section()
        command_section.append(('new', 'new'))
        command_section.append(('copy', 'cp'))
        command_section.append(('rename', 'ren'))
        command_section.append(('remove', 'rm'))
        return main_menu

    ### PUBLIC METHODS ###

    def interactively_edit_asset(
        self, 
        filesystem_path,
        pending_user_input=None,
        ):
        r'''Interactively edits asset.

        Returns none.
        '''
        self._session.io_manager._assign_user_input(pending_user_input)
        manager = self._asset_manager_class(
            filesystem_path=filesystem_path, 
            session=self._session,
            )
        manager.interactively_edit()

    def interactively_edit_header_stylesheet(
        self,
        pending_user_input=None,
        ):
        r'''Interactively edits header stylesheet.

        Returns none.
        '''
        file_path = self._get_header_stylesheet_file_path()
        self.interactively_edit_asset(file_path)

    def interactively_edit_layout_stylesheet(
        self,
        pending_user_input=None,
        ):
        r'''Interactively edits layout stylesheet.

        Returns none.
        '''
        file_path = self._get_layout_stylesheet_file_path()
        self.interactively_edit_asset(file_path)

    def interactively_edit_paper_stylesheet(
        self,
        pending_user_input=None,
        ):
        r'''Interactively edits paper stylesheet.

        Returns none.
        '''
        file_path = self._get_paper_stylesheet_file_path()
        self.interactively_edit_asset(file_path)

    def interactively_make_asset(
        self,
        pending_user_input=None,
        ):
        r'''Interactively makes asset.

        Returns none.
        '''
        from scoremanager import managers
        self._session.io_manager._assign_user_input(pending_user_input)
        with self.backtracking:
            storehouse_path = \
                self.interactively_select_storehouse_directory_path(
                abjad_library=False,
                user_library=True,
                abjad_score_packages=False,
                user_score_packages=False,
                )
        if self._session._backtrack():
            return
        getter = self._session.io_manager.make_getter(where=self._where)
        getter.append_string('stylesheet name')
        stylesheet_file_path = getter._run()
        if self._session._backtrack():
            return
        stylesheet_file_path = \
            stringtools.string_to_accent_free_snake_case(
            stylesheet_file_path)
        if not stylesheet_file_path.endswith('.ily'):
            stylesheet_file_path = stylesheet_file_path + '.ily'
        stylesheet_file_path = os.path.join(
            storehouse_path,
            stylesheet_file_path,
            )
        manager = managers.FileManager(
            stylesheet_file_path, 
            session=self._session,
            )
        if self._session.is_test:
            manager._make_empty_asset()
        else:
            manager.interactively_edit()

    def list_asset_filesystem_paths(
        self,
        abjad_library=True, 
        user_library=True,
        abjad_score_packages=True, 
        user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset filesystem paths.

        Lists abjad stylesheet filesystem paths:

        ::

            >>> for x in wrangler.list_asset_filesystem_paths(
            ...     user_library=False, 
            ...     user_score_packages=False,
            ...     ):
            ...     x
            '.../abjad/stylesheets/clean-letter-14.ily'
            '.../abjad/stylesheets/clean-letter-16.ily'
            '.../abjad/stylesheets/rhythm-letter-16.ily'
            '.../red_example_score/stylesheets/red-example-score-stylesheet.ily'

        Returns list.
        '''
        superclass = super(StylesheetFileWrangler, self)
        return superclass.list_asset_filesystem_paths(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            head=head,
            )

    def list_asset_managers(
        self, 
        abjad_library=True, 
        user_library=True,
        abjad_score_packages=True, 
        user_score_packages=True, 
        head=None,
        ):
        r'''Lists asset managers.

        Lists abjad stylesheet managers:

        ::

            >>> for x in wrangler.list_asset_managers(
            ...     user_library=False, 
            ...    user_score_packages=False):
            ...     x
            FileManager('.../abjad/stylesheets/clean-letter-14.ily')
            FileManager('.../abjad/stylesheets/clean-letter-16.ily')
            FileManager('.../abjad/stylesheets/rhythm-letter-16.ily')
            FileManager('.../scoremanager/scorepackages/red_example_score/stylesheets/red-example-score-stylesheet.ily')

        Returns list.
        '''
        superclass = super(StylesheetFileWrangler, self)
        return superclass.list_asset_managers(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            head=head,
            )

    def list_asset_names(
        self, 
        abjad_library=True, 
        user_library=True,
        abjad_score_packages=True, 
        user_score_packages=True, 
        head=None, 
        include_extension=False,
        ):
        r'''Lists asset names.

        Lists abjad stylesheet names:

        ::

            >>> for x in wrangler.list_asset_names(
            ...     user_library=False, 
            ...     user_score_packages=False, 
            ...     include_extension=True):
            ...     x
            'clean-letter-14.ily'
            'clean-letter-16.ily'
            'rhythm-letter-16.ily'
            'time-signature-context.ily'
            'red-example-score-stylesheet.ily'

        Returns list.
        '''
        superclass = super(StylesheetFileWrangler, self)
        return superclass.list_asset_names(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            head=head,
            include_extension=include_extension,
            )

    def list_storehouse_directory_paths(
        self,
        abjad_library=True, 
        user_library=True,
        abjad_score_packages=True, 
        user_score_packages=True,
        ):
        r'''Lists asset storehouse filesystem paths.

        Lists abjad storehouse filesystem paths:

        ::

            >>> for x in wrangler.list_storehouse_directory_paths(
            ...     user_library=False, 
            ...     user_score_packages=False,
            ...     ):
            ...     x
            '.../abjad/stylesheets'
            '.../blue_example_score/stylesheets'
            '.../green_example_score/stylesheets'
            '.../red_example_score/stylesheets'

        Returns list.
        '''
        superclass = super(StylesheetFileWrangler, self)
        return superclass.list_storehouse_directory_paths(
            abjad_library=abjad_library,
            user_library=user_library,
            abjad_score_packages=abjad_score_packages,
            user_score_packages=user_score_packages,
            )

    ### UI MANIFEST ###

    _user_input_to_action = Wrangler._user_input_to_action.copy()
    _user_input_to_action.update({
        'h': interactively_edit_header_stylesheet,
        'l': interactively_edit_layout_stylesheet,
        'p': interactively_edit_paper_stylesheet,
        'new': interactively_make_asset,
        })
