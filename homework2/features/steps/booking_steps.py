from behave import given, when, then
from django.test import Client

# imports will be resolved at runtime inside steps to ensure Django setup



@given('the database has a movie titled "{title}"')
def step_impl(context, title):
    from bookings.models import Movie
    # remove existing entries to keep clean state
    Movie.objects.filter(title=title).delete()
    Movie.objects.create(title=title, description='desc', release_date='2026-01-01', duration=90)

@given('that movie has at least one unbooked seat')
def step_impl(context):
    from bookings.models import Movie, Seat
    movie = Movie.objects.get()
    Seat.objects.create(movie=movie, seat_number='A1')

@when('I go to the movies page')
def step_impl(context):
    client = Client()
    context.response = client.get('/bookings/')

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.response.content.decode()

@when('I book the first available seat for "{title}"')
def step_impl(context, title):
    from bookings.models import Movie, Seat
    movie = Movie.objects.get(title=title)
    seat = Seat.objects.filter(movie=movie, is_booked=False).first()
    client = Client()
    # use API to book
    response = client.post('/bookings/api/seats/', {'movie': movie.id, 'seat': seat.id}, content_type='application/json')
    context.response = response
    context.seat_id = seat.id

@then('the seat should be marked as booked')
def step_impl(context):
    from bookings.models import Seat
    assert context.response.status_code == 201
    seat = Seat.objects.get(id=context.seat_id)
    assert seat.is_booked
