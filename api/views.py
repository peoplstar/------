import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import DBManager
import login

from .serializers import (BoardStatusSerializer, LoginSerializer,
                          ReservationSerializer, StatusSerializer, 
                          BoardWriteSerializer, CommentsSerializer,
                          BoardReadSerializer, AdminPasswordSerializer,
                          CheckLogSerializer, ApproveRezSerializer)

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
                db_connect = DBManager.Firebase()
                msg = db_connect.password_check_admin(password)

                if msg == '1':
                    return Response(suc_msg, status = status.HTTP_200_OK)
                else :
                    return Response(err_msg, status = status.HTTP_200_OK)
                
            else:
                module = login.loginModule(userid, password)
                msg = module.login()
            
                if msg == '1':
                    return Response(suc_msg, status = status.HTTP_200_OK)
                else :
                    return Response(err_msg, status = status.HTTP_200_OK)

class AdminPasswordView(APIView):
    def post(self, request):
        serializer = AdminPasswordSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            password = tmp['password']
            db_connect = DBManager.Firebase()
            db_connect.set_admin(password)
            msg = '비밀번호가 변경되었습니다.'

            return Response(msg, status = status.HTTP_200_OK)
            
            
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
            
# check
class ReservationView(APIView):
      def post(self, request):
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            mode = tmp['mode']
            lms_id = tmp['lms_id']
            day = tmp['day']
            place = tmp['place']
            start_time = tmp['start_time']
            end_time = tmp['end_time']
            appd = tmp['appd'] # 승인 여부

            db_connect = DBManager.Firebase()
            if mode == 'rez':
                db_connect.add_reservation(place, day, lms_id, start_time, end_time, appd)
            elif mode == 'del':
                db_connect.delete_reservation(place, day, lms_id)
            
            return Response("Success", status = status.HTTP_200_OK)
            # 해당 내용을 DB에 전송 이후 관리자에게 FCM
            
            
class BoardReadView(APIView):
    def post(self, request):
        serializer = BoardReadSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            title = tmp['title']
            
            db_connect = DBManager.Firebase()
            read = db_connect.read_board(title)
            
            return Response(read, status = status.HTTP_200_OK)

class BoardStatusView(APIView):
    def post(self, request):
        serializer = BoardStatusSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)

            db_connect = DBManager.Firebase()
            lst = db_connect.post_list()

            return Response(lst, status = status.HTTP_200_OK)

class BoardWriteView(APIView):
    def post(self, request):
        serializer = BoardWriteSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            comment = 'null'
            mode = tmp['mode']
            title = tmp['title']
            day = tmp['day']
            contents = tmp['contents']
            lms_id = tmp['lms_id']
            db_connect = DBManager.Firebase()

            if mode == 'write':
                db_connect.write_post(lms_id, title, contents, day)
                return Response("Success", status = status.HTTP_200_OK)

            elif mode == 'del':
                msg = db_connect.del_post(lms_id, title)
                return Response(msg, status = status.HTTP_200_OK)
    
class CommentsView(APIView):
    def post(self, request):
        serializer = CommentsSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            mode = tmp['mode']
            lms_id = tmp['lms_id']
            title = tmp['title']
            comment = tmp['comment']
            db_connect = DBManager.Firebase()

            if mode == 'ins':
                db_connect.write_comment(lms_id, title, comment)
            elif mode == 'del':
                db_connect.delete_comment(lms_id, title, comment) 

            return Response("Success", status = status.HTTP_200_OK)

class ApproveRezView(APIView):
    def post(self, request):
        serializer = ApproveRezSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)
            lms_id = tmp['lms_id']
            day = tmp['day']
            appd = tmp['appd']
            place = tmp['place']
            db_connect = DBManager.Firebase()
            
            if appd == '2':
                db_connect.approve_rez(place, lms_id, day, appd)
                return Response("승인 허가", status = status.HTTP_200_OK)
            elif appd == '3':
                db_connect.delete_reservation(place, day, lms_id)
                return Response("승인 거부", status = status.HTTP_200_OK)

class CheckLogView(APIView):
    def post(self, request):
        serializer = CheckLogSerializer(data = request.data)
        if serializer.is_valid():
            inform = request.data
            dump = json.dumps(inform)
            tmp = json.loads(dump)

            db_connect = DBManager.Firebase()
            log = db_connect.check_log_admin()
            return Response(log, status = status.HTTP_200_OK)

