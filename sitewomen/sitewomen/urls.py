from django.contrib import admin
from django.urls import path, include
from women.views import page_not_found
from sitewomen import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from women.sitemaps import PostSiteMap, CategorySiteMap
from django.views.decorators.cache import cache_page


sitemaps = {
    "posts": PostSiteMap,
    "cats": CategorySiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path("users/", include("users.urls", namespace="users")),
    path('__debug__/', include('debug_toolbar.urls')),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path('captcha/', include('captcha.urls')),
    path(
        "sitemap.xml",
        cache_page(1200 * 60)(sitemap),
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные женщины мира'
