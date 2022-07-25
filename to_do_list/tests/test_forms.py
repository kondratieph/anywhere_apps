from django.test import TestCase
from django.http import HttpRequest
from to_do_list.forms import ToDoForm
from to_do_list.models import ToDo


class ToDoFormTest(TestCase):

    def test_empty_form(self):
        form = ToDoForm()
        self.assertIn("title", form.fields)
        self.assertIn("status", form.fields)
        self.assertIn("due_date", form.fields)

    def test_filled_form(self):
        request = HttpRequest()
        request.POST = {
            "title": 'Testing...',
            "status": "False",
            "due_date": "2023-06-03",
        }
        form = ToDoForm(request.POST)
        self.assertIn("title", form.fields)
        self.assertIn("status", form.fields)
        self.assertIn("due_date", form.fields)
        form.save()
        self.assertEqual(ToDo.objects.count(), 1)