from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as mediaserve

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace='Home')),
    path('about/', include('About.urls', namespace='About')),
    path('portfolio/', include('Portfolio.urls', namespace='Portfolio')),
    path('contact/', include('Contact.urls', namespace='Contact')),
    path('blog/', include('Blog.urls', namespace='Blog')),
    path('summernote/', include('django_summernote.urls'))
]


urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                       mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
