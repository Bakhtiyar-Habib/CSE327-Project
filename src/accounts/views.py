from django.shortcuts import render, redirect #IMPORT redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #2nd one is for logging in
from django.contrib.auth import login, logout # for loggin in users and logging them out
# Create your views here.

def signup_view(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() #saves data to the database and creates new user
			return redirect('http://127.0.0.1:8000/home/')

	else: #if GET request
		form = UserCreationForm() #show a fresh form

	return render(request, "accounts/signup.html", {'form': form})


def login_view(request):
	if request.method == 'POST':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			#login the user
			user = login_form.get_user()
			login(request, user) # user is the variable from previous line
			return redirect('http://127.0.0.1:8000/home/')
	else:
		login_form = AuthenticationForm()
		
	return render(request, "accounts/login.html", {'login_form':login_form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('http://127.0.0.1:8000/home/')