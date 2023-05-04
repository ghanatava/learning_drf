from django.urls import path
from . import views


urlpatterns=[
    path('',views.endpoints,name='endpoints'),
    path('advocate_list',views.advocates,name='advocates'),
    path('advocate/<str:username>/',views.advocate_detail,name='advocate_detail'),
]