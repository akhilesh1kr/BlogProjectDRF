from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('publish', 'created', )

    def __str__(self):
        return self.title