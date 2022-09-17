from django.db import models
from django.contrib.auth.models import User

# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)

#     """
#     @author: <hauvo1709@gmail.com>
#     @todo: display a default attribute to be displayed
#     @param {Object} self
#     @return string
#     """
#     def _str_(self):
#         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    """
    @author: <hauvo1709@gmail.com>
    @todo: display a default attribute to be displayed
    @param {Object} self
    @return string 
    """
    def _str_(self):
        return f'{self.user.username} Profile'


