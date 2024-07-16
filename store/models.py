from django.db import models






class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey("Product",on_delete=models.SET_NULL,null=True,related_name="+")

    #using magic string to show the name on admin panel its shoieng the object name 
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering =['title']



class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product set  due to  revesse relaitonship by def

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6 , decimal_places=2)  # Corrected the typo and added missing arguments
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT) # when  deleting collection we dont want to delete product 
    promotions =models.ManyToManyField(Promotion)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering =['title']

class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER ="S"
    MEMBERSHIP_GOLD ="G"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,"Silver"),
        (MEMBERSHIP_GOLD,"Gold"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=15)  # Assuming the phone number is a string
    birth_date = models.DateField(null = True  )
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        ordering =['first_name','last_name']

    
 

class Address(models.Model): 
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer =models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE ="C"
    PAYMENT_STATUS_FAILED ="F"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING ,'pending'),
        (PAYMENT_STATUS_COMPLETE ,'complete'),
        (PAYMENT_STATUS_FAILED ,'failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1 , choices=PAYMENT_STATUS_CHOICES , default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)


 
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=4)



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

