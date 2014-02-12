# -*- encoding: utf-8 -*-
from experimental.tools import handlertools
from experimental.tools.scoremanagertools import getters
from experimental.tools.scoremanagertools.editors.DynamicHandlerEditor \
    import DynamicHandlerEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest


class NoteAndChordHairpinHandlerEditor(DynamicHandlerEditor):

    ### PUBLIC PROPERTIES ###

    @property
    def target_manifest(self):
        return TargetManifest(
            handlertools.NoteAndChordHairpinHandler,
            ('hairpin_token', None, 'ht', getters.get_hairpin_token, True),
            ('minimum_duration', None, 'md', getters.get_duration, True),
            )
