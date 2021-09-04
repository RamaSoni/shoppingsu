from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from blogs.forms import AuthorForm, AuthorLoginForm, BlogForm
from django.views import generic
from django.views.generic import CreateView
from .models import Author, Post
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreateBlogView(CreateView):
    template_name = "create_blog.html"
    form_class = BlogForm
    success_url = reverse_lazy("home")


class AuthorRegistrationView(CreateView):
    template_name = "authorregistration.html"
    form_class = AuthorForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class AuthorLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")


class AuthorLoginView(FormView):
    template_name = "authorlogin.html"
    form_class = AuthorLoginForm
    success_url = reverse_lazy("home")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Author.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class AuthorProfileView(TemplateView):
    template_name = "authorprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Author.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    
