from django.contrib.auth.models import Group
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

User.objects.all().delete()
User.objects.create_superuser(username='krishna',email='krishnasadhu9@gmail.com', password='12341234')
print('create super user krishna')


user_obj = User.objects.create_user(username='user1',email='krishnasadhu9@gmail.com', password='12341234')
g = Group.objects.get(name='user')
g.user_set.add(user_obj)
print('created user1 ')

staff_obj = User.objects.create_user(username='staff1',email='krishnasadhu9@gmail.com', password='12341234')
g = Group.objects.get(name='staff')
g.user_set.add(staff_obj)
print('created staff_obj')
