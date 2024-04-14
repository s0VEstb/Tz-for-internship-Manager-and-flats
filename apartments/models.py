from django.db import models

# Create your models here.


class Apartment(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активно'),
        ('reserved', 'Зарезервировано'),
        ('sold', 'Продано'),
        ('installment', 'Рассрочка'),
        ('barter', 'Бартер'),
    )
    object = models.CharField(max_length=100)
    floor = models.IntegerField()
    square = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    price = models.IntegerField()
    client = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        related_name='apartments',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.id}. Object: {self.object} - {self.status}'


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}. {self.full_name} {self.contract_number}'
