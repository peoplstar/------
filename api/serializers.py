from rest_framework import serializers

from .models import BoardStatus, Login, Reservation, Status


class LoginSerializer(serializers.ModelSerializer):
    lms_id = serializers.CharField(max_length = 15)
    lms_pw = serializers.CharField(max_length = 30)
    
    class Meta:
        model = Login
        fields = ('lms_id', 'lms_pw')
        
class StatusSerializer(serializers.ModelSerializer):
    day = serializers.CharField(max_length = 10)
    place = serializers.CharField(max_length = 20)
    
    class Meta:
       model = Status
       fields = ('day', 'place')
       
class ReservationSerializer(serializers.ModelSerializer):
    lms_id = serializers.CharField(max_length = 15)
    day = serializers.CharField(max_length = 10)
    place = serializers.CharField(max_length = 20)
    start_time = serializers.CharField(max_length = 10)
    end_time = serializers.CharField(max_length = 10)
    appd = serializers.BooleanField()
    
    class Meta:
       model = Reservation
       fields = ('lms_id', 'day', 'place', 'start_time', 'end_time', 'appd')
       
class BoardStatusSerializer(serializers.ModelSerializer):
    idx = serializers.IntegerField(max_length = 10, primary_key = True)
    title = serializers.CharField(max_length = 25)
    day = serializers.CharField(max_length = 15)
    
    class Meta:
       model = BoardStatus
       fields = ('idx', 'title', 'day')