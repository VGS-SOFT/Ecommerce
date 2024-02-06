from .models import ConnectionWithDb
from pydantic import BaseModel

class SchemaForMasterCat(BaseModel):
    CatId: int
    CatName: str

def pydenticfieldconversion():
    cursor = ConnectionWithDb()
    cursor.execute('EXEC [dbo].[prc_GetAllDataCatMaster]')
    rows = cursor.fetchall()
    empty_lst = []
    for row in rows:
        PydenticResponse = SchemaForMasterCat(CatId=row[0], CatName=row[1])
        empty_lst.append(PydenticResponse)
    return empty_lst
