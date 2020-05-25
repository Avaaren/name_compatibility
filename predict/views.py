from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import (
    Relationship,
    MaleName,
    FemaleName,
)
from .forms import RelationshipForm


class HomePageView(View):

    def get(self, request):
        form = RelationshipForm()
        return render(request, 'predict/home.html',  {'form': form})

    def post(self, request):
        form = RelationshipForm(request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            predict = get_object_or_404(
                Relationship,
                male_name=cd.get('male_name'),
                female_name=cd.get('female_name')
            )
            print(predict.get_absolute_url())
        return redirect(predict.get_absolute_url())


class PredictView(View):

    def get(self, request, name_slug):
        form = RelationshipForm()
        prediction = get_object_or_404(Relationship, slug=name_slug)
        return render(request, 'predict/home.html',  {'prediction': prediction,
                                                      'form': form})


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
