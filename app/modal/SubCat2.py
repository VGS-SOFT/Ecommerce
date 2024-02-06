from ..models import ConnectionWithDb


def getalldatafromsubcat2():
    cursor = ConnectionWithDb()
    cursor.execute(f'EXEC [prc_GetAllDataSubCat2] {0}')
    rows = cursor.fetchall()
    return rows

def insertdatintosubcat2(name, id):
    curses = ConnectionWithDb()
    curses.execute(f"EXEC prc_SaveSubCategory2 '{name}', {id}")
    curses.commit()

# def getallsubcat2data(id):
#     cursor = ConnectionWithDb()
#     cursor.execute(f'EXEC [dbo].[prc_GetAllDataSubCat2] {id}')
#     cursor.commit()
    

def DeleteSubCat2(id):
    cursor = ConnectionWithDb()
    cursor.execute(f'EXEC DeleteSubCat2 {id}')
    cursor.commit()