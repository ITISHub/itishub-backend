from django.db import models


class Creator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    avatar = models.ImageField()
    about = models.TextField()
    telegram = models.URLField()
    github = models.URLField()
    vk = models.URLField()

    def __str__(self):
        return self.name + " " + self.surname


class HomeCard(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    pdf_file = models.FileField(blank=True,upload_to='media/homecards')

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    url = models.CharField(max_length=200)
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.title

    def get_lessons(self):
        return Lesson.objects.filter(course=self)