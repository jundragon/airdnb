from django.db import models


class AbstractTimeStampedModel(models.Model):

    """ Abstract Time Stamped Model Definition """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
