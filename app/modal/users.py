from ..models import ConnectionWithDb


def GetAllUsers():
    cursor = ConnectionWithDb()
    cursor.execute('EXEC [dbo].[GetExistingUser]')
    rows = cursor.fetchall()
    return rows
