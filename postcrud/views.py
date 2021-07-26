from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from .models import Post, Scrap, Like

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def postshow(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.filter(user=request.user, post=post)
    return render(request, 'postshow.html', {'post':post, 'like':like})
def postnew(request):
    return render(request, 'postnew.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
        else:
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'postnew.html', {'form': form})
    

def scrap(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)

    if not scrapped:
        Scrap.objects.create(user=request.user, post=post)
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    liked = Like.objects.filter(user=request.user, post=post)
    if not liked:
        Like.objects.create(user=request.user, post=post)
    else:
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))