from django.db import models
from django.urls import reverse

from vmsUser.models import Requisition


class LogBook(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, null=True)
    startingkm = models.DecimalField(verbose_name='Enter starting value...', null=True, decimal_places=2, max_digits=10)
    endingkm = models.DecimalField(verbose_name='Enter ending value...', null=True, blank=True, decimal_places=2, max_digits=10)
    startingfuel = models.DecimalField(verbose_name='Enter starting fuel...', null=True, blank=True, decimal_places=2, max_digits=10)
    endingfuel = models.DecimalField(verbose_name='Enter ending fuel...', null=True, blank=True, decimal_places=2, max_digits=10)
    suppliedfuel = models.DecimalField(verbose_name='Enter spent fuel...', null=True, blank=True, decimal_places=2, max_digits=10)

    def totalkm(self):
        totalkm = self.endingkm - self.startingkm
        return totalkm

    def remainedfuel(self):
        remainedfuel = (self.startingfuel + self.suppliedfuel) - self.endingkm
        return remainedfuel

    def get_absolute_url(self):
        return reverse('datainput', kwargs={"id": self.pk})

    def __str__(self):
        return str(self.startingfuel)