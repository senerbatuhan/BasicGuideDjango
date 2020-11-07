from django.db import models

# Create your models here.
class Guide(models.Model):
    isim = models.CharField(verbose_name="İsim", max_length=20)
    soyisim = models.CharField(verbose_name="Soyisim", max_length=20)
    numara = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{isim} {soyisim}'.format(
            isim=self.isim,
            soyisim=self.soyisim
        )