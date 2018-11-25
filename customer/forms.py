from django.shortcuts import render
from .models import person,info
from django import forms
from django.db import models
from django.contrib.admin import widgets
class postform(forms.ModelForm):
    class Meta:
        model=person
        fields=('firstname','lastname','dob','phone','address')
class postmovie(forms.ModelForm):
    class Meta:
        model=info
        fields=['moviename','genre','language','year','price','rentby']