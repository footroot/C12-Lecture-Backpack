from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog

# Create your views here.
@login_required(login_url='/auth/login/')
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect('view_blog', blog_id=blog_post.pk)
        else:
            return HttpResponse("<h1>Post not added!</h1>")
    form = BlogForm()
    return render(request, 'create_blog.html', {'form':form})

def view_blog(request, blog_id):
    try:
        blog_post = Blog.objects.get(pk=blog_id)
        context = {
            'title': blog_post.title,
            'author': blog_post.author,
            'body': blog_post.body
        }
        return render(request, 'view_blog.html', context=context)
    except Exception as e:
        return HttpResponse(f"{e}")
  
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

@login_required
def delete_blog(request, blog_id):
    user = request.user
    if user.has_perm('Blog_App.delete_post'):
        blog_post = Blog.objects.get(pk=blog_id)
        blog_post.delete()
    return redirect('home')
