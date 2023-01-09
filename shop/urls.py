from django.urls import path
from . import views

urlpatterns = [
    path("",views.product,name='homeshop'),
    path("auto/",views.autocomplete,name='auto'),
    path("search/",views.search,name='search'),
    path("about/",views.about,name='about'),
    path("contactUs/",views.contactUs,name='contactUs'),
    path("tracker/",views.tracker,name='tracker'),
    path("products/<int:myid>",views.productView,name='productView'),
    path("checkout/",views.checkout,name='checkout'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
