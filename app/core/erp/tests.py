from django.test import TestCase
from config.wsgi import *
from core.erp.models import *

data = ['Milk and dairy products', 'Meat, fish and eggs', 'Potatoes, legumes, nuts',
         'Vegetables', 'Fruits', 'Cereals and derivatives, sugar and sweets',
         'Fats, oil and butter']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Saving Register N°{}'.format(cat.id))

