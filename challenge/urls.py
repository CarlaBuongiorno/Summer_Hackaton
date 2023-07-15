# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('locations/',views.location,name="location"),
    path('challenge/<int:id>/',views.challenge,name="challenge"),
    path('answers/<int:id>/',views.answer,name="answer"),
]