from django.urls import path
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('',views.MyPortfolioView.as_view(), name='Portfolio')
]