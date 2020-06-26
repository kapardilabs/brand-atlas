from django.shortcuts import render, redirect
from .models import *
from . import utils
from django.contrib import messages


# Create your views here.


def index(request):
    all_brands = Brand.objects.all()

    return render(request, "sb-admin/index.html", {"allBrands": all_brands})


# def crawl_data(request, config):
#     if request.method == "POST":
#
#         crawl_config = []
#         crawl_config.crawled = True
#         crawl_config.save()
#         context = {"url": crawl_config.url}
#         brands, countries, description = [], [], []
#         try:
#             brands, countries, description = utils.crawl_link(crawl_config.url, crawl_config.brand_selector,
#                                                               crawl_config.country_selector,
#                                                               crawl_config.description_selector,
#                                                               crawl_config.user_agent)
#
#             country_objects = []
#             if countries is not None:
#                 for c in countries:
#                     c_object = Country.objects.get_or_create(name=c)
#                     country_objects.append(c_object[0])
#             no_of_brands = len(brands)
#             no_of_countries = len(countries)
#             no_of_descriptions = len(description)
#
#             context.update({"no_of_brands": no_of_brands, "no_of_countries": no_of_countries,
#                             "no_of_descriptions": no_of_descriptions})
#
#             if no_of_brands == no_of_countries:
#                 print("brand == countries")
#                 if no_of_brands == no_of_descriptions:
#                     for idx, b in enumerate(brands):
#                         b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx],
#                                                                description=description[idx])
#                 else:
#                     for idx, b in enumerate(brands):
#                         b_object = Brand.objects.get_or_create(name=b, origin_country=country_objects[idx])
#             else:
#                 for idx, b in enumerate(brands):
#                     b_object = Brand.objects.get_or_create(name=b)
#         except Exception as e:
#             context.update({"exception": e})
#         return render(request, "response.html", context)
#     return redirect("main:index")
#

def create_brand(request):
    if request.method == "GET":
        all_countries = Country.objects.all()
        all_categories = Category.objects.all()
        all_brands = Brand.objects.all()
        context = {"allCategories": all_categories, "allCountries": all_countries, "allBrands": all_brands}

        return render(request, "sb-admin/blank.html", context)

    if request.method == "POST":
        try:
            name = request.POST.get("brandName", None)
            logo_url = request.POST.get("logoUrl", None)
            changed_country = request.POST.get("originCountry", None)
            changed_description = request.POST.get("brandDescription", None)
            category_string = request.POST.get("category", None)
            parent_brand_string = request.POST.get("parentBrand", None)
            category = Category.objects.get_or_create(name=category_string)
            expected_country = Country.objects.get(name=changed_country)
            if parent_brand_string != "None":
                parent_brand = Brand.objects.get(id=parent_brand_string)
                Brand.objects.create(name=name, origin_country=expected_country, logo=logo_url,
                                     description=str(changed_description), category=category[0], parent=parent_brand)
            else:
                Brand.objects.create(name=name, origin_country=expected_country, logo=logo_url,
                                     description=str(changed_description), category=category[0])

            messages.success(request, "Brand Created!")
        except Exception as e:
            messages.error(request, str(e))
        return redirect("main:index")


def edit_brand(request, brand_id):
    if request.method == "GET":
        brand_to_edit = Brand.objects.get(id=brand_id)
        all_countries = Country.objects.all()
        all_categories = Category.objects.all()
        all_brands = Brand.objects.all()
        context = {"editbrand": brand_to_edit, "allBrands": all_brands ,"allCategories": all_categories, "allCountries": all_countries}

        return render(request, "sb-admin/cards.html", context)

    if request.method == "POST":
        try:
            changed_name = request.POST.get("brandName", None)
            logo_url = request.POST.get("logoUrl", None)
            category_string = request.POST.get("category", None)
            changed_country = request.POST.get("originCountry", None)
            changed_description = request.POST.get("brandDescription", None)
            parent_brand_string = request.POST.get("parentBrand", None)
            expected_country = Country.objects.get(name=changed_country)
            category = Category.objects.get(name=category_string)
            if parent_brand_string != "None":
                parent_brand = Brand.objects.get(id=parent_brand_string)
                Brand.objects.filter(id=brand_id).update(name=changed_name, origin_country=expected_country, logo=logo_url,
                                                         description=str(changed_description), category=category,
                                                         edited=True,
                                                         parent=parent_brand)
            else:
                Brand.objects.filter(id=brand_id).update(name=changed_name, origin_country=expected_country,
                                                         logo=logo_url,
                                                         description=str(changed_description), category=category,
                                                         edited=True)
            messages.warning(request, "Edit Complete")
        except Exception as e:
            messages.error(request, str(e))
        return redirect("main:index")


def finalise_brand(request, brand_id):
    if request.method == "POST":
        try:
            expected_brand = Brand.objects.get(id=brand_id)
            expected_brand.finalise = True
            expected_brand.save()
            messages.success(request, "Finalisation successful")
        except Exception as e:
            messages.error(request, str(e))
    return redirect("main:index")
