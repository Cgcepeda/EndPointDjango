from django.db import models

# Create your models here.


#Class generic is created to group the construction of the attributes id and slug 
#so that it doesn't be necessary to write in all classes 
class Generic(models.Model):
    slug = models.CharField(max_length=30)
    def __str__(self):
        return self.slug




class Reviews(models.Model):
    feedback = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=0)
    avatar = models.URLField()

    def __str__(self):
        return self.feedback


class PropertyTypes(Generic):
    pass

class Transaction(Generic):
    pass

class States(Generic):
    pass


class Cities(models.Model):
    slug = models.CharField(max_length=30)
    zip = models.PositiveSmallIntegerField()
    state = models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.slug


class Categories(Generic):
    pass


class Properties(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    price = models.PositiveIntegerField()
    city = models.ForeignKey('Cities', on_delete=models.CASCADE)
    bath = models.DecimalField(max_digits=2, decimal_places=0)
    beds = models.DecimalField(max_digits=2, decimal_places=0)
    sqft = models.PositiveSmallIntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    propertietypes = models.ForeignKey('PropertyTypes', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title