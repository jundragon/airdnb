from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.AbstractTimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ Room Type Object Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Object Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ House Rule Object Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.AbstractTimeStampedModel):

    """ Photo Object Definition """

    caption = models.CharField(max_length=140)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.AbstractTimeStampedModel):

    """ Room Model Definition """

    # Required Fields
    name = models.CharField(max_length=140)
    description = models.TextField()
    price = models.IntegerField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # Not Required Fields
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilites = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
