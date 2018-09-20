from django.urls import path
from . import views
urlpatterns=[
	path('',views.main_view,name='main_view'),
	path('result/',views.result),				#when request comes for 'result/' execute 'result' function from 'views.py'
]