from django.urls import path

from .views import BoardStatusView, LoginView, ReservationView, StatusView, BoardReadView, BoardWriteView, CommentsView, AdminPasswordView

urlpatterns = [
   path('login/', LoginView.as_view()),
   path('status/', StatusView.as_view()),
   path('rez/', ReservationView.as_view()),
   path('board/status/', BoardStatusView.as_view()),
   path('board/write/', BoardWriteView.as_view()),
   path('board/comments/', CommentsView.as_view()),
   path('board/read/', BoardReadView.as_view()),
   path('admin/passwd/', AdminPasswordView.as_view())
]