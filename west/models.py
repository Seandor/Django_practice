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
        return self.id, self.name, self.sex
