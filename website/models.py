import os
from django.db import models
from os.path import join

class PersonManager(models.Manager):
    def createCard(self, firstName, lastName, email, phoneNo, position, fb, linkedin):
        person = self.create(firstName=firstName, lastName=lastName, email=email, phoneNo=phoneNo, position=position, fb=fb, linkedin=linkedin)
        return person

class PersonManager_2(models.Manager):
    def createCard(self, firstName, lastName, email, phoneNo, department, fb, linkedin):
        person = self.create(firstName=firstName, lastName=lastName, email=email, phoneNo=phoneNo, department=department, fb=fb, linkedin=linkedin)
        return person

class GalleryManager(models.Manager):
    def createGallery(self, galleryName, thumbnail):
        gallery = self.create(galleryName=galleryName, thumbnail=thumbnail)
        return gallery

class PictureManager(models.Manager):
    def createPicture(self, picsrc):
        pics = self.create(picsrc=picsrc)
        return pics


class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    phoneNo = models.CharField(max_length=20)
    position = models.CharField(max_length=120)
    fb = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    persons = PersonManager()

class EventManager(models.Manager):
  def createEvent(self, title, picUrl, date, content):
    event = self.create(title=title, picUrl=picUrl, date=date, content=content)
    return event

class Talks(models.Model):
    title = models.CharField(max_length=255)
    picUrl = models.CharField(max_length=255)
    date =  models.DateField()
    content = models.TextField()
    events_talks = EventManager()

class Hackathons(models.Model):
    title = models.CharField(max_length=255)
    picUrl = models.CharField(max_length=255)
    date =  models.DateField()
    content = models.TextField()
    events_hackathons = EventManager()

class Workshops(models.Model):
    title = models.CharField(max_length=255)
    picUrl = models.CharField(max_length=255)
    date =  models.DateField()
    content = models.TextField()
    events_workshops = EventManager()

class Person_2(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    phoneNo = models.CharField(max_length=20)
    department = models.CharField(max_length=120)
    fb = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    persons = PersonManager_2()

class Album(models.Model):
    galleryName = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=50)
    all_albums = GalleryManager()


class Pictures(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    picsrc = models.CharField(max_length=50)
    pics = PictureManager()
    #pik = PictureManager()