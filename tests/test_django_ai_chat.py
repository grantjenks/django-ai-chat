import django_ai_chat


def test_version():
    assert tuple(map(int, django_ai_chat.__version__.split('.'))) > (0, 0, 0)


def test_title():
    assert django_ai_chat.__title__ == 'django-ai-chat'
