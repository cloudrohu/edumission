from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.utils.translation import gettext_lazy as _

from django.views.generic import RedirectView
urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('logout/',RedirectView.as_view(url = '/admin/logout/')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('contactus/', views.contactus, name='contactus'),  # existing ✅
    path('contactus/submit/', views.submit_form, name='submit_form'),  # 👈 NEW ✅
    path(('faqs/'), views.faqs, name='faqs'),
    path(('product/'), views.product, name='product'),
    path(('brand/'), views.BRAND, name='brand'),
    path(('gallery/'), views.Gallery, name='gallery'),

    path(('about/'), views.aboutus, name='aboutus'),
    path(('our-team/'), views.Our_Team, name='our-team'),
    path(('vision-mission/'), views.Vision_Mission, name='vision-mission'),
    path(('director-desk/'), views.DirectorDesk, name='director-desk'),


    path(('architecture/'), views.Architecture, name='architecture'),
    path(('construction/'), views.Construction, name='construction'),
    path(('interior/'), views.Interior, name='interior'),
    path(('landscape/'), views.Landscape, name='landscape'),
    path(('turnkey/'), views.Turnkey, name='turnkey'),


    path(('blog/'), views.BLOG, name='blog'),
    path(('real-estate/'), views.REALESTATE, name='real-estate'),

    path(('product/'), views.product, name='product'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),

    path(('complate_project/'), views.Complate_project, name='complate_project'),
    path(('ongoing_project/'), views.Ongoing_project, name='ongoing_project'),
    path(('upcoming_project/'), views.Upcoming_project, name='Upcoming_project'),
    path('project_details/<slug:slug>', views.project_details, name='project_details'),

    path(('service/'), views.service, name='service'),
    path('service_details/<slug:slug>', views.service_details, name='service_details'),

    path('thank_you/', views.THANK_YOU, name='thank_you'),
    path('consultation/success/', views.consultation_success, name='consultation_success'),
    path('privacy_policy/', views.Privacy_Policy, name='privacy_policy'),
    path('cookies/', views.Cookies, name='cookies'),
    path('terms_and_condition/', views.Terms_and_condition, name='terms_and_condition'),
    path('enquiry/', views.contact_enquiry, name='enquiry'),




                                                                                                                                                                                                 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
