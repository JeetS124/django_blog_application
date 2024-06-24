from blog.slug import slugify
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.


class Post(models.Model):
    s_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    post_image = models.ImageField(
        upload_to='upload_images/', default='post_image.jpg')
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, null=False, unique=True)
    timeStamp = models.DateTimeField(blank=True, default=timezone.now())

    def __str__(self):
        return self.title + ' by ' + self.author.first_name + f' ({self.s_no})'

    def save(self, **kwargs):
        slug = '%s' % (self.title)
        self.slug = slugify(self, slug)
        super(Post, self).save()


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
