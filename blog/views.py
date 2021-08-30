from django.shortcuts import render
from.forms import CommentForm
from django.http import HttpResponseRedirect
from.models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def blog_list (request):
    posts=Post.objects.all()


    context ={
        'posts':posts,
    }
    return render (request,'blog/index.html',context)


def blog_details (request,slug):
    post=Post.objects.get (slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # redirect to a new URL:
            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)
    # if a GET (or any other method) we'll create a blank form
    else:
        comment_form = CommentForm()

    context ={
        'post':post,
        'comments':comments
    }
    return render (request,'blog/details.html',context)