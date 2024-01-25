from django.db import models

# Create your models here.
class BOOKS_TBL(models.Model):
    ISBN=models.CharField(max_length=10)
    title=models.CharField(max_length=60)
    authors=models.CharField(max_length=15)
    books=models.IntegerField()
   #the profile picture
    profile=models.ImageField(null=True,blank=True, upload_to='images/')

    def __str__(self):
        return f"{self.id}:{self.title} by {self.authors}"
    

class ORDERS_TBL(models.Model):
    order_number=models.ForeignKey(BOOKS_TBL,on_delete=models.CASCADE,related_name="orders")
    username=models.CharField(max_length=30)
    ISBN=models.ForeignKey(BOOKS_TBL,on_delete=models.CASCADE,related_name="codes")
    date=models.DateField()

    def __str__(self):
        return f"{self.username}: {self.order_number} {self.ISBN}"
