from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from MainApp.models import Therapy


class StaticViewSitemap(Sitemap):
     def items(self):
         return Therapy.objects.all()