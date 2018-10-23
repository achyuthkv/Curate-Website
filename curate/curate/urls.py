from django.urls import include,path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from curateapp.views import collection
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', collection),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
