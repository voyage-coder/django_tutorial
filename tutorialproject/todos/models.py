from django.db import models

# Create your models here.

# this will be like ENUMS
class PriorityChoices(models.IntegerChoices):
    LOW = 1, 'Low'
    MEDIUM = 2, 'Medium'
    HIGH = 3, 'High'

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    # all these columns by default are not nullable
    # if we want to allow them as null we need to set it
    deadline = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PriorityChoices.choices, null=True, blank=True)
    def __str__(self):
        return f"{self.id} - {self.title}"
    # so when we now print a todo obj in python we see it's id and title
    # now we  need to create a todo view that allows us to create todos
    # id is implicitly created when migrating