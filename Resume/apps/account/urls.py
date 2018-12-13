from django.urls import path,re_path
from .views import *


urlpatterns = [
    re_path('^login$', LoginView.as_view(), name="login"),
]

