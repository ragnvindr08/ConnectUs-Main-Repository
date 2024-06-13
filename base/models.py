from django.db import models
from django.contrib.auth.models import User



class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null=True)
    receiver = models.CharField(max_length=100, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def delete_content(self):
        self.content = ''
        self.save() 

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    image = models.ImageField(upload_to='post_images/', default='default_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"
      