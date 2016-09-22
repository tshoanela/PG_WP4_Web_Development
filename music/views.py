from django.http import Http404
from django.http import HttpResponse
from .models import Album,Song

from django.shortcuts import render

# html = ''
# for album in all_albums:
#
#     # url = '/music/' + str(album.id) + '/'
# html += '<a href="'+ url +'">' + album.album_title+ '</a><br>'

def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {'all_albums':all_albums}

    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)


def details(request,album_id):
    try:
        albums = Album.objects.get(pk=album_id)
        context = {'albums': albums}
    except:
        raise Http404("Album with the given Id not found")

    return  render(request,'music/details.html',context)

def test(request):
    album = Album.objects.all()
    context = {'album':album}
    return render(request,'music/test.html',context)
