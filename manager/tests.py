from django.test import TestCase
from .models import Neighbourhood,Business,User,Post,Comments
from django.contrib.auth.models import User


# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='nick',email='Nickromero187@@gmail.com')
        self.new_user.save()
        self.westlands = Neighbourhood(name='kikuyu',location='westlands',occupants=5)
        self.westlands.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.westlands,Neighbourhood))

    def test_save_neighborhood(self):
        self.thome.save_neighborhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood)>0)




class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="nick",email="Nickromero187@@gmail.com")
        self.new_user.save()
        self.thome = Neighbourhood(name='kikuyu',location='westlands',occupants_count=5,admin=self.new_user)
        self.thome.save_neighborhood()
        self.garage = Business(name='garage',email='Garage@gmail.com',user=self.new_user,neighborhood=self.thome)
        self.garage.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.garage,Business))

    def test_save_business(self):
        self.garage.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)




class PostTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="nick",email="Nickromero187@gmail.com")
        self.new_user.save()
        self.westlands = Neighbourhood(name='kikuyu',location='westlands',occupants_count=5,admin=self.new_user)
        self.westlands.save_neighborhood()
        self.nick = User(name="nick",user=self.new_user,neighborhood=self.westlands)
        self.nick.save_user()
        self.new_post=Post(post='Test dfghj post',author=self.nick)

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)




class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="nick",email="Nickromero187@gmail.com")
        self.new_user.save()
        self.westlands = Neighbourhood(name='kikuyu',location='westlands',occupants_count=5,admin=self.new_user)
        self.westlands.save_neighborhood()
        self.nick = User(name="nicki",user=self.new_user,neighborhood=self.westlands)
        self.nick.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.nick,User))