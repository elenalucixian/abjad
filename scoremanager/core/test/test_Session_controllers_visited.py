# -*- encoding: utf-8 -*-
import pytest
from abjad import *
import scoremanager


def test_Session_controllers_visited_01():
    r'''Score manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='q', is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_02():
    r'''Score package manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='red~example~score q', is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_03():
    r'''Build directory manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='red~example~score u q', is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.managers.BuildDirectoryManager(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_04():
    r'''Material package manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    score_manager._run(pending_user_input='red~example~score m q', is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.wranglers.MaterialPackageWrangler(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_05():
    r'''Material package manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    string = 'red~example~score m tempo~inventory q'
    score_manager._run(pending_user_input=string, is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.wranglers.MaterialPackageWrangler(),
        scoremanager.managers.TempoInventoryMaterialManager(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_06():
    r'''Segment wrangler.
    '''

    score_manager = scoremanager.core.ScoreManager()
    string = 'red~example~score g q'
    score_manager._run(pending_user_input=string, is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.wranglers.SegmentPackageWrangler(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_07():
    r'''Segment package manager.
    '''

    score_manager = scoremanager.core.ScoreManager()
    string = 'red~example~score g 1 q'
    score_manager._run(pending_user_input=string, is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.wranglers.SegmentPackageWrangler(),
        scoremanager.managers.SegmentPackageManager(),
        ]
    assert score_manager._session.controllers_visited == controllers


def test_Session_controllers_visited_08():
    r'''Stylesheet file wrangler.
    '''

    score_manager = scoremanager.core.ScoreManager()
    string = 'red~example~score y q'
    score_manager._run(pending_user_input=string, is_test=True)

    controllers = [
        scoremanager.core.ScoreManager(),
        scoremanager.managers.ScorePackageManager(),
        scoremanager.wranglers.StylesheetWrangler(),
        ]
    assert score_manager._session.controllers_visited == controllers
