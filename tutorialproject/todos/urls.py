from django.urls import path
from . import views

# this list contains our paths
urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world' ),
    path('', views.hello_python_view, name='hello_python'),
    path('htmlrender', views.hello_html_view, name='hello_html'),
    # path('helloname/<name>') or we can force a datatype also
    path('helloname/<str:name>', views.hello_path, name='hello_path'),
    path('helloquery', views.hello_query, name='hello_query'),
    # path('add/<int:num1>/<int:num2>) -> we can add multiple parameters
    path('special', views.special_view, name='special'),
    path('postendpoint', views.post_example, name='post_example'),
    path('submitendpoint', views.submit_example, name='submit_example'),
    path('postdjangoform', views.post_django_form, name='post_django_form'),
    path('submitdjango', views.submit_django_form, name='submit_django')

]