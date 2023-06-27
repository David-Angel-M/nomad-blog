from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post, Comment, Category
from django.contrib import messages
from .mixins import SuccessMessageMixin


class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')

    def form_valid(self, form):
        # Add success message
        messages.success(self.request, "Login successful.")

        return super().form_valid(form)


class Register(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

            # Add success message
            messages.success(self.request, "Registration successful. You are now logged in.")

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super().get(*args, **kwargs)


class PostListProvider(LoginRequiredMixin, ListView):
    model = Post
    fields = '__all__'
    template_name = 'base/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'category', 'image']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
       # Add success message
        messages.success(self.request, "Post created successfully.")

        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'category', 'image']
    success_url = reverse_lazy('posts')
    success_message = "Post updated successfully"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class PostList(ListView):
    model = Post
    fields = '__all__'
    template_name = 'base/post_list.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    fields = '__all__'
    template_name = 'base/post_detail.html'
    context_object_name = 'post'

