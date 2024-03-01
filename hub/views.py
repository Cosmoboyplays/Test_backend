from django.db.models import Count
from django.shortcuts import (render)
from hub.models import Products, Lessons, Group
from users.utils import AccessManager


access_manager = AccessManager()


def group_selection(product_id, username):  # юзера будем брать из request при боевом проекте

    product = Products.objects.get(id=product_id)
    access_manager.add_user(product.name, username)  # дал доступ этому юзеру к продукту
    max_users = product.max_users
    groups = product.groups.all()

    groups = groups.annotate(num_students=Count('students')).order_by('-num_students')

    for group in groups:
        if group.students.all() < max_users:
            group.students.add(username)
            break



    # return render(request, 'hub/group_selection.html', {'groups': groups})