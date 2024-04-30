from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from .views import index, BlogList, BlogDetail, CommentList, CommentDetail

urlpatterns = [
    path("", index, name="index"),
    
    # Post
    path("api/posts", BlogList.as_view(), name="blog_list_create"),
    path("api/posts/<int:pk>", BlogDetail.as_view(), name="blog_read_update_delete"),

    
    # Comments
    path("api/posts/<int:pk>/comments", CommentList.as_view(), name="comment_list_create"),

    path("api/posts/<int:pk>/comments/<int:comment_pk>", CommentDetail.as_view(), name="comment_read_update_delete"),
    
    
    # path("", index, name="index"),
    
    
    
]