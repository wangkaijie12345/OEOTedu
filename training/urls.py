from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 公司信息详情页__来自小罗
    path('company/', views.company, name='company'),
    # 删除页——艾鹏
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),

]
