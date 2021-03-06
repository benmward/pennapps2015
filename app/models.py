from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class DonationCenter(models.Model):
    name = models.CharField(max_length=100)
    dropoff_notes = models.CharField(max_length=1000)
    icon_image = models.CharField(max_length=1000)

    FOOD = 'fd'
    CLOTHING = 'cl'
    TOYS = 'ty'
    HOUSEHOLD_ITEMS = 'hi'
    INDUSTRY_CHOICES = (
        (FOOD, 'Food'),
        (CLOTHING, 'Clothing'),
        (TOYS, 'Toys'),
        (HOUSEHOLD_ITEMS, 'Household Items'),
    )
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, default=FOOD)

    address = models.ForeignKey('Address')
    coordinate = models.ForeignKey('Coordinate')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)

class Address(models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.num)+" "+self.street+" "+self.city+", "+self.state+" "+self.zipcode

class Coordinate(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):              # __unicode__ on Python 2
        return str(self.longitude)+" "+str(self.latitude)

class Pickup(TimeStampedModel):
    manifest = models.CharField(max_length=100, verbose_name="Donation Contents")
    pickup_name = models.CharField(max_length=100, verbose_name="Your Name")
    pickup_address = models.CharField(max_length=100, verbose_name="Your Address")
    pickup_phone_number = models.CharField(max_length=20, verbose_name="Your Phone Number")
    pickup_business_name = models.CharField(max_length=100, verbose_name="Your Bussiness Name")
    pickup_notes = models.CharField(max_length=200, verbose_name="Pickup Notes")
    dropoff = models.ForeignKey(DonationCenter, verbose_name="Dropoff Location")
    #dropoff_notes = models.CharField(max_length=200)
    delivery_id = models.CharField(max_length=20)
    quote_id = models.CharField(max_length=20)

    def __str__(self):
        return self.manifest
