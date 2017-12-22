from django.shortcuts import render
from . import models
import os
from django.core import serializers
from .models import Album

def contact(request):
    return render(request, 'website/contact.html')

# home part


def home(request):
    return render(request, 'website/index.html')
# about part


def team(request):
    person = models.Person.persons.all()
    return render(request, 'website/team.html',{ 'person': person })


def success_stories(request):
    return render(request, 'website/success_stories.html')

# Events part

def events(request):
    events_talks = models.Talks.events_talks.all()
    events_hackathons = models.Hackathons.events_hackathons.all()
    events_workshops = models.Workshops.events_workshops.all()
    return render(request, 'website/events.html', {'events_talks' : events_talks, 'events_hackathons' : events_hackathons, 'events_workshops' : events_workshops })

# associates part


def associates(request):
    return render(request, 'website/associates.html')


def partners(request):
    return render(request, 'website/partners.html')


def sponsors(request):
    return render(request, 'website/sponsors.html')

# gallery


def gallery(request):

    all_albums = models.Album.all_albums.all()
    pics = models.Pictures.pics.all()
    
    return render(request, 'website/galleryitem.html', {'all_albums': all_albums, 'pics' : pics })
    


    #a = []
    #for root, dirs, files in os.walk('./website/STATIC/images/gallery'):
     #   a.append(files)
    #return render(request, 'website/galleryitem.html',{ 'image': a })

# mentors


def industry(request):
    return render(request, 'website/industry.html')


def students(request):
    return render(request, 'website/students.html')


def faculty(request):
    return render(request, 'website/faculty.html')

# e resources


def e_resources(request):
	return render(request,'website/e-resources.html')

# team

def vision(request):
    return render(request, 'website/vision.html')
