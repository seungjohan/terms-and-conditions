# users/urls.py

from django.urls import path
import agree.views

app_name = 'agree'

urlpatterns = [
    path('', agree.views.agree, name = "agree"),
]