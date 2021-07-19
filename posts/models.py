from django.conf import settings
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="slug", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def post_count(self):
        return self.post.all().count()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    publishing_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(default="slug", editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2, related_name="post")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
