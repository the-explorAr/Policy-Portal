from django.conf.urls import url

from . import views

urlpatterns = [

	 url(r'^$', views.team_register, name='team_register'),
	 url(r'^member$', views.member_register, name='member_register'),
	 url(r'^success_team$', views.success_team, name='success_team'),
	 url(r'^registration_successful$', views.registration_successful, name='registration_successful'),
	 # url(r'^team/create/$', views.TeamCreate.as_view(), name='team_create'),
	 # url(r'^member/create/$', views.MemberCreate.as_view(), name='member_create'),
	 

	 

]