from django.urls.conf import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('logout' , views.logout , name="logout"),

    path('', csrf_exempt(views.login), name="login")

]