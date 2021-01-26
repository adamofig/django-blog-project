from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Writer
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth import authenticate, logout, login

from .forms import ArticleForm


def welcome(request):
    last_30_days = Count(
        'written_by', filter=Q(created_at__gt=datetime.datetime(2021, 1, 1)))
    writer_info = Article.objects.values('written_by').annotate(
        last_30_days=last_30_days).annotate(total=Count('written_by'))
    return render(request, "blog/dashboard.html", {
        "articles": articles,
        "writer_info": writer_info
    })


def articles(request, id=None):
    if not request.user.is_authenticated:
        return HttpResponse(
            "Unauthorized! <a href='/login'> please login </a>")

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if id is None:
            form.save(request.user.username)
        else:
            Article.objects.filter(pk=id).update(
                title=form.data["title"],
                content=form.data["content"],
                edited_by=request.user.username)

        return HttpResponseRedirect('/article')
    elif id is None:
        form = ArticleForm()
        return render(request, "blog/article.html", {
            "article": None,
            "form": form
        })
    else:
        article = Article.objects.get(pk=id)
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            'id': article.id
        })
        return render(request, "blog/article.html", {
            "article": article,
            "form": form,
            "id": article.id
        })


def article_approval(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            "Unauthorized! <a href='/login'> please login </a>")

    id = request.user.id
    try:
        writer = Writer.objects.get(id_user=id)
        if not writer.is_editor:
            return HttpResponse(
                "Sorry, You need editor permission <a href='/'> return </a>")

        articles = Article.objects.filter(status=0)
        return render(request, "blog/article-approval.html", {
            "user": request.user,
            "articles": articles
        })
    except Exception as e:
        print(e)
        return HttpResponse(
            "The user is authenticated but not a writer <a href='/logout'> logout</a>"
        )


def articles_edited(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            "Unauthorized! <a href='/login'> please login </a>")

    id = request.user.id
    try:
        writer = Writer.objects.get(id_user=id)
        if not writer.is_editor:
            return HttpResponse(
                "Sorry, You need editor permission <a href='/'> return </a>")

        articles = Article.objects.exclude(status=0)

        return render(request, "blog/articles-edited.html",
                      {"articles": articles})
    except Exception as e:
        print(e)
        return HttpResponse("Unexpetected Error")


def approve_article(request, id):
    Article.objects.filter(pk=id).update(status=1)
    return HttpResponseRedirect('/article-approval')


def reject_article(request, id):
    Article.objects.filter(pk=id).update(status=2)
    return HttpResponseRedirect('/article-approval')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)

        if user is None:
            return HttpResponse("Unauthorized!")
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, "blog/login.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')
