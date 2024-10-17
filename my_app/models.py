from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='streets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
