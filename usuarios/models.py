from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
    #REQUIRED_FIELDS = ['matricula','username' , 'email' ,'cpf', 'phone']

    def _create_user(self, username, numero,email, cpf, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not username:
           raise ValueError("O username é obrigatório")
        if not cpf:
           raise ValueError("O cpf é obrigatório")
        
        email = self.normalize_email(email)
        
        """ username = seusername
        matricula = seemail """
        
        user = self.model(username=username, numero=numero, email=email, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  username, email, numero, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user( username, numero, email, cpf, password, **extra_fields)

    def create_superuser(self, username, numero,email, cpf , password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user( username, numero, email, cpf , password, **extra_fields)



class CustomUser(AbstractUser):


    username = models.CharField(("Nome"), max_length=50, unique=False, primary_key=None)
    email = models.EmailField("E-mail", unique=True)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    numero = models.IntegerField(("Numero para votacao"), unique=True, null=True, blank=True)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    total_de_votos = models.IntegerField(("Total de votos"), default=0, null=True, blank=True)
    photo = models.ImageField(upload_to='Media', blank=True, null=True)
    
    is_staff = models.BooleanField('Membro da equipe', default=True)
    

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username' , 'email', 'numero']

    def __str__(self):
        return self.username

    objects = UserManager()