from django.db import models

# Create your models here.


# Create your models here.
class ChatMessage(models.Model):
    ROLES = (
        ('user', 'User'),
        ('bot', 'Bot'),
    )

    role = models.CharField(max_length=5, choices=ROLES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} - {self.timestamp}"

class CallBackRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    exported = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
class Team(models.Model):
    image=models.ImageField(upload_to='Team')
    name=models.TextField(max_length=100)
    post=models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.name
    