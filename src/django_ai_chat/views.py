from hashids import Hashids

from django.conf import settings
from django.shortcuts import redirect, render

from .models import AppVar, Chat, Message, Model


def get_hashids():
    salt = getattr(settings, 'DJANGO_AI_CHAT_HASHIDS_SALT', 'default-salt')
    min_length = getattr(settings, 'DJANGO_AI_CHAT_HASHIDS_MIN_LENGTH', 8)
    hashids = Hashids(salt=salt, min_length=min_length)
    return hashids


def new_chat(request):
    app_var = AppVar.objects.get(key='django-ai-chat/model/default')
    model_title = app_var.value
    model = Model.objects.get(title=model_title)
    chat = Chat(model=model)
    chat.save()
    hashids = get_hashids()
    hashid = hashids.encode(chat.id)
    return redirect('chat', hashid=hashid)


def chat(request, hashid=None):
    hashids = get_hashids()
    chat_id, = hashids.decode(hashid)
    chat, _ = Chat.objects.get_or_create(pk=chat_id)
    messages = chat.message_set.order_by('-update_time')
    return render(
        request,
        'django-ai-chat/index.html',
        {'messages': messages},
    )
