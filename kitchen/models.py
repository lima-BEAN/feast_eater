from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eater(models.Model):
    # first name, last name, email, password are all inheritied from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    question_1 = models.CharField(max_length=200, null=False)
    answer_1 = models.CharField(max_length=200, null=False)
    question_2 = models.CharField(max_length=200, null=False)
    answer_2 = models.CharField(max_length=200, null=False)
    is_provider = models.BooleanField(null=False)
    # TODO: associate kitchen with provider if provider
    def __str__(self):
        return self.user.username

# class Provider(Eater):
#     def __str__(self):
#         return self.username


class Kitchen(models.Model):
#    WORKING_DAYS = (
#        ('Monday', 'Monday'),
#        ('Tuesday',  'Tuesday'),
#        ('Wednesday', 'Wednesday'),
#        ('Thursday', 'Thursday'),
#        ('Friday', 'Friday'),
#        ('Saturday', 'Saturday'),
#        ('Sunday', 'Sunday'),
#        )

    name = models.CharField(max_length=50, null=False)
#    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    open_time = models.CharField(max_length=10, null=False)
    close_time = models.CharField(max_length=10, null=False)
    image = models.ImageField(upload_to='img', blank=True)
    working_days = models.CharField(max_length=50, null=False)
    # TODO: Menu

    def __str__(self):
        return self.name

"""
class Menu(models.Model):
    pass

"""
class Food(models.Model):
    name = models.CharField(max_length=50, null=False)
    diet = models.CharField(max_length=7, choices=(('Veg','Veg'),('Non-Veg','Non-Veg')))
    price = models.FloatField(null=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
# class Order(models.Model):
#     pass
