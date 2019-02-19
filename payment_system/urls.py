from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from checkout import views as checkout_views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^about/', views.about,name='about'),
    url(r'^contact/', views.contact,name='contact'),
    url(r'^checkout/', checkout_views.checkout,name='checkout'),
]

if settings.DEBUG:
    urlpatterns == static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns == static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
