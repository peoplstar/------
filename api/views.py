import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import DBManager
import login

from .serializers import (BoardStatusSerializer, LoginSerializer,
                          ReservationSerializer, StatusSerializer, BoardWriteSerializer)

err_msg = "입력하신 아이디 혹은 비밀번호가 일치하지 않습니다."
suc_msg = "로그인이 되었습니다."

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            userid = tmp['lms_id']
            password = tmp['lms_pw']

            if userid == 'gwnu_admin':
                # DB에서 해당 패스워드 비교 이후 admin account msg return
                pass
            else:
                module = login.loginModule(userid, password)
                msg = module.login()
            
                if msg == '1':
                    return Response(suc_msg, status = status.HTTP_200_OK)
                else :
                    return Response(err_msg, status = status.HTTP_200_OK)
            
class StatusView(APIView):
    def post(self, request):
        serializer = StatusSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            day = tmp['day']
            place = tmp['place']


            db_connect = DBManager.Firebase()
            status_time = db_connect.status_user_reservation(day, place)
            
            return Response(status_time, status = status.HTTP_200_OK)
            # DB에서 place, day 기반 사용중인 시간대 전송
            
class ReservationView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            lms_id = tmp['lms_id']
            day = tmp['day']
            place = tmp['place']
            start_time = tmp['start_time']
            end_time = tmp['end_time']
            appd = tmp['appd'] # 승인 여부
            db_connect = DBManager.Firebase
            db_connect.add_user_reservation(place, day, lms_id, start_time, end_time, appd)
            
            return Response("Reservation Success", status = status.HTTP_200_OK)
            # 해당 내용을 DB에 전송 이후 관리자에게 FCM
            
            
class BoardStatusView(APIView):
    def post(self, request):
        serializer = BoardStatusSerializer(data = request.data)
        if serializer.is_valid():
            res_data = []
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            idx = tmp['idx']
            title = tmp['title']
            day = tmp['day']
            
        pass
    
class BoardWriteView(APIView):
    def post(self, request):
        serializer = BoardWriteSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            idx = tmp['idx']
            title = tmp['title']
            day = tmp['day']
            contents = tmp['contents']
        pass
    