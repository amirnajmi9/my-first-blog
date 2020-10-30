from django.db import models
from django.utils import timezone
import random
# Create your models here.
def random_string():
    return str(random.randint(10000, 99999))
class post (models.Model):
	title = models.CharField(max_length = 60)
	slug = models.SlugField(max_length = 100)
	body = models.TextField()
	publish = models.DateTimeField(auto_now_add=True)
	created =  models.DateTimeField(auto_now_add=True)
	updated =  models.DateTimeField(auto_now = True)
	user = models.CharField(max_length = 11)
	daste = models.CharField(max_length = 60)
	image = models.ImageField(help_text=False, upload_to='img/')
	code = models.CharField(max_length = 5 , default = random_string)
	vrf = models.CharField(max_length = 1 , default = '0')


def __str__(self):
	return "post objects(id={}& title={})".format(self.id,self.title)
#@a1234578s
