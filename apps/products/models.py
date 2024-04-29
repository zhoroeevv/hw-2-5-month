from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="называние"
    )
    description = models.TextField(
        verbose_name="описание"
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    image = models.ImageField(
        upload_to='product_images/', verbose_name="Фотография"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        