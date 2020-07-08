from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}   ||  {self.title}'