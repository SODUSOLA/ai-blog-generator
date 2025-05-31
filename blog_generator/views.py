from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

# This function handles user signup

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']
        
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Automatically log in the user after signup
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')  # Redirect to the index page after successful signup
            except Exception as e:
                error_message = f"Error creating account : {str(e)}"
                render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = "Passwords do not match."
            render(request, 'signup.html', {'error_message': error_message})
    else:
        # Render the signup form
        pass
    return render(request, 'signup.html')

def user_logout(request):
    pass



