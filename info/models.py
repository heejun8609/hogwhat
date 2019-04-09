from django.db import models


class ThisMonthDisease(models.Model):
    name = models.CharField(max_length=60, verbose_name='질병 이름')
    symptoms = models.TextField(verbose_name='주요 증상')
    treatments = models.TextField(verbose_name='예방 및 치료')

    def __str__(self):
        return self.name

class AtTimesLikeThis(models.Model):
    question = models.TextField(verbose_name='Q')
    answer = models.TextField(verbose_name='A')
    reference = models.CharField(max_length=60, verbose_name='출처')
