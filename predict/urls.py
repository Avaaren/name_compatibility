from django.urls import path

from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('<slug:name_slug>/', views.PredictView.as_view(), name='predict')
    path('ajax_search_male/', views.ajax_search_male, name='search_male'),
    path('ajax_search_female/', views.ajax_search_female, name='search_female'),
]