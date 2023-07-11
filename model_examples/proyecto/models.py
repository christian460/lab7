from django.db import models

# Create your models here.

class Autor(models.Model):
    name=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    perfil=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
    
class Proyecto(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




    