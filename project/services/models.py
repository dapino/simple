from django.db import models

'''
Contains all the hierarcy of the services that offers the platform: groups, categories, sub-categories, skus.
'''


class Skus (models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)
    specification = models.CharField(blank=True, null=True, max_length=500)
    price = models.IntegerField(default=0)
    time_stimated = models.DurationField()
    StatusType = models.TextChoices('StatusType', 'Enabled Disabled')
    Status = models.CharField(default='Enabled', choices=StatusType.choices, max_length=15)

    class Meta:
        verbose_name_plural = "Skus"
    
    def __str__(self):
        return self.name


class Subcategories (models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.name

class Categories (models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Groups (models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class Services (models.Model):
    idgroups = models.ForeignKey(Groups, on_delete=models.CASCADE)
    idcategories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    idsubcategories = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    idskus = models.ForeignKey(Skus, on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "Services"