from django.db import models

class Character(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    id   = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    sex  = models.CharField(max_length=2, choices=GENDER_CHOICES)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
