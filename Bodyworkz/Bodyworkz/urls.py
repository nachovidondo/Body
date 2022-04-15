
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from MainApp.models import TherapiesSitemaps
from MainApp.sitemaps import StaticViewSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'therapies': TherapiesSitemaps,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainApp.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
         ]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)