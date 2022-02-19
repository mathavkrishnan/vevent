from django.urls import include, path
from nonclubmembers import views

urlpatterns = [
    path('',views.studentlogin,name='studentlogin'),
    path('homies/',views.homies,name='homies'),
    path('registered/',views.registered,name='registered'),
    path('searchelement/',views.searchelement,name='searchelement'),
    path('signupuser/',views.signupuser,name='signupuser')
]