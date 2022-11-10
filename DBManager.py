import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase():
    def __init__(self):
        # Firebase database 인증 및 앱 초기화
        if not firebase_admin._apps:
            cred = credentials.Certificate("/home/ubuntu/server/gwnu-reservation-496bf-firebase-adminsdk-w90ca-6fc6c9370a.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://gwnu-reservation-496bf-default-rtdb.asia-southeast1.firebasedatabase.app/'
            })
        
        self.user = db.reference().child('user')
        self.admin = db.reference().child('admin')

    # 예약 추가, user - place - day - student_id - time 으로 저장
    def add_user_reservation(self, place, day, student_id, start_time, end_time, appd):
        self.user.child(place).child(day).child(student_id).update(
            {"start_time": start_time, "end_time" : end_time, "appd" : appd}
        )

    # 예약 현황
    def status_user_reservation(self, day, place):
        time = []
        local_place = self.user.child(place).child(day)
        c = local_place.get()
        
        for i in c:
            db_time = local_place.child(i).get()
            time.append({'start_time' : db_time['start_time'], 'end_time' : db_time['end_time']})        
    
        return time
    
    # 예약 삭제
    def delete_user_reservation(self, place, day, student_id):
        self.user.child(place).child(day).child(student_id).delete()


    # admin 계정 설정, admin_id가 키 값, admin - admin_id - password 로 저장
    def set_admin(self, admin_pwd):
        self.admin.update({"password": admin_pwd})


    # admin 계정에 예약 log 추가, admin - log - place - day - student_id - time 으로 저장
    def add_admin_reservation_log(self, place, day, student_id, time):
        self.admin.child('log').child(place).child(day).child(student_id).update({"time": time})


    # admin 계정의 예약 log 삭제
    def delete_admin_reservation_log(self, place, day, student_id):
        self.admin.child('log').child(place).child(day).child(student_id).child("time").delete()


    # 예약, 예약 로그 추가
    def add_reservation(self, place, day, student_id, time):
        self.add_admin_reservation_log(self, place, day, student_id, time)
        self.add_user_reservation(self, place, day, student_id, time)


    # 예약, 예약 로그 삭제
    def delete_reservation(self, place, day, student_id):
        self.delete_admin_reservation_log(self, place, day, student_id)
        self.delete_user_reservation(self, place, day, student_id)


    # 게시글 추가, 게시글 키 값은 고유 키로 부여
    def write_post(self, title, contents, student_id):
        information = {
            "title": title,
            "contents": contents,
            "user_id": student_id
        }
        self.ref.child('post').push().update(information)


    # 게시글 목록 읽기, post_list[0].title => 0번 게시글 타이틀
    def read_post(self):
        post_list = self.ref.child('post').get().val()
        return post_list

# if __name__ == '__main__':
#     fb = Firebase()
#     # fb.add_user_reservation('gym', '2022-10-23', '20220202', '11-00', '13-00', '0')
#     fb.status_user_reservation('gym', '2022-10-23')
#     # fb.delete_user_reservation('gym', '2022-10-23', '20171473')