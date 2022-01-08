from django.db import models
from authentication.models import User

# Create your models here.


class Income(models.Model):

    INCOME_OPTIONS = [
        ('SALARY', 'SALARY'),
        ('FREELANCING', 'FREELANCING'),
        ('OTHERS', 'OTHERS'),
    ]

    source = models.CharField(choices=INCOME_OPTIONS, max_length=256)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.owner
