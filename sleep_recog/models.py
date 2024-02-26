# sleep_recog/models.py


# sleep_recog_id => AUTO INCREMENT,PK
# blink_score => float
# move_score => float
# silence => float
# baby_cry => float
# baby_laughter => float

from django.db import models

class SleepRecogModel(models.Model):
    sleep_recog_id = models.AutoField(primary_key=True)
    blink_score = models.FloatField()
    move_score = models.FloatField()
    silence = models.FloatField()
    baby_cry = models.FloatField()
    baby_laughter = models.FloatField()

    def __str__(self):
        return f"Sleep Recog ID: {self.sleep_recog_id}"
