from datetime import timedelta, datetime

from django.test import TestCase

from todo.models import Todo


class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(name='Learn GitHub Actions',
                                   description='We need to create project which uses GitHub Actions')


    def test_str(self):
        todo = Todo.objects.get(pk=1)
        self.assertEqual(str(todo), f'{todo.name}')

    def test_get_absolute_url(self):
        todo = Todo.objects.get(pk=1)
        self.assertEqual(todo.get_absolute_url(), f'/{todo.pk}')