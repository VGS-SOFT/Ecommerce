from django.shortcuts import render, redirect
from ..modal.SubCat1 import insertdatintosubcat1, getalldatafromsubcat1, DeleteSubCat1
from ..modal.CatMast import getalldata
from django.http import JsonResponse
from ..response import ResponseObj
from django.contrib.auth.decorators import login_required


# Render the page with data
# @login_required(login_url='/accounts/login')
def SUBCAT1(request):
    return render(request, 'SubCat1/SubCat1.html')


# Add new data
# @login_required(login_url='/accounts/login')
def ADDSUBCAT1(request):
    if request.method == 'POST':
        mainid = request.POST.get('valifid')
        idofmastclass = request.POST.get('idofmastclass')
        SubCatName1 = request.POST.get('SubCatName1')
        print('mainid: ',mainid,'idodmasterclass: ',idofmastclass,'name: ',SubCatName1)
        # insertdatintosubcat1(mainid,SubCatName1, idofmastclass)
        response = JsonResponse({'ResponseStatus': True}, safe=False)
        return response
    return render(request, 'product/SubCat1.html')


# Get Data
# @login_required(login_url='/accounts/login')
def GETALLDATA(request):
    rows = getalldatafromsubcat1()
    response_data = []
    for row in rows:
        response_data.append({
            'id': row.SubCatId1,
            'name': row.SubCatName1,
            'ref':row.RefCatIdMast
        })
    return JsonResponse(response_data, safe=False)

# Delete Data
# @login_required(login_url='/accounts/login')
def DeletedataSubCat1(request,id):
    print(id)
    DeleteSubCat1(id)
    response_instance = ResponseObj(response_status=True,
                                    response_message="Success",
                                    response_obj={'key': 'value'})
    json_object = response_instance.to_dict()
    return JsonResponse(json_object)