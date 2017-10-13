# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase

from ipywidgets import IntText


class TestIntText(TestCase):

    def test_construction_default_value(self):
        textbox = IntText()
        state = textbox.get_state()
        assert state['value'] == 0
        assert state['disabled'] is False
        assert state['continuous_update'] is False
        assert state['step'] == 1

    def test_construction_explicit_value(self):
        textbox = IntText(72)
        assert textbox.get_state()['value'] == 72

    def test_construction_value_kwarg(self):
        textbox = IntText(value=72)
        assert textbox.get_state()['value'] == 72

    def test_set_value(self):
        textbox = IntText()
        textbox.value = 72
        assert textbox.get_state()['value'] == 72
