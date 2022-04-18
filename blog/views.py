from django.shortcuts import render, redirect
from .models import PostModel, Comment
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
	posts = PostModel.objects.all()

	# --------IMPORTANT LOGIC FOR CREATING RECORDS-----------
	if request.method == 'POST':

		# If request is a 'POST' request, invoke our 'PostModelForm'
		# from forms.py
		form = PostModelForm(request.POST)

		# Check if the data is 'valid'
		if form.is_valid():

			# Every post made must have the name of an author, 
			# commit=False because we don't save it yet 
			instance = form.save(commit=False) 
			instance.author = request.user


			# Save our form
			instance.save()


			return redirect('blog-index')
			

	else:
		form = PostModelForm()



	context = {
		'posts':posts,
		'form':form
	}
	return render(request, 'blog/index.html', context)


# -------------Use this type of method when a certain record is needed-----------  
# -------------------ASSIGN PRIMARY KEY---------------------
def postDetail(request, pk):
	post = PostModel.objects.get(id=pk)

	if request.method == 'POST':
		c_form = CommentForm(request.POST)

		if c_form.is_valid():

			# don't save yet
			instance = c_form.save(commit=False)

			# get the author
			instance.user = request.user
			instance.post = post
			instance.save()

			return redirect('blog-post-detail', pk=post.id)


	else:
		c_form = CommentForm()

	context = {
		'post':post,
		'c_form': c_form

	}



	return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


def post_delete(request, pk):
	post = PostModel.objects.get(id=pk)

	# ---------------DELETE A RECORD--------------------

	if request.method == 'POST':
		post.delete()
		return redirect('blog-index')


	context = {
		'post':post
	}

	return render(request, 'blog/post_delete.html', context)

