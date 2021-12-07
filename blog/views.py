from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CommentForm


# Create your views here.
class HomeView(ListView):
    template_name = 'blog/home.html'
    queryset = Post.objects.all()
    paginate_by = 2

 #this function is PostView
class PostView(DetailView):
    model = Post
     #This render from template
    template_name = 'blog/post.html'
    #This is Context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()
        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context


     #this is Post function
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
      #get data
        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
     #form validation
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        #return self.render_to_response(context=context)



     #this is Postcreateview function
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image", "tags"]
   #get URL
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blog:home")
    #form validation
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


#this is Postcreateview function
class PostUpdateView (LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image", "tags"]
#get data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context
   #get URL
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blog:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    #this is PostDeleteview function


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
     #get URL
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("blog:home")

#This render from template
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    
