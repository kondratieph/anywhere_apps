from django.test import TestCase
from to_do_list.models import ToDo
import datetime

class ToDoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        ToDo.objects.create(title='Untitled Task', status='False', due_date=datetime.date(2023, 7, 14))

    def test_title_label(self):
        todo_item = ToDo.objects.get(id=1)
        field_label = todo_item._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_status_label(self):
        todo_item = ToDo.objects.get(id=1)
        field_label = todo_item._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')


    def test_date_label(self):
        todo_item = ToDo.objects.get(id=1)
        field_label = todo_item._meta.get_field('due_date').verbose_name
        self.assertEquals(field_label, 'due date')

    def test_title_max_length(self):
        todo_item = ToDo.objects.get(id=1)
        max_length = todo_item._meta.get_field('title').max_length
        self.assertEquals(max_length, 80)