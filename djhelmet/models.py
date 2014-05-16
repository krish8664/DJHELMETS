from django.db import models

class Product(models.Model):
    product_id          =   models.CharField(max_length=100)
    product_category    =   models.CharField(max_length=200)
    product_brand_name  =   models.CharField(max_length=200)
    product_model_name  =   models.CharField(max_length=200)
    price               =   models.CharField(max_length=200)


    def __unicode__(self):
        return self.product_id

class Images(models.Model):
    product_id          =   models.ForeignKey(Product)
    title               =   models.CharField(max_length = "200")
    product_images      =   models.ImageField(upload_to="Product_Image")

    def __unicode__(self):
        return self.title


class Colors(models.Model):
    color       = models.CharField(max_length=100)

    def __unicode__(self):
        return self.color


class Product_colors(models.Model):
    color             =  models.ForeignKey(Colors)
    product_id        =  models.ForeignKey(Product)

#    def __unicode__(self):
#        return self.color

class Size(models.Model):
    size                    =  models.CharField(max_length=100)

    def __unicode__(self):
        return self.size

class Product_size(models.Model):
    product_id              =  models.ForeignKey(Product)
    size                    =  models.ForeignKey(Size)

#    def __unicode__(self):
#        return self.size

