from ..models import ConnectionWithDb


def getalldata():
    cursor = ConnectionWithDb()
    cursor.execute('EXEC prc_GetAllDataCatMaster')
    rows = cursor.fetchall()
    return rows


def insertdata(name):
    cursor = ConnectionWithDb()
    sql_query = f"EXEC prc_SaveCategoryMasterData @CatName = ?"
    cursor.execute(sql_query, (name,))
    cursor.commit()


def UpdateMastCat(new_data, id):
    cursor = ConnectionWithDb()
    cursor.execute(f"EXEC [dbo].[UpCatMast] @name = ?,@id = ?", (new_data, id))
    cursor.commit()


def DeleteCatMaster(id):
    cursor = ConnectionWithDb()
    cursor.execute(f"EXEC DeleteCatMaster {id}")
    cursor.commit()
