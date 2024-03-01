from django.shortcuts import (render)
from hub.models import Products, Lessons, Group
from users.models import User
from users.utils import AccessManager

access_manager = AccessManager()


def group_selection(product_id, username):  # юзера будем брать из request на боевом проекте

    product = Products.objects.get(id=product_id)
    access_manager.add_user(product.name, username)  # дал доступ этому юзеру к продукту
    user = User.objects.get(username=username)

    max_users = product.max_users
    min_users = product.min_users
    groups = product.groups.all()

    '''Ниже алгоритм распределения в группы, сначала он добивает группу 1 до минимума, затем вторую и т.д.
    Когда везде минимум, он добавляет в группу по очереди, чтобы разница между группами была максимум 1
    '''
    groups = sorted((group.name_count() for group in groups), key=lambda x: x[1], reverse=True)
    # -> (Query group, count)
    flag = True
    for group in groups:
        if group[1] < min_users:
            if group[1] < max_users:
                group[0].students.add(user)
                print(f'добавил юзера {username} в группу {group[0].name}')
                flag = False
                break

    if flag:
        groups = sorted(groups, key=lambda x: x[1])  # меньше в начале
        for group in groups:
            if group[1] < max_users:
                group[0].students.add(user)
                print(f'добавил юзера {username} в группу {group[0].name}')
                break
            else:
                print(f'Достигнут максимум в во всех группах')
                break

    # return render(request, 'hub/group_selection.html', {'groups': groups})
