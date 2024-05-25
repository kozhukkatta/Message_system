from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    #path('student_login',views.student_login,name='student_login'),
    path('loginaction',views.loginaction,name='loginaction'),
    path('index',views.index,name='index'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('mark/userhome',views.userhome,name='userhome'),
    path('adcom',views.adcom,name='adcom'),
    path('deletemsg/<int:mid>',views.deletemsg,name='deletemsg'),
    #path('validate',views.validate,name='validate'),
    # path('approveuser/<str:username>',views.approveuser,name='approveuser'),
    path('rejectuser/<str:username>',views.rejectuser,name='rejectuser'),
    path('editusers',views.editusers,name='editusers'),
    path('editlogin/<str:username>', views.editlogin),
    path('updatelogin/<str:username>', views.updatelogin),
    path('deletelogin/<str:username>',views.deletelogin,name='deletelogin'),
    path('brdmsg',views.brdmsg,name='brdmsg'),
    path('broad',views.broad,name='broad'),
    path('unimsg',views.unimsg,name='unimsg'),
    path('unicast',views.unicast,name='unicast'),
    path('encryptmsg',views.encryptmsg,name='encryptmsg'),
    path('encryptms',views.encryptms,name='encryptms'),
    path('decryptmsg/<int:mid>',views.decryptmsg,name='decryptmsg'),
    path('messg',views.messg,name='messg'),
    path('viewmesg',views.viewmesg,name='viewmesg'),
    path('sendmesg',views.sendmesg,name='sendmesg'),
    path('cmmesg',views.cmmesg,name='cmmesg'),
    path('pernmesg',views.pernmesg,name='pernmesg'),
    path('prof',views.prof,name='prof'),
    path('editp/<str:username>',views.editp,name='editp'),
    path('updatelog/<str:username>',views.updatelog,name='updatelog'),
    # path('mark/<int:mid>',views.mark,name='mark'),
    path('logout',views.logout, name='logout'),
    
]
