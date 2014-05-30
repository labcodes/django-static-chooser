#coding: utf-8

from django.test import TestCase
from django.conf import settings
from django.template import Template, Context
from django.test.utils import override_settings


class StaticFilesProductionTestCase(TestCase):

    def test_with_param(self):
        """static tag should return remote url on debug false"""
        template = Template(
            "{% load staticfiles2 %}{% static 'local/path' http://remote.url %}"
        )
        c = Context({})
        self.assertEqual(template.render(c), "http://remote.url")

    def test_without_param(self):
        """static tag should return local path in absense of remote url"""
        template = Template(
            "{% load staticfiles2 %}{% static 'local/path' %}"
        )
        c = Context({})
        expected = settings.STATIC_URL + 'local/path'
        self.assertEqual(template.render(c), expected)


class StaticFilesDevelopmentTestCase(TestCase):

    @override_settings(DEBUG=True)
    def test_with_param(self):
        """static tag should return remote url on debug false"""
        template = Template(
            "{% load staticfiles2 %}{% static 'local/path' http://remote.url %}"
        )
        c = Context({})
        expected = settings.STATIC_URL + 'local/path'
        self.assertEqual(template.render(c), expected)

    @override_settings(DEBUG=True)
    def test_without_param(self):
        """static tag should return remote url on debug false"""
        template = Template(
            "{% load staticfiles2 %}{% static 'local/path' %}"
        )
        c = Context({})
        expected = settings.STATIC_URL + 'local/path'
        self.assertEqual(template.render(c), expected)


