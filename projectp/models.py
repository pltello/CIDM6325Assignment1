from django.db import models


class Project(models.Model):
    """A project that will be managed using the application."""
    name = models.CharField(
        max_length=50, help_text="The name of the Project.")

    def __str__(self):
        return self.name


class Task(models.Model):
    """A project task."""
    title = models.CharField(max_length=75, help_text="The name of the Task.")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
