from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def index(request):
    return render(request, 'index.html')

# This function handles user login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
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
    logout(request)
    return redirect('index')  # Redirect to the index page after logout

def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.load(request.body)
            yt_link = data['youtube_link']
        except:
            return JsonResponse({'error': 'Invalid data sent.'}, status=405)
        
        # get yt_link from the request body
        
        # get transcript from the youtube link
        
        # Use OpenAI API to generate a blog post based on the transcript
        
        # Save the generated blog post to the database
        
        # Return the generated blog post as a JSON response
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400) 