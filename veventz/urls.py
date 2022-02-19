from django.contrib import admin
from django.urls import path, include
from clubmembers import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginuser,name='login'),
    path('home/',views.home,name='home'),
    path('yourevents/',views.yourevents,name='yourevents'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('deleteevent/',views.deleteevent,name='delete'),
    path('searchelement/',views.searchelement,name='searchelement'),
    path('student/', include('nonclubmembers.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
