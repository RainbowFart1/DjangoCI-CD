python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi --ini /home/YuanQi/Django/uwsgi.ini

sleep infinity
