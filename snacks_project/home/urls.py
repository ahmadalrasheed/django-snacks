from django.urls import path
from .views import Homepageview , Aboutuspageview

urlpatterns =[
    path('' , Homepageview.as_view() , name="home"),
    path('about-us' , Aboutuspageview.as_view() , name="about-us")
]
