from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Movie, Category
from .forms import MovieForm


def home(request):

    search = request.GET.get("search")
    category = request.GET.get("category")

    movies = Movie.objects.all()

    if search:
        movies = movies.filter(title__icontains=search)

    if category:
        movies = movies.filter(category_id=category)

    categories = Category.objects.all()

    return render(
        request,
        "movies/home.html",
        {
            "movies": movies,
            "categories": categories,
        }
    )

@login_required
def add_movie(request):

    if request.method == "POST":

        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():

            movie = form.save(commit=False)

            movie.user = request.user

            movie.save()

            messages.success(request, "Movie added successfully!")

            return redirect("home")

    else:

        form = MovieForm()

    return render(
        request,
        "movies/add_movie.html",
        {
            "form": form
        }
    )

def movie_detail(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    return render(
        request,
        "movies/movie_detail.html",
        {
            "movie": movie
        }
    )
@login_required
def edit_movie(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if movie.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this movie.")

    if request.method == "POST":

        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():

            form.save()

            messages.success(request, "Movie updated successfully!")

            return redirect("movie_detail", movie.id)

    else:

        form = MovieForm(instance=movie)

    return render(
    request,
    "movies/edit_movie.html",
    {
        "form": form,
        "movie": movie,
    }
)

@login_required
def delete_movie(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if movie.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this movie.")

    if request.method == "POST":

        movie.delete()

        messages.success(request, "Movie deleted successfully!")

        return redirect("home")

    return render(
        request,
        "movies/delete_movie.html",
        {"movie": movie}
    )