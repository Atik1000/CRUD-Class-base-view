# CRUD-Class-base-view


1. ### clone repo
  - git clone https://github.com/Atik1000/CRUD-Class-base-view
  - cd CRUD-Class-base-view

2. ### virtual env setup

- virtualenv2 --no-site-packages env
- source env/bin/activate

3. requirement install
(env)$ pip install -r requirements.txt



4. ### Run the project
    - Run `makemigrations` and `migrate`.
   
    - Create superuser to access the admin panel.
    - Run django `server` to view the project or application.
    ```shell script
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
