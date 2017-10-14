# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase

from ipywidgets import IntText, BoundedIntText, IntSlider, IntProgress


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


class BoundedIntBase(object):
    """ Mixin for tests common to all bounded int widgets """

    def create_widget(self, *args, **kwargs):
        return NotImplemented

    def test_construction_default_value(self):
        widget = self.create_widget()
        state = widget.get_state()
        assert state['value'] == 0
        assert state['min'] == 0
        assert state['max'] == 100

    def test_construction_explicit_arguments(self):
        widget = self.create_widget(52, -5, 81, 3)
        state = widget.get_state()
        assert state['value'] == 52
        assert state['min'] == -5
        assert state['max'] == 81

    def test_construction_with_kwargs(self):
        widget = self.create_widget(
            value=52,
            min=-5,
            max=81
        )
        state = widget.get_state()
        assert state['value'] == 52
        assert state['min'] == -5
        assert state['max'] == 81

    def test_value_bounded_at_min(self):
        textbox = self.create_widget(
            value=52,
            min=10,
            max=80
        )
        textbox.value = -21
        assert textbox.value == 10

    def test_value_bounded_at_max(self):
        textbox = self.create_widget(
            value=52,
            min=10,
            max=80
        )
        textbox.value = 421
        assert textbox.value == 80


class TestBoundedIntText(BoundedIntBase, TestCase):

    def create_widget(self, *args, **kwargs):
        return BoundedIntText(*args, **kwargs)


class TestIntSlider(BoundedIntBase, TestCase):

    def create_widget(self, *args, **kwargs):
        return IntSlider(*args, **kwargs)


class TestIntProgress(BoundedIntBase, TestCase):

    def create_widget(self, *args, **kwargs):
        return IntProgress(*args, **kwargs)
