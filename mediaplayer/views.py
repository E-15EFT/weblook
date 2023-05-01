from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import UploadMovie
from .forms import UploadMovieForm
from django.conf import settings



def homet(request):
   
    
    queryset = UploadMovie.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(queryset, 12)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, "home.html", {"movies": movies})


def play_movie(request, slug):
    instance = get_object_or_404(UploadMovie, slug=slug)
    return render(request, "play_movie.html", {"instance": instance})


def add_movie(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = UploadMovieForm(request.POST, request.FILES)
            if fm.is_valid():
                obj = fm.save(commit=False)
                obj.slug = slugify(obj.title)
                obj.user = request.user
                obj.save()
                fm.save_m2m()
                messages.success(request, "Movie Uploaded Successfully")
                return HttpResponseRedirect("/")
        fm = UploadMovieForm()
        return render(request, "add_movie.html", {"form": fm})
    else:
        messages.warning(request, "Please Login First")
    return HttpResponseRedirect("admin/login/")
