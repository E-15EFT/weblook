from django.db import models
from django.urls import reverse

# Create your models here.


class UploadMovie(models.Model):
    title = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to="thumbnail", null=True, blank=True)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, max_length=300)
    movie = models.FileField(upload_to="movies", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def get_absolute_url(self):
        return reverse("read-more", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
