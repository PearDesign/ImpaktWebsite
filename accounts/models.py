from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "Team Impakt"
