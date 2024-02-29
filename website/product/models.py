from django.db import models


# Create your models here.


class companyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

    
class category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    
class product(models.Model):
    product_name =models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add= True,null=True)
    
    
    def __str__(self) -> str:
        return self.product_name
    
class about_us(models.Model):
    
    vision = models.CharField(max_length = 10)
    vision_discription = models.TextField()
    v_image = models.ImageField()
    mission = models.CharField(max_length = 10)
    mission_discription = models.TextField()
    m_image = models.ImageField()
    value = models.CharField(max_length = 10)
    value_discription = models.TextField()
    value_image = models.ImageField()
    
    
    
class Form(models.Model):
    full_name=models.CharField(max_length =100)
    address=models.CharField(max_length=100)
    car_brand=models.CharField(max_length=100)
    car_model=models.CharField(max_length=100)
    additional_option = models.CharField(max_length=300)
    price=models.IntegerField()
     
     
    def __str__(self) :
      return self.full_name

class contact(models.Model):
   name  = models.CharField(max_length=100)
   email  = models.EmailField()
   comment  = models.TextField()

   def __str__(self) :
      return self.name
  
class Home(models.Model):
    name = models.CharField(max_length=100) 
    slogan = models.CharField(max_length=200)
    background_image = models.ImageField()
    
    
    def __str__(self) :
       return self.name