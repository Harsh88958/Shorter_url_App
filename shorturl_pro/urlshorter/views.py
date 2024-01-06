# Imports
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, Http404
import random, string
from django.db.models import Q
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Give the randomly alpha numerics
def generate_short_url():
    random_numbers = "".join(random.choice(string.digits) for i in range(3))
    random_letters = "".join(random.choice(string.ascii_lowercase) for i in range(2))
    random_combination = random_numbers + random_letters
    combination_list = list(random_combination)
    random.shuffle(combination_list)
    joined_suffled_letters = "".join(combination_list)
    if URLShortener.objects.filter(short_url=joined_suffled_letters).exists():
        generate_short_url()
    else:
        return joined_suffled_letters


# Give the short URL function
def shorten_url(request):
    if request.method == "POST":
        long_url = request.POST["long_url"]
        if not URLShortener.objects.filter(long_url=long_url).exists():
            # short_url = 'http://cs.in/'+generate_short_url()
            short_url = generate_short_url()
            url_entry = URLShortener(long_url=long_url, short_url=short_url)
            url_entry.save()
            long = URLShortener.objects.get(long_url=long_url)
            data = {
                "long": long.short_url,
            }
            return render(request, "index.html", {"data": data})

        else:
            url_entry = URLShortener.objects.get(long_url=long_url)
            data = {"long": url_entry.short_url}
            return render(request, "index.html", {"data": data})

    return render(request, "index.html")


# Short URL redirect function
def redirect_url(request, short_url):
    try:
        url_entry = URLShortener.objects.get(short_url=short_url)
        # Use for number of counts
        url_entry.no_of_count += 1
        url_entry.save()
        return HttpResponseRedirect(url_entry.long_url)

    except URLShortener.DoesNotExist:
        raise Http404("Short URL does not exist")


# This is for search and filter data
class TableViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Search query perm
        query = self.request.query_params.get("search")
        # no_of_count query perm
        no_of_count = self.request.query_params.get("no_of_count")

        if query:
            try:
                # Search the data
                query_id = int(query)
                search_data = URLShortener.objects.filter(
                    Q(id=query_id) | Q(short_url=query)
                ).values()
            except ValueError:
                search_data = URLShortener.objects.filter(short_url=query).values()
        else:
            search_data = URLShortener.objects.values()
            # Sort in ascending order

        if no_of_count and no_of_count.lower() == "asc":
            search_data = search_data.order_by("no_of_count")
            # Sort in descending order
        elif no_of_count and no_of_count.lower() == "dsc":
            search_data = search_data.order_by("-no_of_count")
        return Response({"data": search_data})


# Pagination
class UrlPagination(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = URLShortener.objects.all()
    serializer_class = Urlshotserializer


def alldata(request):
    alldata = URLShortener.objects.all()
    return render(request, "alldata.html", {"alldata": alldata})
