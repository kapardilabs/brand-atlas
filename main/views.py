from django.shortcuts import render, redirect
from .models import *
from . import utils


# Create your views here.


def index(request):
    if request.method == "GET":
        all_configs = CrawlConfig.objects.all()
        return render(request, "index.html", {"configs":all_configs})

    if request.method == "POST":
        pass


def crawl_data(request, config):
    if request.method == "POST":
        crawl_config = CrawlConfig.objects.get(id=config)
        crawl_config.crawled = True
        crawl_config.save()
        brands, countries, description = [], [], []
        try:
            brands, countries, description = utils.crawl_link(crawl_config.url, crawl_config.brand_selector,
                                                              crawl_config.country_selector,
                                                              crawl_config.description_selector,
                                                              crawl_config.user_agent)
        except Exception as e:
            print(e)

        country_objects = []
        if countries is not None:
            for c in countries:
                c_object = Country.objects.get_or_create(name=c)
                country_objects.append(c_object[0])
        print(len(brands))
        print(len(countries))
        if len(brands) == len(countries):
            print("brand == countries")
            if len(brands) == len(description):
                for idx, b in enumerate(brands):
                    b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx],
                                                           description=description[idx])
            else:
                for idx, b in enumerate(brands):
                    b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx])
        else:
            for idx, b in enumerate(brands):
                b_object = Brand.objects.get_or_create(name=b)

    return redirect("main:index")
