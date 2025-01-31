from django.db import models

# Create your models here.



class Branch(models.Model):
    location_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/branch_image', null=True, blank=True)
    video = models.FileField(upload_to='media/videos/branch_video', null=True, blank=True)
    description = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_name


class Category_FastFood(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FastFood(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(Category_FastFood, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/food_image', null=True, blank=True)
    video = models.FileField(upload_to='media/videos/food_video', null=True, blank=True)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
