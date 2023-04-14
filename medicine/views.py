from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from .models import Medicine, GenericMedicine

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from django.http import HttpResponse
from django.views.decorators.http import require_GET

BLOG_POSTS_PER_PAGE = 15


def home(request):
    context = {}

    query = request.GET.get("query", "")
    page = request.GET.get("page", 1)
    if query:
        medicines = Medicine.objects.filter(Q(name__istartswith=query)).order_by("name")
    else:
        medicines = Medicine.objects.all()

    medicine_list_paginator = Paginator(medicines, BLOG_POSTS_PER_PAGE)
    medicine_list_paginator.get_elided_page_range(3, on_each_side=1, on_ends=0)

    try:
        medicine_list = medicine_list_paginator.page(page)
    except PageNotAnInteger:
        medicine_list = medicine_list_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        medicine_list = medicine_list_paginator.page(medicine_list_paginator.num_pages)

    medicine_list.adjusted_elided_pages = medicine_list_paginator.get_elided_page_range(
        page
    )

    context["medicines"] = medicine_list

    context["query"] = query

    print(medicine_list.paginator.page_range)

    return render(request, "home.html", context)


def details(request, pk, slug):
    context = {}
    medicine = get_object_or_404(Medicine, pk=pk, slug=slug)
    context["medicine"] = medicine
    return render(request, "medicine_details.html", context)


def privacy_policy_view(request):

    return render(request, "privacy_policy.html", context={})


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Sitemap : https://infosdiv.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
