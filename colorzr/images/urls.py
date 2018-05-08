from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from images import views

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)/$',
        views.ImageDeleteView.as_view(),
        name='delete'),
    url(r'^upload/$', views.ImageAddView.as_view(), name='upload'),
    url(r'^album/(?P<username>\w{0,50})/$',
        views.AlbumView.as_view(),
        name='album'),
    url(r'^album/$', views.AlbumView.as_view(), name='my_album'),
]
