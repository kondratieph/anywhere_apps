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


        # self.assertTrue(form.fields['title'].disabled)
        #
        # self.assertTrue(
        #     form.fields['title'].label == 'Testing...')



    # def test_empty_form(self):
    #     form = ToDoForm()
    #     self.assertInHTML(
    #         '<input type="text" name="title" id="title">', str(form)
    #     )
        # self.assertInHTML(
        #     '<input type="date" name="due_date" required id="due_date">', str(form)
        # )

    # def test_todo_form_title_field_label(self):
    #     form = ToDoForm()
    #
    #     self.assertTrue(form.fields['title'].label == None or form.fields['title'].label == 'title')

    # def test_renew_form_date_field_label(self):
    #     form = RenewBookForm()
    #     self.assertTrue(
    #         form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')
    #
    # def test_renew_form_date_field_help_text(self):
    #     form = RenewBookForm()
    #     self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')
    #
    # def test_renew_form_date_in_past(self):
    #     date = datetime.date.today() - datetime.timedelta(days=1)
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_too_far_in_future(self):
    #     date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_today(self):
    #     date = datetime.date.today()
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertTrue(form.is_valid())
    #
    # def test_renew_form_date_max(self):
    #     date = timezone.now() + datetime.timedelta(weeks=4)
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertTrue(form.is_valid())