# sleep_recog/urls.py


from django.urls import path
from .views import SleepRecogAPIView

urlpatterns = [
    path('sleep_recog_data_input/', SleepRecogAPIView.as_view(), name='sleep_recog_post'),
]
