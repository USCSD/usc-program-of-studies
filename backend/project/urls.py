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
    path(r'admin/', include('massadmin.urls')),
    path("admin/", admin.site.urls),

    # Path for the Vue Single-Page Application (SPA)
    re_path(r'^app/(.*)$', 
            TemplateView.as_view(
                template_name="spa.html",
                extra_context={ "ENV_NAME": settings.ENV_NAME }),
            name="app")
]
admin.site.site_header= "Program of Studies Administration"
admin.site.index_title= ""
admin.site.site_url= "/app"
# media file fix in development; not needed in production
if settings.DEBUG is True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
