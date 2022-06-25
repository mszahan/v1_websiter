from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    delivary_mail = models.EmailField(max_length=254)
    country = CountryField()

    def __str__(self):
        return self.delivary_mail



CATEGORY_CHOICES=(
    ('general', 'General'),
    ('premium', 'Premium'),
)

class PortfolioPricing(models.Model):
    package_name = models.CharField(max_length=100)
    features = models.TextField()
    price = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    def feature_ls(self):
        return self.features.split(';')
    

    def __str__(self):
        return str(self.price)



class PortfolioTheme(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ecom/theme_image')
    description = models.TextField()
    
    def __str__(self):
        return self.name


STATUS_CHOICES =(
    ('Pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('Delivered', 'Delivered'),
)

class OrderPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.ForeignKey(PortfolioPricing, on_delete=models.CASCADE)
    theme = models.ForeignKey(PortfolioTheme, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    ordered_date = models.DateTimeField(auto_now_add=True)
    domain_name = models.CharField(max_length=100, null=True)
    buy_domain = models.CharField(max_length=100, null=True)

    

    def __str__(self):
        return self.theme.name

