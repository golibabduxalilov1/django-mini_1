from django.shortcuts import render, get_object_or_404, redirect

from .models import Link


def index(req):
    links = Link.objects.all()
    context = {"links": links}
    return render(req, "index.html", context)


def root_link(req, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()

    return redirect(link.url)


def add_link(req):
    return render(req, "create.html", {})
