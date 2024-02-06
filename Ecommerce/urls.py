"""
Definition of urls for Ecommerce.
"""

from django.urls import path, include
from django.contrib import admin
from app import views
from app.viewes import CategoryMaster,SubCat1,SubCat2,product,users 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

urlpatterns = [

    # Auth
    # path("", TemplateView.as_view(template_na me="home.html"), name="home"),
    path("", include("accounts.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),

    # General
    # path('',)
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('getimg/<int:id>',views.imagetry,name='imagetry'),

    # Category Master
    path('catmaster', CategoryMaster.CATEGORYMASTER, name='catmaster'),
    path('getallcatmaster', CategoryMaster.GETDATAODCATMASTER, name='getallcatmast'),
    path('addcatmaster',CategoryMaster.ADDDATACATMASTER, name='addcatmaster'),
    path('updatecategory', CategoryMaster.EDITMASTCAT, name='editmastcat'),
    path('deletecatmaster/<int:id>',CategoryMaster.DELETECATMASTERDATA,name='deletecatmasterdata'),

    # Sub Category 1
    path('subcat1', SubCat1.SUBCAT1, name='subcat1'),
    path('addsubcat1', SubCat1.ADDSUBCAT1, name='addsubcat1'),
    path('getalldata',SubCat1.GETALLDATA,name='getthedata'),
    path('deletesubcat1/<int:id>',SubCat1.DeletedataSubCat1,name='deletesubcat1'),

    # Sub Cateory 2
    path('subcat2', SubCat2.SUBCAT2, name='subcat2'),
    path('addsubcat2', SubCat2.ADDSUBCAT2, name='addsubcat2'),
    path('getsubcat2',SubCat2.GetTheData,name='getsubcat2'),
    path('deletesubcat2/<int:id>',SubCat2.DeletedataSubCat2,name='deletesubcat2'),

    # Products
    path('product', product.GETALLPRODUCT, name='getallproduct'),
    path('newproduct', product.ADDNEWPRODUCT, name='addnewproduct'),
    path('productpage',product.PRODUCTPAGE,name='productpage'),
    path('deleteproduct/<int:id>',product.DELETEPRODUCT, name='deleteproduct'),
    # path('updateproduct',product.ADDNEWPRODUCT,name='updateproduct')
    # path('setimg/<int:id>',product.getimgandset, name='getimgandset'),

    # Users
    path('getusers',users.GETALLUSERS, name='getallusers'),

]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
