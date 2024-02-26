# sleep_recog/serializers.py


from rest_framework import serializers
from .models import SleepRecogModel

class SleepRecogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepRecogModel
        fields = ['blink_score', 'move_score', 'silence', 'baby_cry', 'baby_laughter']