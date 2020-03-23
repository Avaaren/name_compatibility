from django.urls import path

from . import views

app_name = 'predict'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('<slug:name_slug>/', views.PredictView.as_view(), name='predict')
]