### Start the project
django-admin startproject blogtoy ./

### Run the app 
python manage.py runserver

### Init application 
python manage.py startapp dashboard


### super user
python manage.py createsuperuser

### 
python manage.py migrate
python manage.py makemigrations


### query for get writter details 
    with one as (select written_by, count(written_by) last_30 from dashboard_article  where created_at > date('now','-30 days') GROUP by written_by)
    select dashboard_article.written_by, count(dashboard_article.written_by) total_articles, one.last_30 from dashboard_article  
    inner join one on one.written_by = dashboard_article.written_by