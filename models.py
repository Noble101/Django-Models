from django.db import models

# Create your models here.
Title = models.CharField("A Model on Django under the application blog")
Text = models.TextField("I love this web development training by Ingressive for good and the Zuri team. God bless you all")
Author = get_user_model()
Created_date : models.DateTimeField(auto_now_add=True)
Published_date : models.DateTimeField(auto_now_add=True)