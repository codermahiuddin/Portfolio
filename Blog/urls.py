from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path("", views.BlogView.as_view(), name="Blog"),
    path('post/<slug>/', views.BlogDetails, name='Blog_Details'),
]