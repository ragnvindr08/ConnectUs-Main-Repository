from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404 , redirect 
from django.http import HttpRequest, HttpResponse
from django.contrib import messages  # For flash messages
from .models import Message
from .forms import PostForm
from .models import Post


@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/signup.html", {"form": form, "success": True})
        else:
            return render(request, "registration/signup.html", {"form": form, "error": True})
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
  
def send_message(request):
    if request.method == 'POST':
        # Process the form submission
        # Assuming you have a form for sending messages
        pass
    else:
        # Render the form for sending messages
        return render(request, 'send_message.html')
def send_message(request):
    # Your logic for sending messages goes here
    return render(request, 'send_message.html')

def community(request):
    return render(request, 'community.html')

def developer(request):
    return render(request, 'developer.html')    

@login_required
def messages_view(request):
    if request.method == 'POST':
        if 'delete_message' in request.POST:
            message_id = request.POST.get('message_id')
            try:
                message_to_delete = Message.objects.get(id=message_id, receiver=request.user)
                message_to_delete.delete()
                messages.success(request, 'Message deleted successfully!')
            except Message.DoesNotExist:
                messages.error(request, 'Message does not exist or you do not have permission to delete it.')
        else:
            receiver_username = request.POST.get('receiver')
            content = request.POST.get('content')

            try:
                receiver = User.objects.get(username=receiver_username) 
                message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
                messages.success(request, 'Message sent successfully!')
            except User.DoesNotExist:
                messages.error(request, 'Invalid username. Please enter a valid user.')
            except Exception as e:
                messages.error(request, f'Error sending message: {e}')

    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messages.html', {'received_messages': received_messages})
    
def messages_home(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        content = request.POST.get('content')

        try:
            receiver = User.objects.get(username=receiver_username) 
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, 'Message sent successfully!')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except User.DoesNotExist:
            messages.error(request, 'Invalid username. Please enter a valid user.')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern 
    else:
        received_messages = Message.objects.filter(receiver=request.user)
        return render(request, 'homemessage.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern

@login_required
def create_post(request):
    if request.method == 'POST':
        # Handle form submission (create post)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user  # Set the user before saving
            new_post.save()
            form = PostForm()  # Clear the form after successful submission
    else:
        # Handle GET request (display form and user posts)
        form = PostForm()

    # Handle POST request to delete a post
    if request.method == 'POST' and 'post_id' in request.POST:
        post_id = request.POST.get('post_id')
        post_to_delete = get_object_or_404(Post, id=post_id)
        if post_to_delete.user == request.user:
            post_to_delete.delete()
            return redirect('/create_post/')  # Redirect to the same page after deletion
        else:
            # Handle the case where user tries to delete someone else's post
            return HttpResponseForbidden("You don't have permission to delete this post.")

    # Retrieve all posts created by the logged-in user
    user_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'post_form.html', {'form': form, 'user_posts': user_posts})

def user_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)

    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'user_posts.html', context)

def timeline(request):
    # Get all posts ordered by created_at descending
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

def timelinehome(request):
    # Get all posts ordered by created_at descending
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts1.html', context)     


