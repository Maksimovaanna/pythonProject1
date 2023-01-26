from django.test import TestCase
from proj.models import car
from proj.views import plswork, mygod

class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        car.objects.create(id='1', moddel='Toyota', nomer='12kf3r23', voditel='Anna', online='da')

    def test_id_label(self):
        test = car.objects.get(id=1)
        field_label = test._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_model_label(self):
        test = car.objects.get(id=1)
        field_label = test._meta.get_field('moddel').verbose_name
        self.assertEquals(field_label, 'moddel')

    def test_nomer_label(self):
        test = car.objects.get(id=1)
        field_label = test._meta.get_field('nomer').verbose_name
        self.assertEquals(field_label, 'nomer')

    def test_login_max_length(self):
        test = car.objects.get(id=1)
        max_length = test._meta.get_field('moddel').max_length
        self.assertEquals(max_length, 50)

    def test_passw_max_length(self):
        test = car.objects.get(id=1)
        max_length = test._meta.get_field('nomer').max_length
        self.assertEquals(max_length, 50)

    def test_for_display(self):
        display = plswork("<WSGIRequest: GET '/'>").__str__()
        self.assertEquals(display, "<HttpResponse status_code=200, \"text/html; charset=utf-8\">")

    def test_for_records(self):
        expected_num = mygod()
        self.assertEquals(expected_num, 3)