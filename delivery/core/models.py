from django.db import models
from django.contrib.auth.models import AbstractUser

#Область
class Region(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

#Город
class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

#Район
class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.city.name
    
#Должность
class Position(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    
#Статус доставки
class Status(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

#ТБ-центр
class TBCenter(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return 'ТБ-центр: ' + self.city.name + ' ' + self.address

#Консилиум
class Consilium(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return 'Консилиум: ' + self.city.name + ' ' + self.address

#Пользователь системы
class User(AbstractUser):
    parent_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    TB_center = models.ForeignKey(TBCenter, on_delete=models.CASCADE, null=True, blank=True)
    consilium = models.ForeignKey(Consilium, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    whatsup = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    viber = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return str(self.first_name + ' ' + self.last_name + ' ' + self.parent_name)
    
#Пакет документов
class DocPack(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=6, null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    TB_center = models.ForeignKey(TBCenter, on_delete=models.CASCADE)
    consilium = models.ForeignKey(Consilium, on_delete=models.CASCADE, null=True, blank=True)
    reason_for_cancellation = models.TextField(null=True, blank=True)
    #Отправка и получение пакета документов из ТБ-центра в консилиум
    TBCenter_to_Consilium_sent_time = models.DateTimeField(null=True, blank=True)
    TBCenter_to_Consilium_delivered_time = models.DateTimeField(null=True, blank=True)
    #Отправка и получение пакета документов из консилиума координатору
    Consilium_to_Coordinator_sent_time = models.DateTimeField(null=True, blank=True)
    Consilium_to_Coordinator_delivered_time = models.DateTimeField(null=True, blank=True)
    #Отправка и получение пакета документов от координатора в ТБ-центр
    Coordinator_to_TBCenter_sent_time = models.DateTimeField(null=True, blank=True)
    Coordinator_to_TBCenter_delivered_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ': ' + self.status.name
