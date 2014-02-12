# -*- encoding: utf-8 -*-
from abjad.tools import rhythmmakertools
from scoremanagertools import getters
from scoremanagertools.editors.RhythmMakerEditor \
    import RhythmMakerEditor


class RestRhythmMakerEditor(RhythmMakerEditor):

    ### PUBLIC PROPERTIES ###

    @property
    def target_manifest(self):
        return self.TargetManifest(
            rhythmmakertools.RestRhythmMaker,
            )