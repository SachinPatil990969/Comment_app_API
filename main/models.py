from django.db import models

class CommentModel(models.Model):
    postId = models.CharField(max_length=100)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    body = models.TextField()

    def __str__(self):
        return self.name
