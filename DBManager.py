import firebase_admin
import json

from firebase_admin import credentials
from firebase_admin import db

class Firebase():
    def __init__(self):
        # Firebase database 인증 및 앱 초기화
        if not firebase_admin._apps:
            cred = credentials.Certificate("gwnu-reservation-496bf-firebase-adminsdk-w90ca-6fc6c9370a.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://gwnu-reservation-496bf-default-rtdb.asia-southeast1.firebasedatabase.app/'
            })
        
        self.user = db.reference().child('user')
        self.admin = db.reference().child('admin')

    # 예약 추가, user - place - day - student_id - time 으로 저장 check
    def add_user_reservation(self, place, day, lms_id, start_time, end_time, appd):
        self.user.child(place).child(day).child(lms_id).update(
            {"start_time": start_time, "end_time" : end_time, "appd" : appd}
        )

    # 날짜 별 예약 현황 check
    def status_user_reservation(self, place, day):
        time = []
        local_place = self.user.child(place).child(day)
        
        c = local_place.get()
        
        for i in c:
            db_time = local_place.child(i).get()
            time.append({'start_time' : db_time['start_time'], 'end_time' : db_time['end_time']})        
    
        print(time)
        return time
    
    # 예약 삭제 check
    def delete_user_reservation(self, place, day, lms_id):
        self.user.child(place).child(day).child(lms_id).delete()

    # 

    # 해당 게시물 타이틀 클릭 시 모든 내용 전송 check 
    def read_board(self, title):
        read = self.user.child('post').child(title).get()
        return read

    # 게시글 추가, 게시글 키 값은 고유 키로 부여 check
    def write_post(self, student_id, title, contents, day):
        information = {
            "student_id": student_id,
            "contents": contents,
            "day": day,
            "comment": 'null'
        }
        self.user.child('post').child(title).update(information)

    # check
    def write_comment(self, student_id, title, comments):
        information = {
            student_id : comments
        }

        try:
            if self.user.child('post').child(title).child('comment').get() == 'null':
                idx = 0
                self.user.child('post').child(title).child('comment').child(str(idx)).update(information)
            else:
                idx = len(self.user.child('post').child(title).child('comment').get())
                self.user.child('post').child(title).child('comment').child(str(idx)).update(information)

        except TypeError:
            except_code = {
                "comment": 'null'
            }
            self.user.child('post').child(title).update(except_code)
            self.user.child('post').child(title).child('comment').child('0').update(information)

    # check
    def delete_comment(self, student_id, title, comments):
        ref = self.user.child('post').child(title).child('comment').get()

        try:
            for j, i in enumerate(ref):
                try:
                    if i[str(student_id)] == str(comments):
                        self.user.child('post').child(title).child('comment').child(str(j)).child(student_id).delete()
                except (KeyError, TypeError):
                    pass

        except (KeyError, TypeError):
            pass

    # check
    def post_list(self):
        lst = []
        post_ref = self.user.child('post')
        
        c = post_ref.get(False, True)

        for i in c:
            lst.append(i)

        print(lst)
        return lst

    
    # admin 계정 설정, admin_id가 키 값, admin - admin_id - password 로 저장
    def set_admin(self, admin_pwd):
        self.admin.update({"password": admin_pwd})

    # check
    def password_check_admin(self, password):
        db_passwd = self.admin.child('password').get()
        
        if str(db_passwd) == password:
            return '1'
        else:
            return '-1'

    # check
    # admin 계정에 예약 log 추가, admin - log - place - day - student_id - time 으로 저장
    def add_admin_reservation_log(self, place, day, student_id, start_time, end_time):
        self.admin.child('log').child(place).child(day).child(student_id).update(
            {"start_time": start_time, "end_time" : end_time}
        )


    # admin 계정의 예약 log 삭제 check
    def delete_admin_reservation_log(self, place, day, student_id):
        self.admin.child('log').child(place).child(day).child(student_id).delete()


    # 예약, 예약 로그 추가 check
    def add_reservation(self, place, day, student_id, start_time, end_time, appd):
        #place, day, lms_id, start_time, end_time, appd)
        self.add_admin_reservation_log(place, day, student_id, start_time, end_time)
        self.add_user_reservation(place, day, student_id, start_time, end_time, appd)

    # 예약, 예약 로그 삭제 check
    def delete_reservation(self, place, day, student_id):
        self.delete_admin_reservation_log(place, day, student_id)
        self.delete_user_reservation(place, day, student_id)

if __name__ == '__main__':
    fb = Firebase()
    
    # fb.delete_comment('20222004', '하 시발 좆같다4', 'ㅇㅈㅇㅈ')
    # fb.write_comment('20222001', '하 시발 좆같다', 'ㅇㅈㅇㅈ')
    # fb.add_reservation('gym', '2022-12-15', '20220202', '13-00', '15-00', '0')
    # fb.status_user_reservation('gym', '2022-12-15')
    fb.delete_reservation('gym', '2022-12-15', '20220202')
    # fb.delete_user_reservation('gym', '2022-10-23', '20171473')