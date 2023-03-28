from django.urls import path
from .views import (ListingListView, ListingDetailView, search,search1,search2,search3)


urlpatterns = [
    path('', ListingListView.as_view(), name='listings'),
    path('<int:pk>', ListingDetailView.as_view(), name='listing'),
    path('search', search, name='search'),
    path('search1', search1, name='search1'),
    path('search2', search2, name='search2'),
    path('search3', search3, name='search3'),
]
