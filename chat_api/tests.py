from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from .models import Message



valid_payload_data = {
    'text': 'test text',
    'author_email':'test@example.com'
}

invalid_text_blank_payload_data = {
    'text': ' ',
    'author_email':'test@example.com'
}

invalid_text_more_than_100_payload_data = {
    'text': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.',
    'author_email':'test@example.com'
}

invalid_email_payload_data = {
    'text': 'test text',
    'author_email':'test@err'
}




class MessageCreateTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_message_with_valid_data(self):
        response = self.client.post('/api/v1/messages/create/', data=valid_payload_data, format='json',)
        self.assertEqual(response.status_code, 201)

    def test_create_message_with_invalid_text_blank(self):
        response = self.client.post('/api/v1/messages/create/', data=invalid_text_blank_payload_data, format='json',)
        self.assertEqual(response.status_code, 400)

    def test_create_message_with_invalid_text_more_than_100(self):
        response = self.client.post('/api/v1/messages/create/', data=invalid_text_more_than_100_payload_data, format='json',)
        self.assertEqual(response.status_code, 400)

    def test_create_message_with_invalid_email(self):
        response = self.client.post('/api/v1/messages/create/', data=invalid_email_payload_data, format='json',)
        self.assertEqual(response.status_code, 400)

