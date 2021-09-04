from .views import *
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path("register/",
         AuthorRegistrationView.as_view(), name="authorregistration"),
    path("logout/", AuthorLogoutView.as_view(), name="authorlogout"),
    path("login/", AuthorLoginView.as_view(), name="authorlogin"),
    path("profile/", AuthorProfileView.as_view(), name="authorprofile"),
    path('create_blog/', CreateBlogView.as_view(), name='create_blog'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
