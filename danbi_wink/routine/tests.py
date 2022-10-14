from unicodedata import category
from django.test import TestCase, Client
from account.models import User
from routine.models import Routine, Result, Day 
import json

# Create your tests here.
client = Client() 
class RoutineTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create test user
        User.objects.create_user(
            email="test@test.com",
            name="TEST",
            password="1q2w3e4r!"
        )
        u = User.objects.get(name="TEST")
        # create test data
        Routine.objects.create(
            title="TEST",
            account_id=u,
            category="HOMEWORK",
            goal="TEST ROUTINE DATA",
            is_alarm= True,
        )
        r = Routine.objects.get(title='TEST')
        Day.objects.create(
            routine_id = r.routine_id,
            day=['MON', 'TUE', 'WED', 'THU', 'FRI']
        )

    def setUp(self):
        # get token
        data = {
            "email"        : "test@test.com",
            "password"     : "1q2w3e4r!",
        }
        response = client.post('/token', json.dumps(data), content_type = 'application/json')
        self.token = response.json()['access']

    def test_create_routine(self):
        data = {
            "title" : "problem solving",
            "category" : "HOMEWORK",
            "goal": "Increase your problem-solving skills",
            "is_alarm": True,
            "days": ["MON", "WED", "FRI"]
        }
        header = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        response = client.post('/routine', json.dumps(data), content_type = 'application/json', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message']['msg'], "You have successfully created the routine.")


    def test_retrieve_routine(self):
        ...

    def test_detail_routine(self):
        ...

    def test_update_routine(self):
        ...

    def test_delete_routine(self):
        ...

    def test_create_routine_result(self):
        ...
