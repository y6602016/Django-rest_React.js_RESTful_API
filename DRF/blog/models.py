from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Postobjects is a model manager, it helps the home page only displays
    # the post which has status 'published'
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    # every post belongs a category, so Post has an atrribution that is category
    # category use ForeignKey pointing to Category class
    # once we delete a category, we also detele the all associated posts
    # so on_delete.PROTECR avoids it happening
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        # on_delete=models.CASCADE means once we delete a User
        # all associated posts are deleted as well
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects() #custom manager

    # class Meta:
    #     ordering = ('-published',)

    def __str__(self):
        return self.title
