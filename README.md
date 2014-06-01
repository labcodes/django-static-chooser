django-static-chooser
=====================

Simply choose between your local static file or a remote CDN.


Usage
-----

```html

{% load staticfileschooser %}
<link rel="stylesheet" type="text/css" href="{% static 'local' http://remote.url %}">

```
