from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import users
def index(request):
    all_posts = Post.objects.all().filter(classified=False).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)

@login_required
def classified(request):
    all_posts = Post.objects.all().filter(classified=True).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)

def post(request,slug,id):
    post = get_object_or_404(Post,pk=id)
    all_posts = []
    if post.classified == True:
        if request.user.is_authenticated():
            print(request.user)
            all_posts = Post.objects.all().filter(classified=True).order_by('-publish_date')
        else:
            return users.views.login(request)
    else:
        all_posts = Post.objects.all().filter(classified=False).order_by('-publish_date')
    context = {'post': post,'post_list': all_posts}
    return render(request,'blog/post.html',context)
