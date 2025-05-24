from django.contrib.auth.models import Group, User

def get_all_group():
    return Group.objects.all().order_by("id")

def get_all_user():
    return User.objects.all().order_by("id")

def get_user(pk):
    return User.objects.get(pk=pk)

def get_group(user):
    return User.objects.get(pk=user.pk).groups.first()
