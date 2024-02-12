from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = self.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user_account', kwargs={'slug': self.slug})


class Animals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_ru = models.TextField(verbose_name='Слово на Русском')
    word_en = models.TextField(verbose_name='Слово на Английском')

    def __str__(self):
        return self.word_ru

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class Technic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_ru = models.TextField(verbose_name='Слово на Русском')
    word_en = models.TextField(verbose_name='Слово на Английском')

    def __str__(self):
        return self.word_ru

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'


class Colors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_ru = models.TextField(verbose_name='Слово на Русском')
    word_en = models.TextField(verbose_name='Слово на Английском')

    def __str__(self):
        return self.word_ru

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
