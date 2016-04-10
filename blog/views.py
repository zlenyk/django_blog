from django.shortcuts import render
from blog.models import Post
def index(request):
    all_posts = Post.objects.all().filter(classified=False).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)

def classified(request):
    all_posts = Post.objects.all().filter(classified=True).order_by('-publish_date')
    context = {'post_list': all_posts}
    return render(request,'blog/classified.html',context)
