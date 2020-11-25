from django.shortcuts import render , get_object_or_404,redirect
from django.utils import timezone
from .models import Post , Comment
from django.views.generic import (TemplateView , ListView,
                                  DetailView,CreateView, UpdateView,DeleteView)
from django.utils import timezone
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

#class based views involving with listing , creating , updating and deleting a post

class AboutView(TemplateView):
    template_name = 'about.html'

# This class will list all the posts, so we use a listview class
class PostListView(ListView):
    model = Post #we connect to model

    def get_queryset(self): #how we want to bring the list , kind of like a sql query that says grab all posts from database , and order them by published date
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    #decorators : login required
    #mix ins in class based views , automade login requirements
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model= Post
    success_url =reverse_lazy('post_list')




#taking care of unpublished drafts

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    form_class = Post

    def get_queryset(self): #sql query in python
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


############## Now Taking Care of the Comments  ###########################

@login_required
def post_publish(request,pk):
    post= get_object_or_404(Post,pk=pk)
    post.publish()
    return  redirect('post_detail',pk=post.pk)



#using function based views
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)

        else:
            form = CommentForm()
            return render(request, 'blog/comment_form.html',{'form':form})
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
