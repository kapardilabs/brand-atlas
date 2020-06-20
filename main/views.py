from django.shortcuts import render, redirect
from .models import *
from . import utils


# Create your views here.


def index(request):
    if request.method == "GET":
        all_configs = CrawlConfig.objects.all()
        return render(request, "index.html", {"configs": all_configs})

    if request.method == "POST":
        pass


def crawl_data(request, config):
    if request.method == "POST":

        crawl_config = CrawlConfig.objects.get(id=config)
        crawl_config.crawled = True
        crawl_config.save()
        context = {"url": crawl_config.url}
        brands, countries, description = [], [], []
        try:
            brands, countries, description = utils.crawl_link(crawl_config.url, crawl_config.brand_selector,
                                                              crawl_config.country_selector,
                                                              crawl_config.description_selector,
                                                              crawl_config.user_agent)

            country_objects = []
            if countries is not None:
                for c in countries:
                    c_object = Country.objects.get_or_create(name=c)
                    country_objects.append(c_object[0])
            no_of_brands = len(brands)
            no_of_countries = len(countries)
            no_of_descriptions = len(description)

            context.update({"no_of_brands": no_of_brands, "no_of_countries": no_of_countries,
                            "no_of_descriptions": no_of_descriptions})

            if no_of_brands == no_of_countries:
                print("brand == countries")
                if no_of_brands == no_of_descriptions:
                    for idx, b in enumerate(brands):
                        b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx],
                                                               description=description[idx])
                else:
                    for idx, b in enumerate(brands):
                        b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx])
            else:
                for idx, b in enumerate(brands):
                    b_object = Brand.objects.get_or_create(name=b)
        except Exception as e:
            context.update({"exception": e})
        return render(request, "response.html", context)
    return redirect("main:index")


def edit_brand(request):
    if request.method == "GET":
        brand_to_edit = Brand.objects.filter(origin_country_id=1).order_by("id").first()
        all_countries = Country.objects.all()
        context = {"editbrand": brand_to_edit, "allCountries": all_countries}

        return render(request, "brandedit.html", context)

    if request.method == "POST":
        entry_id = request.POST.get("brandId", None)
        changed_name = request.POST.get("brandName", None)
        changed_country_id = request.POST.get("originCountry", None)
        expected_country = Country.objects.get(id=changed_country_id)
        Brand.objects.filter(id=entry_id).update(name=changed_name, origin_country=expected_country)

        return redirect("main:edit")
