from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns=[
    path('',views.endpoints,name='endpoints'),
    path('advocates/',views.AdvocateList.as_view(),name='advocates'),
    path('advocate/<str:username>/', views.advocate_detail, name='advocate_detail'),
    path('company/', views.company, name='company'),
    #api token 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
