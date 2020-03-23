from django.shortcuts import render
from django.views.generic import View
from .names import create


class HomePageView(View):
   
    def get(self, request):
        return render(request, 'predict/home.html',  {})


class PredictView(View):

    def get(self, request):
        return render(request, 'predict/home.html',  {})