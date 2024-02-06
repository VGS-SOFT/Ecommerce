from ..schemes import pydenticfieldconversion
from ..modal.CatMast import  DeleteCatMaster, insertdata, UpdateMastCat
import json
from django.shortcuts import render
from django.http import JsonResponse
from ..response import ResponseObj
from django.contrib.auth.decorators import login_required


# Render The Page
# @login_required(login_url='/accounts/login')
def CATEGORYMASTER(request):
    return render(request, 'CatMaster/CatMaster.html')


# Render the data for table
# @login_required(login_url='/accounts/login')
def GETDATAODCATMASTER(request):
    rows = pydenticfieldconversion()
    response_data = []
    for row in rows:
        response_data.append({
            'CatId': row.CatId,
            'CatName': row.CatName,
        })
    return JsonResponse(response_data, safe=False)


# Add the data
# @login_required(login_url='/accounts/login')
def ADDDATACATMASTER(request):
    if request.method == "POST":
        name = request.POST.get('catmastername')
        # json_data = json.loads(str(request.body, encoding='utf-8'))
        # name = (json_data['new_data'])
        insertdata(name)
        response_instance = ResponseObj(response_status=True,
                                        response_message="Success",
                                        response_obj={'key': 'value'})
        json_object = response_instance.to_dict()
        return JsonResponse(json_object)


# Edit Data
# @login_required(login_url='/accounts/login')
def EDITMASTCAT(request):
    if request.method == "POST":
        json_data = json.loads(str(request.body, encoding='utf-8'))
        id = (json_data['id'])
        name = (json_data['new_data'])
        UpdateMastCat(name, id)
        response_instance = ResponseObj(response_status=True,
                                        response_message="Success",
                                        response_obj={'key': 'value'})
        json_object = response_instance.to_dict()
        return JsonResponse(json_object)    


# Delete the Data
# @login_required(login_url='/accounts/login')
def DELETECATMASTERDATA(request, id):
    if request.method == 'POST':
        DeleteCatMaster(id)
        response_instance = ResponseObj(response_status=True,
                                        response_message="Success",
                                        response_obj={'key': 'value'})
        json_object = response_instance.to_dict()
        return JsonResponse(json_object)
