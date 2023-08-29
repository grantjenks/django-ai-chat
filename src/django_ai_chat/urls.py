from django.urls import path

from . import views

urlpatterns = [
    path("", views.new_chat, name='new-chat'),
    path("<hashid>/", views.chat, name='chat'),
]
