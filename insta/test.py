from django.test import TestCase
from . models import Image,Comment
from django.contrib.auth.models import User


class TestImages(TestCase):
  '''
  Class where we write our image models tests
  '''
  def setUp(self):
    '''
    function that runs before others
    '''
    self.test_user = User(username = 'Elizabeth')
    self.test_user.save()
    self.image = Image(image = 'Elizabeth.jpeg',name = 'liz',caption = 'beth',user = self.test_user)
    self.comments = Comment(comment = 'beauty',image = self.image,user = self.test_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))


  def test_save_image(self):
    self.image.save_image()
    image = Image.objects.all()
    self.assertTrue(len(image)>0)


  def test_delete_image(self):
    self.image2 = Image(image = 'nyambura.jpeg',name = 'nyambu',caption = 'nyambu',user = self.test_user)
    self.image2.save_image()
    self.image.save_image()
    self.image.delete_post()
    images = Image.objects.all()
    self.assertEqual(len(images),1)


  def test_search(self):
    self.image.save_image()
    self.image2 = Image(image = 'nyambura.jpeg',name = 'nyambu',caption = 'nyambu',user = self.test_user)
    self.image2.save_image()
    search_term = "nyambu"
    search1 = Image.search_images(search_term)
    search2 = Image.objects.filter(name__icontains = search_term)
    self.assertEqual(len(search2),len(search1))


  def test_display_images(self):
    self.image.save_image()
    self.image2= Image(image = 'nyambura.jpeg',name = 'nyambura',caption = 'nyambura',user = self.test_user)
    self.image2.save_image()
    dt = Image.display_images()
    self.assertEqual(len(dt),2)


class TTestComments(TestCase):
  '''
  class that will test the profile model
  '''
  def setUp(self):
    self.test_user = User(username = 'thee_dev')
    self.test_user.save()
    self.image = Image(image = 'thee.jpeg',name = 'dev',caption = 'dev',user = self.test_user)
    self.comments = Comment(comment = 'beauty',image = self.image,user = self.test_user)


