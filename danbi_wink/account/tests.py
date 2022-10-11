from django.test import TestCase
from account.models import User

# Create your tests here.
class AccountTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        member = User.objects.create(name='byeonguk')

    def test_name_label(self):
        first_member =Member.objects.get(name='byeonguk').first_name
        self.assertEquals(first_name, 'first name')

    def test_age_bigger_19(self):
        age = Member.objects.get(name='byeonguk').age
        check_age = age > 19
        self.assertTrue(check_age)