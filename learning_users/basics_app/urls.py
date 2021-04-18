from django.conf.urls import url
from basics_app import views

app_name = 'basics_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^userlogin/$',views.user_login,name='user_login'),
]
