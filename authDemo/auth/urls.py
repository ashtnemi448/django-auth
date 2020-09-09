from django.conf.urls import url, include
from . import views

app_name = 'auth'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^nopermission/', views.nopermission, name='nopermission'),
    url(r'^dash/', views.dash, name='dash'),
    url(r'^blog/', views.bloger, name='blog'),
    url(r'^blogwriter/', views.blogwriter, name='blogwriter'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register/', views.register_user, name='register'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^username/', views.nm, name='nm')
]