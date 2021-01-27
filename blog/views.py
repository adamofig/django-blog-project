import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ArticleForm
from .models import Article, Writer


@login_required()
def get_dashboard(request):
    last_30_days = Count(
        'written_by', filter=Q(created_at__gt=datetime.datetime(2021, 1, 1)))
    writer_info = Article.objects.values('written_by').annotate(
        last_30_days=last_30_days).annotate(total=Count('written_by'))
    return render(request, "blog/dashboard.html", {
        "articles": articles,
        "writer_info": writer_info
    })


@login_required()
def articles(request, id=None):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if id is None:
            form.save(request.user)
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
        # article = Article.objects.get(pk=id)

        article = get_object_or_404(Article, id=id)
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


@login_required()
def article_approval(request):
    try:
        writer = get_object_or_404(Writer, user=request.user)
        if not writer.is_editor:
            return HttpResponse(
                "Sorry, You need editor permission <a href='/'> return </a>")

        articles = Article.objects.filter(status=Article.PENDING)
        return render(request, "blog/article-approval.html", {
            "user": request.user,
            "articles": articles
        })
    except Exception as e:
        print(e)
        return HttpResponse(
            "The user is authenticated but not a writer <a href='/logout'> logout</a>"
        )


@login_required()
def article_edited(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')

    user_id = request.user.id
    try:
        writer = Writer.objects.get(user=user_id)
        if not writer.is_editor:
            return HttpResponse(
                "Sorry, You need editor permission <a href='/'> return </a>")

        articles = Article.objects.exclude(status=0)

        return render(request, "blog/article-edited.html",
                      {"articles": articles, "Article": Article})
    except Exception as e:
        print(e)
        print("Tenemos aquí un error", e)
        return HttpResponse("Unexpetected Error")


def approve_article(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')

    Article.objects.filter(pk=id).update(status=Article.ACCEPTED)
    return HttpResponseRedirect('/article-approval')


def reject_article(request, id):
    Article.objects.filter(pk=id).update(status=Article.REJECTED)
    return HttpResponseRedirect('/article-approval')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("user", user)
        if user is not None:
            login(request, user)

            if user is None:
                return HttpResponse("Unauthorized!", )
            else:
                # return HttpResponseRedirect('login')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Username or password not correct')
            return HttpResponseRedirect('login')
            # return HttpResponse("User not Existe ")

    else:
        return render(request, "blog/login.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


def handler404(request, exception):
    return render(request, 'blog/404.html')
