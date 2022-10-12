from django.test import TestCase, Client
from account.models import User
import json

# Create your tests here.
client = Client() 
class AccountTestClass(TestCase):

    def test_signup(self):
        # signup - success
        data = {
            "email"        : "test@test.com",
            "name"         : "TEST",
            "password"     : "1q2w3e4r!",
        }
        response = client.post('/signup', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "회원가입 성공")
        self.assertIsNotNone(response.json().get('token'))

        # email is used
        data = {
            "email"        : "test@test.com", # used email
            "name"         : "TEST",
            "password"     : "1q2w3e4r!",
        }
        response = client.post('/signup', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

        # password not valid
        data = {
            "email"        : "test2@test.com",
            "name"         : "TEST",
            "password"     : "1q2w3e4r", # invalid pw
        }
        response = client.post('/signup', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)


    def test_signin(self):
        # user_preset
        data = {
            "email"        : "test@test.com",
            "name"         : "TEST",
            "password"     : "1q2w3e4r!",
        }
        client.post('/signup', json.dumps(data), content_type = 'application/json')

        # login for email, password - success
        data = {
            "email"        : "test@test.com",
            "password"     : "1q2w3e4r!",
        }
        response = client.post('/signin', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "로그인 성공")
        self.token = response.json()['token']
        
        # login for email, password - failed
        data = {
            "email"        : "test@test.com",
            "password"     : "password", # invalid pw
        }
        response = client.post('/signin', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

        # token refresh
        data = {
            "refresh"      : f"{self.token['refresh']}",
        }
        response = client.post('/token/refresh', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        