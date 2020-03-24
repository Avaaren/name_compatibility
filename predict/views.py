from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .names import create
from .models import (
    Relationship,
    MaleName,
    FemaleName,
)


class HomePageView(View):

    def get(self, request):

        return render(request, 'predict/home.html',  {})


class PredictView(View):

    def get(self, request):
        return render(request, 'predict/home.html',  {})


def ajax_search_male(request):
    response_data = {}
    search_request = request.GET.get('search_request')

    result_set = MaleName.objects.filter(name__icontains=search_request)[:5]
    result_set = [str(result) for result in result_set]
    response_data['result_set'] = result_set

    return JsonResponse(response_data)


def ajax_search_female(request):
    response_data = {}
    search_request = request.GET.get('search_request')

    result_set = FemaleName.objects.filter(name__icontains=search_request)[:5]
    result_set = [str(result) for result in result_set]
    response_data['result_set'] = result_set

    return JsonResponse(response_data)
