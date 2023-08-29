import openai

from hashids import Hashids

from django.conf import settings
from django.shortcuts import redirect, render

from .models import AppVar, Chat, Message, Model

openai.api_key = getattr(settings, 'DJANGO_AI_CHAT_OPENAI_API_KEY')


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

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'user':
            content = request.POST.get('message', '')
            message = Message(chat=chat, role='user', content=content)
            message.save()

        if action == 'assistant':
            system_prompt = chat.model.system_prompt
            chat_messages = [{'role': 'system', 'content': system_prompt}]
            chat_messages.extend(
                {'role': message.role, 'content': message.content}
                for message in chat.message_set.order_by('update_time')
            )
            response = openai.ChatCompletion.create(
                model=chat.model.name,
                messages=chat_messages,
                temperature=chat.model.temperature,
            )
            content = response['choices'][0]['message']['content']
            message = Message(chat=chat, role='assistant', content=content)
            message.save()

    return render(
        request,
        'django-ai-chat/index.html',
        {'messages': chat.message_set.order_by('-update_time')},
    )
