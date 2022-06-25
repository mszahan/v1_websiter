from django.urls import path
from ecom import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ChangePasswordForm, ResetPasswordForm, ConfirmPasswordForm

urlpatterns = [

    path('', views.home_view, name='home_page'),
    path('contact/', views.contact_view, name='contact_us'),
    path('check-frm/', views.check_frm, name='check_frm'),
    path('about/', views.about_view, name='about_us'),
    path('service-web/', views.service_web_view, name='service_web'),
    path('pricing-plan/', views.pricing_plan, name='pricing_plan'),


    path('pricing-theme/<int:pk>', views.PricingtoTheme.as_view(), name='price_to_theme'),
    path('theme-pricing/<int:pk>', views.ThemetoPricing.as_view(), name='theme_to_pricing'),
    path('portfolio/checkout', views.portfolio_checkout, name='portfolio_checkout'),
    # path('portfolio/checkout/complete', views.portfolio_checkout_complete, name='Portfolio_checkout_complete'),
    path('check-order', views.check_order, name='check_order'),


    path('add-profile/', views.AddProfile.as_view(), name='add_profile'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='ecom/login.html', 
    authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #change password urls next two urls change_passwor and done_password
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='ecom/change_password.html', 
    form_class=ChangePasswordForm, success_url='/done-password/'), name='change_password'),

    path('done-password/', auth_views.PasswordChangeDoneView.as_view(template_name='ecom/done_password.html'),
    name=('done_password')),



    #next password urls are for forgot password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='ecom/password_reset.html',
    form_class=ResetPasswordForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='ecom/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='ecom/password_reset_confirm.html',
    form_class=ConfirmPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='ecom/password_reset_complete.html'),
    name='password_reset_complete'),



]
 
    