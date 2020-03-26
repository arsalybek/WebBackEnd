from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def to_json(self):
        return {
            'id': self.id,
            'category_id': self.category_id.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
        }




