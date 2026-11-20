from datetime import timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Menu, Booking
class MenuModelTests(TestCase):
    def test_menu_string_representation(self):
        item=Menu.objects.create(title='Greek Salad',price='12.50',inventory=10)
        self.assertEqual(str(item),'Greek Salad : 12.50')
class ApiTests(TestCase):
    def setUp(self):
        self.client=APIClient(); self.user=User.objects.create_user(username='tester',password='TestPass123!')
        self.menu=Menu.objects.create(title='Bruschetta',price='8.50',inventory=12)
    def test_menu_list_is_public(self):
        response=self.client.get('/api/menu/'); self.assertEqual(response.status_code,200); self.assertEqual(response.data[0]['title'],'Bruschetta')
    def test_menu_detail_returns_item(self):
        response=self.client.get(f'/api/menu/{self.menu.id}/'); self.assertEqual(response.status_code,200); self.assertEqual(response.data['title'],'Bruschetta')
    def test_booking_requires_authentication(self): self.assertEqual(self.client.get('/api/bookings/').status_code,401)
    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        payload={'name':'Alex','no_of_guests':2,'booking_date':(timezone.now()+timedelta(days=1)).isoformat(),'comment':'Window seat if possible'}
        response=self.client.post('/api/bookings/',payload,format='json'); self.assertEqual(response.status_code,201); self.assertEqual(Booking.objects.count(),1)
