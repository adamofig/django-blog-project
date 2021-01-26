### Start the project
django-admin startproject blogtoy ./

### Run the app 
python manage.py runserver

### Init application 
python manage.py startapp blog

### Create super user
python manage.py createsuperuser

python manage.py creat
### Migrations 
python manage.py migrate
python manage.py makemigrations

## Models 

Article
created_at
title
content
status
written_by (Writer)
edited_by (Writer)

Writer
is_editor (boolean)
name


### query for get writter details 
    with one as (select written_by, count(written_by) last_30 from blog_article  where created_at > date('now','-30 days') GROUP by written_by)
    select blog_article.written_by, count(blog_article.written_by) total_articles, one.last_30 from blog_article  
    inner join one on one.written_by = blog_article.written_by