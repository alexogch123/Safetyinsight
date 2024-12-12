from django.urls import path
from .views import OrganizationView, OrganizationNew, OrganizationEdit, OrganizationDelete

urlpatterns = [
    path('company/', OrganizationView.as_view(), name='company_list'),
    path('company/new', OrganizationNew.as_view(), name='company_new'),
    path('company/edit/<int:pk>', OrganizationEdit.as_view(), name='company_edit'),
    path('company/delete/<int:pk>', OrganizationDelete.as_view(), name='company_delete'),
]