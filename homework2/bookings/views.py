from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

# REST framework imports
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'page_title': 'Now Showing',
    }
    # use movie_list template
    return render(request, 'bookings/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    seats = movie.seats.all()

    # Organize seats by row
    rows = {}
    for seat in seats:
        row = seat.row or 'General'
        if row not in rows:
            rows[row] = []
        rows[row].append(seat)

    context = {
        'movie': movie,
        'rows': rows,
        'page_title': movie.title,
    }
    # show seat booking template
    return render(request, 'bookings/seat_booking.html', context)


# API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        movie = serializer.save()
        # create a default set of seats
        for row in ['A', 'B', 'C']:
            for num in range(1, 11):
                Seat.objects.create(movie=movie, seat_number=f"{row}{num}", row=row)


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        movie_id = self.request.query_params.get('movie')
        if movie_id:
            qs = qs.filter(movie_id=movie_id)
        return qs

    def create(self, request, *args, **kwargs):
        # custom booking via seats endpoint
        movie_id = request.data.get('movie')
        seat_id = request.data.get('seat')
        user = request.user if request.user.is_authenticated else None
        try:
            seat = Seat.objects.get(id=seat_id, movie_id=movie_id)
        except Seat.DoesNotExist:
            return Response({'error': 'Seat not found'}, status=status.HTTP_404_NOT_FOUND)
        if seat.is_booked:
            return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
        # mark as booked
        seat.is_booked = True
        seat.save()
        # create booking record if user
        if user:
            booking = Booking.objects.create(movie_id=movie_id, seat=seat, user=user)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Seat marked as booked'}, status=status.HTTP_201_CREATED)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # users only see their own bookings
        user = self.request.user
        return Booking.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        # ensure user and seat availability
        user = request.user
        movie_id = request.data.get('movie')
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id=seat_id, movie_id=movie_id)
        except Seat.DoesNotExist:
            return Response({'error': 'Seat not found'}, status=status.HTTP_404_NOT_FOUND)
        if seat.is_booked:
            return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
        # mark seat booked
        seat.is_booked = True
        seat.save()
        booking = Booking.objects.create(movie_id=movie_id, seat=seat, user=user)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def booking_history(request):
    if not request.user.is_authenticated:
        return HttpResponse('Please log in to view your booking history.', status=401)
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    context = {'bookings': bookings}
    return render(request, 'bookings/booking_history.html', context)

