from django.urls import path


from blog.views.post import BlogPostListView, BlogPostDetailView, BlogPostCreateView,BlogPostUpdateView, BlogPostDeleteView

from blog.views.category import BlogCategoryListView, BlogCategoryDetailView, BlogCategoryCreateView, BlogCategoryUpdateView, BlogCategoryDeleteView

from blog.views.tag import TagListView, TagDetailView, TagCreateView,TagUpdateView, TagDeleteView

from blog.views.comment import CommentListView, CommentDetailView,CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
   
    path("posts/", BlogPostListView.as_view(), name="blogpost-list"),
    path("posts/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost-detail"),
    path("posts/create/", BlogPostCreateView.as_view(), name="blogpost-create"),
    path("posts/update/<int:pk>/", BlogPostUpdateView.as_view(), name="blogpost-update"),
    path("posts/delete/<int:pk>/", BlogPostDeleteView.as_view(), name="blogpost-delete"),

    path("categories/", BlogCategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", BlogCategoryDetailView.as_view(), name="category-detail"),
    path("categories/create/", BlogCategoryCreateView.as_view(), name="category-create"),
    path("categories/update/<int:pk>/", BlogCategoryUpdateView.as_view(), name="category-update"),
    path("categories/delete/<int:pk>/", BlogCategoryDeleteView.as_view(), name="category-delete"),

 
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

    path("comments/", CommentListView.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("comments/create/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/update/<int:pk>/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment-delete"),
]
