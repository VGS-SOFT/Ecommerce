from django.http import JsonResponse
from ..modal.users import GetAllUsers
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/accounts/login')
def GETALLUSERS(request):
    rows = GetAllUsers()
    data = []
    for row in rows:
        data.append({
            'id': row.ID,
            'name': row.Name
        })
    return JsonResponse(data, safe=False)