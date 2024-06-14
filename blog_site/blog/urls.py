from django.urls import path, re_path
import blog.views as blog_view
import users.views as users_view
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path("about/", blog_view.blog_about, name="about"),
    path("new_post", blog_view.new_post, name="new_post"),
    path("update/<int:s_no>", blog_view.edit_post, name="update"),
    path("delete/<int:s_no>", blog_view.delete_post, name="delete"),
    path("allposts/", blog_view.allpost_view, name="view_more"),
    # re_path(r'^blog/(?P<slug>[0-9]+)/$',blog_view.post_update,name='post_update'),
    # path('post_update', blog_view.post_update, name='post_update'),
    path("blog/<str:slug>", blog_view.post_detail, name="post_detail"),
    path("blog/<str:slug>/comment", blog_view.post_comment, name="post_comment"),
    path("edit_profile/<int:id>", users_view.edit_profile, name="edit_profile"),
]
if True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
