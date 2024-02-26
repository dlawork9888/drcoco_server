# sleep_recog/views.py


from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SleepRecogModel
from .serializers import SleepRecogModelSerializer
# sklearn for SVM
import joblib
import numpy as np
import os

# catboost로 판단 모델 설정
loaded_model = joblib.load('sleep_recog/recog_models/catboost_model.pkl')

class SleepRecogAPIView(APIView):
    def post(self, request, format=None):
        serializer = SleepRecogModelSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            input_data = np.array([[data['blink_score'], data['move_score'], data['silence'], data['baby_cry'], data['baby_laughter']]])
            # 설정된 모델로 예측 실행
            prediction = loaded_model.predict(input_data)
            print(f'sleep recog prediction: {prediction}')
            #serializer.save() # 저장 안함!
            return Response(prediction, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

