from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, MessageForm
from blog.models import PostModel
from django.contrib.auth import logout
from django.contrib import messages 
from.models import Message


# Create your views here.

def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			return redirect('blog-index')

	else:
		form = SignUpForm()


	context = {
		'form':form,
	}
	return render(request, 'users/signUp.html', context)


def logout_view(request):
	logout(request)
	return render(request, 'users/logout.html')



def profile(request):

    posts = PostModel.objects.filter(author = request.user)


    if request.method == 'POST':

        # Load two forms from our forms.py file
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        # If the forms are valid save the following forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # Return to users profile
            return redirect('users-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
        
    context = {
        'posts' : posts,
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

def chatboard(request):
    chats = Message.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            instance =  form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('users-chatboard')
    else:
        form = MessageForm()
    
    context = {
        'chats':chats,
        'form':form,


    }
    return render(request, 'users/chatboard.html', context)

def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    # ----- Delete a record --------

    if request.method == 'POST':
        message.delete()
        return redirect('users-chatboard')


    context = {
        'message':message
    }

    return render(request, 'users/messageDelete.html', context)












