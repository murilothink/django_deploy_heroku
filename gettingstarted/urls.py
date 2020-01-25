from django.urls import path, include

from django.contrib import admin
from django.conf import settings
admin.autodiscover()
from django.conf.urls.static import static
import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
