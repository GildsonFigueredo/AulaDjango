from django.db import models

# Create your models here.
class usuario (models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.TextField(max_length=100)
   idade = models.IntegerField()

   def __str__(self):
      return self.nome
   
   def get_info(self):
      return f'Nome:{self.nome}, Idade:{self.idade}'