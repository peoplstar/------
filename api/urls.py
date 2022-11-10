from django.urls import path

from .views import BoardStatusView, LoginView, ReservationView, StatusView

urlpatterns = [
   path('login/', LoginView.as_view()),
   path('status/', StatusView.as_view()),
   path('rez/', ReservationView.as_view()),
   path('board/status', BoardStatusView.as_view()),
]