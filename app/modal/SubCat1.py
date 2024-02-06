from ..models import ConnectionWithDb

class pydenticforsubcat1:
    id: int
    name: str
    refid: int

def insertdatintosubcat1(mainid, name, id):
    curses = ConnectionWithDb()
    curses.execute(f"EXEC prc_SaveSubCategory1 {mainid},'{name}', {id}")
    curses.commit()


def getalldatafromsubcat1():
    cursor = ConnectionWithDb()
    cursor.execute('EXEC prc_GetAllDataSubCat1')
    rows = cursor.fetchall()
    return rows


def insertdatintosubcat2(name, id):
    curses = ConnectionWithDb()
    curses.execute(f"EXEC prc_SaveSubCategory2 '{name}', {id}")
    curses.commit()


def DeleteSubCat1(id):
    cursor = ConnectionWithDb()
    cursor.execute(f"EXEC DeleteSubCat1 {id}")
    cursor.commit()