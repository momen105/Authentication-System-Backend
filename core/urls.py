from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include,re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user_auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

