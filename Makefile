
manage_py := python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

createsuperuser:
	$(manage_py) createsuperuser

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests

# запуск pytest с подсчета процента покрытия тестами проекта (pytest-cov) с записью в html-файлы.
# создать в корне файл .coveragerc
pytest_cov:
	pytest ./app/tests --cov=app --cov-report html

# WINDOWS запуск pytest с подсчета процента покрытия тестами проекта (pytest-cov) с записью в html-файлы и показом в консоли,
# а так же, если процент покрытия выше 79,7754
pytest_cov_win:
	pytest ./app/tests --cov=app --cov-report html ; coverage report --fail-under=79.7754

# UBUNTU то же
pytest_cov_ub:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=79.7754