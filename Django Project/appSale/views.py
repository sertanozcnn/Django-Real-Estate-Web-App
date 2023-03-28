from re import search
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import path,include
from appSale.models import housesale,Users,Price,House_Category,Realtor_Menu,ContactForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView)
from django.utils.translation import gettext_lazy as _

from appSale.models import State
from listings.models import Listing, ListingType
from accounts.models import Realtor



# def index(request):
#   house=housesale.objects.all()
#   price=Price.objects.all() 

  
#   return render(request, 'index.html',{'house':house,'price':price}) 


def index(request):
  listings=Listing.objects.order_by('-created').filter(is_published=True)[:9]
  states=State.objects.all()
  list_types=ListingType.objects.all()
  price=Price.objects.all() 
  realtor_menu=Realtor_Menu.objects.all()

  
  return render(request, 'index.html',{'listings':listings,'states':states,'list_types':list_types,'price':price,'realtor_menu':realtor_menu}) 







class indexList(TemplateView):
    template_name = 'templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = Listing.objects.order_by('-created').filter(
                               is_published=True)[:3]
        context['states'] = State.objects.all()
        context['list_types'] = ListingType.objects.all()
        context['index'] = True
        # SEO
        context['page_title'] = _("Real estate manager."
                                  " Renting, buying and selling.")
        context['page_description'] = _("Real estate manager. We offer"
                                        " real estate objects and takes care"
                                        " of every aspect for you. Services"
                                        " offered: renting, selling, buying,"
                                        " consultation and way more.")
        return context




def about(request):
  return render(request, 'about.html')

def subscribe(request):
  return render(request, 'subscribe.html')
def house(request):
  house=housesale.objects.all()
  return render(request, 'house.html',{'house':house})
def price(request):
  price=Price.objects.all()
  return render(request, 'price.html',{'price':price})

def contact(request):
      if request.method == 'POST':
        contact=ContactForm()
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        c_phone = request.POST.get('c_phone')
        c_message = request.POST.get('c_message')
        a1=('contact.html')
        a2=('email.html')
        contact.contact_name=c_name
        contact.contact_email=c_email
        contact.contact_phone=c_phone
        contact.contact_messages=c_message
        contact.save()
        

      return render(request, 'contact.html')
    

    


@login_required(login_url="/login/")

# def home(request):  
#     searchTerm = request.GET.get('searchMovie')
#     return render(request, 'home.html',{'searchTerm':searchTerm})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})


# Create your views here.
