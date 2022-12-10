from rest_framework import serializers

from .models import BoardStatus, BoardWrite, Login, Reservation, Status, Comments, BoardRead, AdminPassword


class LoginSerializer(serializers.ModelSerializer):
    lms_id = serializers.CharField(max_length = 15)
    lms_pw = serializers.CharField(max_length = 30)
    
    class Meta:
        model = Login
        fields = ('lms_id', 'lms_pw')

class AdminPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 30)
    
    class Meta:
        model = AdminPassword
        fields = ('password',)
        
class StatusSerializer(serializers.ModelSerializer):
    day = serializers.CharField(max_length = 10)
    place = serializers.CharField(max_length = 20)
    
    class Meta:
       model = Status
       fields = ('day', 'place')
       
class ReservationSerializer(serializers.ModelSerializer):
    mode = serializers.CharField(max_length = 5)
    lms_id = serializers.CharField(max_length = 15)
    day = serializers.CharField(max_length = 10)
    place = serializers.CharField(max_length = 20)
    start_time = serializers.CharField(max_length = 10)
    end_time = serializers.CharField(max_length = 10)
    appd = serializers.CharField(max_length = 3)
    
    class Meta:
       model = Reservation
       fields = ('mode', 'lms_id', 'day', 'place', 'start_time', 'end_time', 'appd')
       
class BoardStatusSerializer(serializers.ModelSerializer):
    lms_id = serializers.CharField(max_length = 15)
    
    class Meta:
       model = BoardStatus
       fields = ('lms_id',)
       
class BoardWriteSerializer(serializers.ModelSerializer):
    mode = serializers.CharField(max_length = 5)
    lms_id = serializers.CharField(max_length = 15)
    title = serializers.CharField(max_length = 25)
    day = serializers.CharField(max_length = 15)
    contents = serializers.CharField(max_length = 500)
    
    class Meta:
       model = BoardWrite
       fields = ('mode', 'lms_id', 'title', 'day', 'contents')

class BoardReadSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 25)
    
    class Meta:
       model = BoardRead
       fields = ('title',)

class CommentsSerializer(serializers.ModelSerializer):
    mode = serializers.CharField(max_length = 5)
    lms_id = serializers.CharField(max_length = 15)
    title = serializers.CharField(max_length = 25)
    comment = serializers.CharField(max_length = 50)    
    
    class Meta:
       model = Comments
       fields = ('mode', 'lms_id', 'title', 'comment')