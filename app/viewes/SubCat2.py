from django.http import JsonResponse
from django.shortcuts import render, redirect
from ..modal.SubCat2 import insertdatintosubcat2, getalldatafromsubcat2, DeleteSubCat2
from ..response import ResponseObj
from django.contrib.auth.decorators import login_required


# Render page with data
# @login_required(login_url='/accounts/login')
def SUBCAT2(request):
    return render(request, 'SubCat2/SubCat2.html')


# Add New Data
# @login_required(login_url='/accounts/login')
def ADDSUBCAT2(request):
    if request.method == 'POST':
        subcat1 = int(request.POST.get('idofmastclass'))
        SubCatName1 = request.POST.get('SubCatName1')
        # print(type(subcat1),'=====>',subcat1)
        # print(type(SubCatName1),'=====>',SubCatName1)
        insertdatintosubcat2(SubCatName1, subcat1)
        response_instance = ResponseObj(response_status=True,
                                        response_message="Success",
                                        response_obj={'key': 'value'})
        json_object = response_instance.to_dict()
        return JsonResponse(json_object)



# Get All Data From Sub Cat 2
# @login_required(login_url='/accounts/login')
def GetTheData(request):
    rows = getalldatafromsubcat2()
    data = []
    for row in rows:
        data.append({
            'id': row.SubCatId2,
            'name': row.SubCatName2,
            'ref': row.RefSubCat1Id
        })
    return JsonResponse(data, safe=False)

# @login_required(login_url='/accounts/login')
def DeletedataSubCat2(request, id):
    print(id)
    DeleteSubCat2(id)
    response_instance = ResponseObj(response_status=True,
                                    response_message="Success",
                                    response_obj={'key': 'value'})
    json_object = response_instance.to_dict()
    return JsonResponse(json_object)
