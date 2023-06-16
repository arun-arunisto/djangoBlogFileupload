from django.urls import path
from .views import index, blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name="home"),
    path('blog/<str:slug>/',blog,name="blog")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
