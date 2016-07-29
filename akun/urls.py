from django.conf.urls import url
from django.contrib.auth import views
from . import views as views_akun
from .forms import LoginForm


urlpatterns  = [
	# login dan logout user
	url('^login/$', views.login, {
			'authentication_form': LoginForm, 
		}, name='login', ),
	url('^logout/$', views.logout, name='logout'),
	url('^logout-then-login/$', views.logout_then_login, name='logout_then_login'),
	url(r'^$', views_akun.dashboard, name='dashboard'),
]
