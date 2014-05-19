from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from rest_framework import routers
from tagsys import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'checks', views.CheckViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'locations', views.LocationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tagsys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^root/', include(router.urls), name="root"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', RedirectView.as_view(url="/root/")),
    url(r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)

urlpatterns += staticfiles_urlpatterns()
