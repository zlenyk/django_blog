from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404

def index(request):
    all_posts = Post.objects.all().filter(classified=False).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)

def classified(request):
    all_posts = Post.objects.all().filter(classified=True).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)

def post(request,slug,id):
    post = get_object_or_404(Post,pk=id)
    all_posts = Post.objects.all().filter(classified=False).order_by('-publish_date')
    context = {'post': post,'post_list': all_posts}
    return render(request,'blog/post.html',context)
