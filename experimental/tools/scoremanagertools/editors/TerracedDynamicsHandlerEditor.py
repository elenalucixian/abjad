# -*- encoding: utf-8 -*-
from experimental.tools import handlertools
from experimental.tools.scoremanagertools import getters
from experimental.tools.scoremanagertools.editors.DynamicHandlerEditor \
    import DynamicHandlerEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest


class TerracedDynamicsHandlerEditor(DynamicHandlerEditor):

    ### PUBLIC PROPERTIES ###

    @property
    def target_manifest(self):
        return TargetManifest(
            handlertools.TerracedDynamicsHandler,
            ('dynamics', None, 'dy', getters.get_dynamics, True),
            ('minimum_duration', None, 'md', getters.get_duration, True),
            )
