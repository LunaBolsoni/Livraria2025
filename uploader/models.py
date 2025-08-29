from django.db import models

class Image(models.Model):
    imagem = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
