from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Results(models.Model):
    comment_text = models.TextField()
    toxic = models.BooleanField()
    severe_toxic = models.BooleanField()
    obscene = models.BooleanField()
    threat = models.BooleanField()
    insult = models.BooleanField()
    identity_hate = models.BooleanField()

    def __str__(self) -> str:
        return (
            f"{self.comment_text[:50]}..."
            if len(self.comment_text) > 50
            else self.comment_text
        )

class UserStudiesCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"User {self.user} has done {self.count} studies"
