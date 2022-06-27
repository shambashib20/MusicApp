from django.db import models
import string
import random

# Function for unique codes for the users
def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choice(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
# Important mdodels for the app
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False) # if host can pause the song
    votes_to_skip = models.IntegerField(null=False, default=1)  # number of votes to skip
    created_at = models.DateTimeField(auto_now_add=True)
