# drcoco_server/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sleep_recog/", include('sleep_recog.urls')) # sleep_recog 앱 urls
]
