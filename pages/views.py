from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import validate_company_create
from django.core.exceptions import ValidationError
from accounts.models import Company, Category, Stage
from django.core.paginator import Paginator


class HomePageView(TemplateView):
    template_name = "pages/index.html"


@login_required
def profile(request):
    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        request.user.name = name
        request.user.save()
        return redirect('pages:profile')

    return render(request, 'pages/profile.html', {'error': error})


@login_required
def company_list(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 10)  # Show 10 companies per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/company_list.html', {'page_obj': page_obj})


@login_required
def company_create(request):
    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        logo = request.FILES.get('logo')
        category = request.POST.getlist('category')
        stage = request.POST.getlist('stage')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        try:
            validate_company_create(name, url, logo, category, stage, address, city, state, zip, country, phone)
        except ValidationError as e:
            error = str(e)
        else:
            # First create the company without the categories
            company = Company.objects.create(name=name, url=url, logo=logo, address=address, city=city, state=state, zip=zip, country=country, phone=phone, creator=request.user)

            # Then add the categories
            for cat_name in category:
                # Fetch the Category instance for this name
                cat = Category.objects.get(name=cat_name.lower())
                # Add the category to the company
                company.category.add(cat)
                
            # Then add the stage
            for stage_name in stage:
                # Fetch the stage instance for this name
                stag = Stage.objects.get(name=stage_name.lower())
                # Add the stage to the company
                company.stage.add(stag)

            # Redirect to the company list page
            return redirect('pages:company_list')


    return render(request, 'pages/company_create.html', {'error': error})


def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'pages/company_detail.html', {'company': company})