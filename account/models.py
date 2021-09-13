from django.db import models

# Create your models here.
from django.db import models
import re 
from datetime import datetime
# Create your models here.


class UserManager(models.Manager):

     def validator(self, postData):

        errors = {}

        #LARGO MINIMO NOMBRE
        if len(postData["nombre"]) < 5:
            errors["nombre"] = "Nombre debe tener minimo 5 caracteres!"
        #EMAIL 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):       
            errors['email'] = "Direccion de correo no valida!"

        #FECHA
        DATE_REGEX = re.compile(r'^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$')
        if not DATE_REGEX.match(postData["fecha_nacimiento"]):
            errors["date"] = "Formato fecha no valido! es: (YY-MM-DD)"

        #MAYOR A 16 AÑOS 
        date_obj = datetime.strptime(postData["fecha_nacimiento"],"%Y-%m-%d")
        birth_date = int(date_obj.strftime("%Y%m%d"))
        sixteenold = int(datetime.now().strftime("%Y%m%d"))- 160000
        
        if birth_date > sixteenold:
            errors["date"] = "Tienes que ser mayor de 16 años para registrarte"
        
        #CONTRASEÑAS IGUALES
        if postData["password"] != postData["confirm_pass"]:
            errors["confirm_pass"] = "Las contraseñas no coinciden!"

        #CONTRASEÑA
        PASS_REGEX = re.compile(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$')
        if not PASS_REGEX.match(postData["password"]):
            errors["password"] = f"Contraseña debe incluir:\n-Al menos una letra mayúscula en inglés\n-Al menos una letra minúscula en inglés\n-Al menos un dígito\n-Al menos un personaje especial\n-Mínimo ocho de longitud"

        return errors

class User(models.Model):

    nombre = models.CharField(max_length=95)
    apellido = models.CharField(max_length=95)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateTimeField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido}  Email: {self.email}"

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email}"
