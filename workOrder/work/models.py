from django.db import models
from django.db.models.functions import Now


class Pekerjaan(models.Model):
    pekerjaan = models.CharField(max_length=255)

    class Meta:
        ordering = ('pekerjaan',)    # iterable
        verbose_name_plural = 'pekerjaan'

    def __str__(self):
        return self.pekerjaan


class Pengguna(models.Model):
    pengguna = models.CharField(max_length=255)

    class Meta:
        ordering = ('pengguna',)
        verbose_name_plural = 'pengguna'

    def __str__(self):
        return self.pengguna


class Status(models.Model):
    status = models.CharField(max_length=255)

    class Meta:
        ordering = ('status',)
        verbose_name_plural = 'status'

    def __str__(self):
        return self.status


class Pelaksana(models.Model):
    pelaksana = models.CharField(max_length=255)

    class Meta:
        ordering = ('pelaksana',)
        verbose_name_plural = 'pelaksana'

    def __str__(self):
        return self.pelaksana

# Create your models here.


class Report(models.Model):
    # nomor = models.IntegerField(default=0)
    jam = models.DateField()
    jenis_pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE)
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    pelaksana = models.ForeignKey(Pelaksana, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255)
