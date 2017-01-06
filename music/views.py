from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Album,Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    return render(request, 'detail.html', {'album': album})

