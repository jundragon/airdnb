from django.contrib import admin
from . import models


@admin.register(models.ReservationModel)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition"""

    pass
