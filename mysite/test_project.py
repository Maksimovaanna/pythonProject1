from django.test import TestCase
from proj.models import uchet
from proj.views import plswork, mygod

class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        uchet.objects.create(id='1', login='Fedor', passw='passw', propusk='123')

    def test_id_label(self):
        test = uchet.objects.get(id=1)
        field_label = test._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_login_label(self):
        test = uchet.objects.get(id=1)
        field_label = test._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_passw_label(self):
        test = uchet.objects.get(id=1)
        field_label = test._meta.get_field('passw').verbose_name
        self.assertEquals(field_label, 'passw')

    def test_login_max_length(self):
        test = uchet.objects.get(id=1)
        max_length = test._meta.get_field('login').max_length
        self.assertEquals(max_length, 50)

    def test_passw_max_length(self):
        test = uchet.objects.get(id=1)
        max_length = test._meta.get_field('passw').max_length
        self.assertEquals(max_length, 50)

    def test_for_display(self):
        display = plswork("<WSGIRequest: GET '/'>").__str__()
        self.assertEquals(display, "<HttpResponse status_code=200, \"text/html; charset=utf-8\">")

    def test_for_records(self):
        expected_num = mygod()
        self.assertEquals(expected_num, 3)