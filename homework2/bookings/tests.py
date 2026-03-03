from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking


class ModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A movie for testing',
            release_date='2026-01-01',
            duration=120,
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_number='A1')
        self.user = User.objects.create_user('user1', password='pass')

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'Test Movie')

    def test_seat_str(self):
        self.assertIn('A1', str(self.seat))

    def test_booking_creation(self):
        booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)
        self.assertEqual(str(booking), f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}")


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('apiuser', password='testpass')
        self.movie = Movie.objects.create(
            title='API Movie',
            description='API Description',
            release_date='2026-02-02',
            duration=90,
        )
        # create seats
        for i in range(1, 6):
            Seat.objects.create(movie=self.movie, seat_number=f'A{i}')

    def test_movie_list(self):
        response = self.client.get('/bookings/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_movie_creation(self):
        data = {
            'title': 'New Movie',
            'description': 'Desc',
            'release_date': '2026-03-03',
            'duration': 100,
        }
        response = self.client.post('/bookings/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_seat_booking_endpoint(self):
        seat = Seat.objects.filter(movie=self.movie).first()
        # mark as booked without login
        response = self.client.post('/bookings/api/seats/', {'movie': self.movie.id, 'seat': seat.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        seat.refresh_from_db()
        self.assertTrue(seat.is_booked)

    def test_booking_history_requires_auth(self):
        response = self.client.get('/bookings/api/bookings/')
        # should return 403 or unauthorized
        self.assertIn(response.status_code, (status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED))
        self.client.login(username='apiuser', password='testpass')
        response = self.client.get('/bookings/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_booking_creation_endpoint(self):
        # use seat and movie created in setUp
        self.client.login(username='apiuser', password='testpass')
        seat = Seat.objects.filter(movie=self.movie, is_booked=False).first()
        data = {'movie': self.movie.id, 'seat': seat.id}
        response = self.client.post('/bookings/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        seat.refresh_from_db()
        self.assertTrue(seat.is_booked)
        # booking belongs to user
        self.assertEqual(response.data['user'], self.user.id)
