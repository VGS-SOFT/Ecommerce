from app.models import ConnectionWithDb
import pyodbc as odbc


def getallproduct(id):
    cursor = ConnectionWithDb()
    cursor.execute(f"EXEC [dbo].[GetProductDetails] {id}")
    rows = cursor.fetchall()
    return rows


def DeleteProduct(id):
    cursor = ConnectionWithDb()
    query = 'EXEC [dbo].[DeleteProduct] @id = ?'
    cursor.execute(query, (id,))
    cursor.commit()


def SetImage(image,id):
    cursor = ConnectionWithDb()
    try:
        query = """
        EXEC [dbo].[InsertImage] @img=?, @id=?
        """
        cursor.execute(query,(image,id))
        cursor.commit()
    except Exception as es:
        print(es)

        
def insertnewproduct(PId, ProductCode, ProductName, ProductDetail, Price, DiscountPrice, DiscountPercentage, Rating,
                     ProductImgPath, S, M, L, XL, XXL, XXXL, RefSubCat2Id, CreatedBy, ModifyedBy, ModifyedOn, CreatedOn):
    cursor = ConnectionWithDb()
    try:        
        query = """
                DECLARE @InsertedID INT;  -- Declare OUTPUT parameter
                EXEC [dbo].[UpSetProductDetails]
                    @PId = ?,
                    @ProductCode = ?,
                    @PName = ?,
                    @ProductDetail = ?,
                    @Price = ?,
                    @DiscountPrice = ?,
                    @DiscountPercentage = ?,
                    @Rating = ?,
                    @ProductImgPath = ?,
                    @SizeSQty = ?,
                    @SizeMQty = ?,
                    @SizeLQty = ?,
                    @SizeXLQty = ?,
                    @SizeXXLQty = ?,
                    @Size3XLQty = ?,
                    @RefSubCat2Id = ?,
                    @CreatedBy = ?,
                    @ModifyedBy = ?,
                    @ModifyedOn = ?,
                    @CreatedOn = ?,
                    @InsertedID = @InsertedID OUTPUT;  -- Assign value to OUTPUT parameter
                SELECT @InsertedID AS 'InsertedID';  -- Return the OUTPUT parameter value
        """
        cursor.execute(query, (
            int(PId), ProductCode, ProductName, ProductDetail, int(Price), float(DiscountPrice), int(DiscountPercentage),
            int(Rating), ProductImgPath, int(S), int(M), int(L), int(XL), int(XXL), int(XXXL), int(RefSubCat2Id),
            int(CreatedBy), ModifyedBy, ModifyedOn, CreatedOn))

        # print("***************")
        # print(query, (
        #     int(PId), ProductCode, ProductName, ProductDetail, int(Price), float(DiscountPrice), int(DiscountPercentage),
        #     int(Rating), ProductImgPath, int(S), int(M), int(L), int(XL), int(XXL), int(XXXL), int(RefSubCat2Id),
        #     int(CreatedBy), ModifyedBy, ModifyedOn, CreatedOn))
        # print("***************")

        rows = cursor.fetchone()
        cursor.commit()
        return rows[0]
    
    except Exception as e:
        # print("$$$$$$$$$$$$$$$$$$$$$")
        print(e)
