Тестовое задание

Для запуска необходимо :

1. Клонировать репозиторий
2. Установить зависимости
pip3 install -r requirements.txt
3. Запустить
python manage.py runserver
4. Перейти на http://127.0.0.1:8000/admin/
Суперюзер
log:  Test
pass: test
5. Api соответствует адресам 
products/
lessons/
соответственно тз.



Доступ юзера к продукту осуществлен через словарь users/access_to_product.json
Каждому продукту соответствует список легализованных юзеров.
В файле users/utils.py написан класс для управление процессами связанными с доступом к продукту.
Чтобы осуществить проверку доступа юзера к продукту используем check_user_in_product с аргументами
product_name и user_name.


Алгоритм распределения находится в файле hub/views.py
Работает исходя из моего понимания тз - сначала одна группа добирает минимальное количество студентов, затем вторая и т.д.
После распределение происходит таким образом, чтобы различие между группами не превышало 1.


Api реализовано исходя из ТЗ, но т.к. сегодня 2.03 я не могу по ссылке получить доступ к ТЗ, я делал API по памяти,
и 3 задание из этого блока скорее всего не выполнил.

Автор: Никита Ильин
