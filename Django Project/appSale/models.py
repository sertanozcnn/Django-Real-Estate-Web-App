from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class housesale(models.Model):
    housesale_ID = models.IntegerField(primary_key = True)
    housesale_title = models.CharField(max_length=30) 
    housesale_description= models.CharField(max_length=250)
    housesale_image= models.ImageField(upload_to='house',null=True,blank=True)
    def __str__(self):
        return self.housesale_title


class Users(models.Model):
   User_ID = models.IntegerField(primary_key = True)
   User_Name = models.CharField(max_length=20)
   User_LastName = models.CharField(max_length=20)  
   User_Mail = models.EmailField(max_length = 254)
   User_Date= models.DateField()

   def __str__(self):
        return self.User_Mail


class Price(models.Model):
   Price_ID = models.IntegerField(primary_key = True)
   Price_Number = models.CharField(max_length=20)
   Price_Special = models.CharField(max_length=20)  
   Price_Money= models.CharField(max_length=50) 
   Price_Line1= models.CharField(max_length=50) 
   Price_Line2= models.CharField(max_length=50) 
   Price_Line3= models.CharField(max_length=50) 
   Price_Line4= models.CharField(max_length=50) 
   Price_Line5= models.CharField(max_length=50) 
   Price_Line6= models.CharField(max_length=50) 
   Price_URL = models.CharField(max_length = 200)

   def __str__(self):
        return self.Price_Special
    

class ContactForm(models.Model):
    contact_name=models.CharField(max_length=200)
    contact_email=models.EmailField()
    contact_phone=models.CharField(max_length=200)
    contact_messages=models.TextField()
    
    def __str__(self):
      return self.contact_name



   
class Realtor_Menu(models.Model):
   Realtor_ID = models.IntegerField(primary_key = True)
   Realtor_Name = models.CharField(max_length=200)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
   Realtor_Photo =  models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
   
   Realtor_Line1= models.CharField(max_length=1500) 
   Realtor_Line2= models.CharField(max_length=200) 
   Realtor_Line3= models.CharField(max_length=200) 
   Realtor_URL = models.CharField(max_length = 200)

   def __str__(self):
        return self.Realtor_Name
    
    
class House_Category(models.Model):
   House_Category_ID = models.IntegerField(primary_key = True)
   HouseType = models.CharField(max_length=20)
   def __str__(self):
        return self.HouseType
    
    



# ================================================================== >> COUNTRY
class Country(models.Model):
    """Country Model."""

    name = models.CharField(
        max_length=150, null=False, blank=False, unique=True)

    shortcut = models.CharField(
        max_length=3, null=False, blank=False, verbose_name="ISO 3166-α2")

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return f'{self.name}'



# ==================================================================== >> STATE
class State(models.Model):
    """State Model.
    Example:
        country_id      1 - Germany
        name            Berlin
    """

    country = models.ForeignKey(Country, null=False, on_delete=models.CASCADE,
                                verbose_name=_("Country"))
    name = models.CharField(max_length=150, blank=False, null=False,
                            verbose_name=_("Country"))
    shortcut = models.CharField(
        max_length=6, null=False, blank=False, verbose_name="ISO 3166-2")

    class Meta:
        unique_together = ('country', 'shortcut')
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return (f"{self.name} - {self.country.name}")



# ================================================================== >> ADDRESS
class Address(models.Model):
    """Address Model."""
    street = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name=_("Street"))
    hn = models.CharField(max_length=15, blank=False, null=False,
                          verbose_name=_("House number"))
    zipcode = models.CharField(max_length=5, blank=False, null=False,
                               verbose_name=_("Zipcode"))
    city = models.CharField(max_length=100, blank=False, null=False,
                            verbose_name=_("City"))
    state = models.ForeignKey(
        State, blank=False, null=False, on_delete=models.CASCADE,
        verbose_name=_("State"))


    class Meta:
        unique_together = ('street', 'hn', 'zipcode')
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return (f"{self.street} {self.hn}, {self.city}"
                f" - {self.state.country.shortcut}")

    def get_listings(self):
        return self.street
