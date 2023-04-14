from django.contrib.sitemaps import Sitemap

from .models import Medicine


class MedicineSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 1
    protocol = "https"

    def items(self):
        return Medicine.objects.all()

    # will return the last time an article was updated
    def lastmod(self, obj):
        return obj.updated_at

    # returns the URL of the article object
    def location(self, obj):
        return f"/{obj.slug}"
