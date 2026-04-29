from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    players = models.CharField(max_length=100)
    rules = models.TextField()
    image = models.ImageField(upload_to='games/', blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='games')

    def __str__(self):
        return self.title


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)