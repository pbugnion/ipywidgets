# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase

from ipywidgets import IntText, BoundedIntText


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


class TestBoundedIntText(TestCase):

    def test_construction_default_value(self):
        textbox = BoundedIntText()
        state = textbox.get_state()
        assert state['value'] == 0
        assert state['disabled'] is False
        assert state['continuous_update'] is False
        assert state['min'] == 0
        assert state['max'] == 100
        assert state['step'] == 1

    def test_construction_explicit_arguments(self):
        textbox = BoundedIntText(52, -5, 81, 3)
        state = textbox.get_state()
        assert state['value'] == 52
        assert state['min'] == -5
        assert state['max'] == 81
        assert state['step'] == 3

    def test_construction_with_kwargs(self):
        textbox = BoundedIntText(
            value=52,
            min=-5,
            max=81,
            step=3
        )
        state = textbox.get_state()
        assert state['value'] == 52
        assert state['min'] == -5
        assert state['max'] == 81
        assert state['step'] == 3
