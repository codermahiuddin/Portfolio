from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path("", views.BlogView.as_view(), name="Blog"),
    path('blog/<slug>/', views.BlogDetails.as_view(), name='Blog_Details'),
]