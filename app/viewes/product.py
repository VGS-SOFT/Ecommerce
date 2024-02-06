# from app.models import insertnewproduct, DeleteProduct
from ..modal.product import insertnewproduct, DeleteProduct, getallproduct, SetImage
import shutil
from django.shortcuts import render
from datetime import datetime
from app.modal.product import getallproduct
from django.http import JsonResponse
from ..response import ResponseObj
from django.core.files.storage import default_storage, FileSystemStorage
from ..models import GetImgPath
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Render The Page
# @login_required(login_url='/accounts/login')
def PRODUCTPAGE(request):
    return render(request, 'product/product.html')


# Get All Produc
# @login_required(login_url='/accounts/login')
def GETALLPRODUCT(REQUEST):
    rows = getallproduct(id=0)
    response_data = []
    for row in rows:
        response_data.append({
            'PId': row.PId,
            'ProductCode': row.ProductCode,
            'PName': row.PName,
            'Price': row.Price,
            'ProductDetails': row.ProductDetail,
            'DiscountPrice': row.DiscountPrice,
            'DiscountPercentage': row.DiscountPercentage,
            'Rating': row.Rating,
            'ProductImgPath': row.ProductImgPath,
            'SizeSQty': row.SizeSQty,
            'SizeMQty': row.SizeSQty,
            'SizeLQty': row.SizeLQty,
            'SizeXLQty': row.SizeXLQty,
            'SizeXXLQty': row.SizeXXLQty,
            'Size3XLQty': row.Size3XLQty,
            'Category': row.RefSubCat2Id,
            'CreatedBy': row.CreatedBy,
            'CreatedOn': row.CreatedOn,
            'ModifiedBy': row.ModifyedBy,
            'ModifyedOn': row.ModifyedOn,
        })
    return JsonResponse(response_data, safe=False)


# FileValue = []

# @login_required(login_url='/accounts/login')
def ADDNEWPRODUCT(request):
    if request.method == 'POST':
        PId = request.POST.get('PId')
        PId = int(PId)
        rows = getallproduct(id=PId)
        print(rows)
        product_code = request.POST.get('product_code')
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_detail = request.POST.get('product_detail')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount_percentage')
        discount_price = request.POST.get('discount_price')
        size_s_qty = request.POST.get('s')
        size_m_qty = request.POST.get('m')
        size_l_qty = request.POST.get('l')
        size_xl_qty = request.POST.get('xl')
        size_xxl_qty = request.POST.get('xxl')
        size_3xl_qty = request.POST.get('3xl')
        subcat2 = request.POST.get('subcat2')
        rating = 1
        User = 1
        created_on = datetime.now()
        images = request.FILES.getlist('path')
        # for image in images:
        #     FileValue.append(image)
        ModifyedOn = datetime.now()
        ModifyedOn = None
        # print(product_code, product_name, product_description, product_detail, price, discount_percentage,
        #       discount_price, size_s_qty, size_m_qty, size_l_qty, size_xl_qty, size_xxl_qty, size_3xl_qty, subcat2, created_on, ModifyedOn, rating, User)

        # print(FileValue)
        # FileValue.clear()     
        result = insertnewproduct(
            PId=PId,
            ProductCode=product_code,
            ProductName=product_name,
            ProductDetail=product_detail,
            Price=price,
            DiscountPrice=discount_price,
            DiscountPercentage=discount_percentage,
            Rating=rating,
            ProductImgPath=None,
            S=size_s_qty,
            M=size_m_qty,
            L=size_l_qty,
            XL=size_xl_qty,
            XXL=size_xxl_qty,
            XXXL=size_3xl_qty,
            RefSubCat2Id=subcat2,
            CreatedBy=User,
            ModifyedBy=None,
            ModifyedOn=ModifyedOn,
            CreatedOn=created_on
        )
        id = str(result)
        if PId > 0 and (images == "" or images == None):
            image_urls = None
            # image_urls = [default_img[0]]
        else:
            image_urls = ''
            product_folder_path = os.path.join(settings.MEDIA_ROOT, id)
            if product_folder_path != "":
                os.makedirs(product_folder_path, exist_ok=True)
            for image in images:
                image_path = os.path.join(product_folder_path, image.name)
                with open(image_path, 'wb') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                image_url = os.path.join(settings.MEDIA_URL, id, image.name).replace('\\', '/')
                image_urls += image_url+','
        if (image_urls):
            SetImage(image_urls, id)
        response_data = {'ResponseStauts': True,
                         'message': 'Data received successfully'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'ResponseStauts': False, 'message': 'Invalid HTTP method'})


# Delete Product
# @login_required(login_url='/accounts/login')
def DELETEPRODUCT(request, id):
    base_path = "media"
    dir_path = os.path.join(base_path, str(id))
    shutil.rmtree(dir_path)
    DeleteProduct(id)
    response_instance = ResponseObj(response_status=True,
                                    response_message="Success",
                                    response_obj={'key': 'value'})
    json_object = response_instance.to_dict()
    return JsonResponse(json_object)
