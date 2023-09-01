Django AI Chat
==============

`Django AI Chat <http://www.grantjenks.com/docs/django-ai-chat/>`__ is an
Apache2 licensed Django application for AI chat.


Features
--------

- Tested on Python 3.7, 3.8, 3.9, 3.10, 3.11
- Tested on Django 3.2 LTS and Django 4.2 LTS
- Tested on Linux, Mac, and Windows

.. image:: https://github.com/grantjenks/django-ai-chat/workflows/integration/badge.svg
   :target: https://github.com/grantjenks/django-ai-chat/actions?query=workflow%3Aintegration

.. image:: https://github.com/grantjenks/django-ai-chat/workflows/release/badge.svg
   :target: https://github.com/grantjenks/django-ai-chat/actions?query=workflow%3Arelease


Quickstart
----------

Installing Django AI Chat is simple with `pip
<http://www.pip-installer.org/>`_::

    $ pip install django-ai-chat

Add `django_ai_chat` to the installed apps in `settings.py` like:

.. code::

   INSTALLED_APPS += ['django_ai_chat']

And add `django_ai_chat.urls` to the urlpatterns in `urls.py` like:

.. code::

   urlpatterns += [
       path('ai-chat/', include('django_ai_chat.urls')),
   ]

Then run:

.. code::

   $ python manage.py migrate


Reference and Indices
---------------------

* `Django AI Chat Documentation`_
* `Django AI Chat at PyPI`_
* `Django AI Chat at GitHub`_
* `Django AI Chat Issue Tracker`_

.. _`Django AI Chat Documentation`: http://www.grantjenks.com/docs/django-ai-chat/
.. _`Django AI Chat at PyPI`: https://pypi.python.org/pypi/django-ai-chat/
.. _`Django AI Chat at GitHub`: https://github.com/grantjenks/django-ai-chat
.. _`Django AI Chat Issue Tracker`: https://github.com/grantjenks/django-ai-chat/issues


Django AI Chat License
----------------------

Copyright 2023 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
