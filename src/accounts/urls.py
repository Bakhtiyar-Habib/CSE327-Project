from django.confs.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
	path('signup/', signup_view, name='signup'),

]