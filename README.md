# CRUD-Class-base-view



1. ### Project setup 
    - git pull `https://github.com/Atik1000/CRUD-Class-base-view`.
    - cd `CRUD-Class-base-view`.
 
2. ### install Virtual env,active ans requirement file install
    - python3 -m venv env
    - source env/bin/activate
    - pip install -r requirements.txt
    



3. ### Run the project
    - Run `makemigrations` and `migrate`.
    - Run `tests` and `linting` to assure nothing is broken.
    - Create superuser to access the admin panel.
    - Run django `server` to view the project or application.
    - Generate `coverage` reports locally.
    ```shell script
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
