from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap


from medicine.views import home, details, privacy_policy_view, robots_txt


from medicine.sitemaps import MedicineSiteMap

sitemaps = {"medicine": MedicineSiteMap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("<slug>", details, name="details"),
    path("privacy-policy", privacy_policy_view, name="privacy-policy"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", robots_txt, name="robotstext"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
