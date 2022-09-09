from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    """
    @author: <hauvo1709@gmail.com>
    @todo: display a default attribute to be displayed
    @param {Object} self
    @return string
    """
    def _str_(self):
        return self.name
