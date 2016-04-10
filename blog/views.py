from django.shortcuts import render
from blog.models import Post
def index(request):
    all_posts = Post.objects.all()
    context = {'post_list': all_posts}
    return render(request,'blog/index.html',context)
