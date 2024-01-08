from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('featured',views.featurepage),
    path('article',views.articlepage),
    path('general',views.generalpage),
    path('prophetic',views.propheticpage),
    path('spiritual',views.spiritualpage),
    path('social',views.socialpage),
    path('about',views.aboutpage),
   
]
