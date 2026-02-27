from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'page_title': 'Now Showing',
    }
    return render(request, 'bookings/home.html', context)

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
    return render(request, 'bookings/movie_detail.html', context)

