from experimental.tools.scoremanagertools.menuing.MenuObject import MenuObject


class MenuSectionAggregator(MenuObject):

    ### INITIALIZER ###

    def __init__(self, session=None, where=None):
        MenuObject.__init__(self, session=session, where=where)
        self._sections = []

    ### READ-ONLY PROPERTIES ###

    @property
    def sections(self):
        return self._sections

    ### PUBLIC METHODS ###

    def handle_hidden_key(self, directive):
        if isinstance(directive, list) and len(directive) == 1:
            key = directive[0]
        else:
            key = directive
        if key in ('b', 'back'):
            self._session.is_backtracking_locally = True
        elif key == 'exec':
            self.exec_statement()
        elif key == 'grep':
            self.grep_directories()
        elif key == 'here':
            self.interactively_edit_client_source_file()
        elif key == 'hidden':
            self.show_hidden_menu_tokens()
        elif key == 'next':
            self._session.is_navigating_to_next_score = True
            self._session.is_backtracking_to_score_manager = True
        elif key == 'prev':
            self._session.is_navigating_to_prev_score = True
            self._session.is_backtracking_to_score_manager = True
        elif key in ('q', 'quit'):
            self._session.user_specified_quit = True
#        # TODO: make this redraw!
#        elif key == 'r':
#            pass
        elif isinstance(key, str) and 3 <= len(key) and 'score'.startswith(key):
            if self._session.is_in_score:
                self._session.is_backtracking_to_score = True
        elif isinstance(key, str) and 3 <= len(key) and 'home'.startswith(key):
            self._session.is_backtracking_to_score_manager = True
        elif key == 'tm':
            self.toggle_menu()
        elif key == 'tw':
            self._session.enable_where = not self._session.enable_where
        elif key == 'where':
            self.show_menu_client()
        else:
            return directive

    def show_hidden_menu_tokens(self):
        menu_lines = []
        for section in self.sections:
            if section.is_hidden:
                for token in section.tokens:
                    number, key, body, return_value = token.unpack(section.return_value_attribute)
                    menu_line = self.make_tab(1) + ' '
                    menu_line += '{} ({})'.format(body, key)
                    menu_lines.append(menu_line)
                menu_lines.append('')
        self._io.display(menu_lines, capitalize_first_character=False)
        self._session.hide_next_redraw = True
