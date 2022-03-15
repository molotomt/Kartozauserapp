from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from PIL import Image

class Userdetails(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    home_address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)
    location = models.PointField()
    

    def __str__(self):
        return self.user.username

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

  # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image