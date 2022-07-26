from django.test import TestCase
from django.urls import reverse
import datetime
from to_do_list.views import ToDo


class ToDoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 4 items for tests
        number_of_todo_items = 4
        for todo_item in range(number_of_todo_items):
            ToDo.objects.create(title='Untitled Task', status='False', due_date=datetime.date(2023, 7, 14))

    # Index page tests
    def test_index_url_exists_at_desired_location(self):
        resp = self.client.get('/app/do/')
        self.assertEqual(resp.status_code, 200)

    def test_index_url_accessible_by_name(self):
        resp = self.client.get(reverse('todo:index'))
        self.assertEqual(resp.status_code, 200)

    def test_index_uses_correct_template(self):
        resp = self.client.get(reverse('todo:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'to_do_list/index.html')


    # Edit page tests
    def test_edit_url_exists_at_desired_location(self):
        todo_item = ToDo.objects.get(id=1)
        resp = self.client.get(reverse('todo:edit_todo', args=(todo_item.pk, )))
        self.assertEqual(resp.status_code, 200)

    def test_edit_uses_correct_template(self):
        todo_item = ToDo.objects.get(id=1)
        resp = self.client.get(reverse('todo:edit_todo', args=(todo_item.pk, )))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'to_do_list/edit.html')

    # Options tests
    def test_delete_url_works_properly(self):
        todo_item = ToDo.objects.get(id=1)
        resp = self.client.get(reverse('todo:delete_todo', args=(todo_item.pk, )))
        self.assertEqual(resp.status_code, 302)

    def test_status_url_works_properly(self):
        todo_item = ToDo.objects.get(id=1)
        resp = self.client.get(reverse('todo:change_status', args=(todo_item.pk, )))
        self.assertEqual(resp.status_code, 302)
