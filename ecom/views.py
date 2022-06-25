from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import CheckFrm, CustomerRegistrationForm, CustomerProfileForm, PortfolioCheckoutForm
from django.contrib import messages
from django.views import View



def home_view(request):
    general_portfolio_price = PortfolioPricing.objects.filter(category='general')
    premium_portfolio_price = PortfolioPricing.objects.filter(category='premium')
    #form = DomainForm()
    #     last_blog = Blog.object.all.order_by('-id')[0]
#     blogs = Blog.object.all().order_by('-id')[1:4]


    context ={ 'general_portfolio_price':general_portfolio_price, 
    'premium_portfolio_price':premium_portfolio_price}

    return render(request, 'ecom/index.html', context)


def pricing_plan(request):
    general_portfolio_price = PortfolioPricing.objects.filter(category='general')
    premium_portfolio_price = PortfolioPricing.objects.filter(category='premium')
    context ={ 'general_portfolio_price':general_portfolio_price, 
    'premium_portfolio_price':premium_portfolio_price}

    return render(request, 'ecom/pricing.html', context)


class PricingtoTheme(View):
    def get(self, request, pk):
        pricing = PortfolioPricing.objects.get(pk=pk)
        themes = PortfolioTheme.objects.all()
        context = {'pricing':pricing, 'themes':themes}
        return render(request, 'ecom/pricing_to_theme.html', context)


class ThemetoPricing(View):
    def get(self, request, pk):
        theme = PortfolioTheme.objects.get(pk=pk)
        pricing = PortfolioPricing.objects.filter(category='general')
        context = {'theme':theme, 'pricings':pricing}
        return render(request, 'ecom/theme_to_pricing.html', context)


def check_frm(request):
    user = request.user
    # address = Customer.objects.filter(user=user)
    frm = CheckFrm()
    context = {'frm': frm}
    return render(request, 'ecom/frm_check.html', context)



def portfolio_checkout(request):
    user = request.user

    if request.method == 'POST':
        custid = request.POST['custid']
        customer = Customer.objects.get(id=custid)
        pricing_id = request.POST['pricing_id']
        pricing = PortfolioPricing.objects.get(id=pricing_id)
        theme_id = request.POST['theme_id']
        theme = PortfolioTheme.objects.get(id=theme_id)
        fm = PortfolioCheckoutForm(request.POST)
        if fm.is_valid():
            domain_name = fm.cleaned_data['doamain_name']
            buy_domain = fm.cleaned_data['buy_doamin']
            order = OrderPortfolio(user=user, customer=customer, theme=theme, price=pricing, 
            domain_name=domain_name, buy_domain=buy_domain)
            order.save()
            return redirect("check_order")


    else:
        pricing_id = request.GET.get('pricing_id')
        pricing = PortfolioPricing.objects.get(id=pricing_id)
        theme_id = request.GET.get('theme_id')
        theme = PortfolioTheme.objects.get(id=theme_id)
        address = Customer.objects.filter(user=user)
        frm = PortfolioCheckoutForm()
        context ={'theme': theme, 'pricing':pricing, 'address':address, 'frm':frm}
        return render(request, 'ecom/portfolio_checkout.html', context)


# def portfolio_checkout_complete(request):
#     user = request.user
#     custid = request.GET.get('custid')
#     customer = Customer.objects.get(id=custid)
#     pricing_id = request.GET.get('pricing_id')
#     pricing = PortfolioPricing.objects.get(id=pricing_id)
#     theme_id = request.GET.get('theme_id')
#     theme = PortfolioTheme.objects.get(id=theme_id)
#     OrderPortfolio(user=user, customer=customer, theme=theme, price=pricing, ).save()
#     return redirect("check_order")

def check_order(request):
    order_placed = OrderPortfolio.objects.filter(user=request.user)
    return render(request, 'ecom/check_order.html', {'order_placed':order_placed})


def contact_view(request):
    return render(request, 'ecom/contact_us.html', {})

def about_view(request):
    return render(request, 'ecom/about_us.html', {})

def service_web_view(request):
    themes = PortfolioTheme.objects.all()
    return render(request, 'ecom/service_web.html', {'themes':themes})




class AddProfile(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'ecom/add_profile.html', {'form':form})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            delivary_mail = form.cleaned_data['delivary_mail']
            reg = Customer(user=usr, name=name, delivary_mail=delivary_mail, country=country)
            reg.save()
            messages.success(request, 'Congratulations!! your profile updated successfully.')
        return render(request, 'ecom/add_profile.html', {'form':form})



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'ecom/customer_registration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered Successfully, Please login")
            form.save()
        return render(request, 'ecom/customer_registration.html', {'form':form})
