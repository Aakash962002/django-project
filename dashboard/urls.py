from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.IndexView,name="index_view"),
    path('login/',views.Login,name="login_page"),
    path('sign_up/',views.SignUp,name="sign_up"),
    path('logout/',views.LogoutFunc,name="logout"),
    path('crud_opr/list/', views.CrudOprListView, name='crud_opr_list'),
    path('crud_opr/create/', views.CrudOprCreateView, name='crud_opr_create'),
    path('crud_opr/detail/<int:pk>/', views.CrudOprDetailView, name='crud_opr_detail'),
    path('crud_opr/update/<int:pk>/', views.CrudOprUpdateView, name='crud_opr_update'),
    path('crud_opr/delete/<int:pk>/', views.CrudOprDeleteView, name='crud_opr_delete'),
]
