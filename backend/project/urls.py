"""
Project URL configuration
"""
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # API specific paths are set by the 'urls.py' file in the 'api' directory
    path("api/", include("api.urls")),
    path("admin/", include("massadmin.urls")),
    path("admin/", admin.site.urls),
]
admin.site.site_header = "Program of Studies Administration"
admin.site.index_title = "Admin"
admin.site.site_url = "/"
# media file fix in development; not needed in production
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
