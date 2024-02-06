# from django.db import models
from django.db import models
import pyodbc as odbc
from pydantic import BaseModel
import os


def ConnectionWithDb():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'VGS-1\SQLEXPRESS'
    DATABASE_NAME = 'Ecommerce'
    # DATABASE_NAME = 'test'
    connection_string = f"""DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;"""

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    return cursor


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File deleted successfully: {file_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")


def GetImgPath(id):
    cursor = ConnectionWithDb()
    query = "EXEC GetImgPath @id = ?"
    cursor.execute(query, id)
    row = cursor.fetchone()
    cursor.commit()
    return row[0]


class Aboutus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='Title', max_length=500,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(
        db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(
        db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AboutUs'


class Appsettings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    settingkey = models.CharField(
        db_column='SettingKey', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    settingvalue = models.TextField(
        db_column='SettingValue', db_collation='SQL_Latin1_General_CP1_CI_AS')
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(
        db_column='ModifiedBy', blank=True, null=True)
    communityid = models.IntegerField(
        db_column='CommunityID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppSettings'


class Brandmaster(models.Model):
    brandid = models.AutoField(db_column='BrandId', primary_key=True)
    brandname = models.CharField(db_column='BrandName', max_length=250,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BrandMaster'


class CategoryMaster(models.Model):
    catid = models.AutoField(db_column='CatId', primary_key=True)
    catname = models.CharField(db_column='CatName', max_length=150,
                               db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category_Master'


class Loginhistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.IntegerField(db_column='UserID')
    ipaddress = models.CharField(
        db_column='IPAddress', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    createddate = models.DateTimeField(db_column='CreatedDate')

    class Meta:
        managed = False
        db_table = 'LoginHistory'


class Productdescription(models.Model):
    proddescid = models.AutoField(db_column='ProdDescId', primary_key=True)
    description = models.CharField(db_column='Description', max_length=500,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    refproductid = models.IntegerField(
        db_column='RefProductId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductDescription'


class Productdetails(models.Model):
    pid = models.AutoField(db_column='PId', primary_key=True)
    productcode = models.CharField(db_column='ProductCode', max_length=150,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pname = models.CharField(db_column='PName', max_length=250,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    productdetail = models.CharField(db_column='ProductDetail', max_length=300,
                                     db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    price = models.IntegerField(db_column='Price', blank=True, null=True)
    discountprice = models.IntegerField(
        db_column='DiscountPrice', blank=True, null=True)
    discountpercentage = models.IntegerField(
        db_column='DiscountPercentage', blank=True, null=True)
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)
    productimgpath = models.CharField(db_column='ProductImgPath', max_length=500,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    PRODUCTIMAGE = models.ImageField(upload_to='media')
    sizesqty = models.IntegerField(db_column='SizeSQty', blank=True, null=True)
    sizemqty = models.IntegerField(db_column='SizeMQty', blank=True, null=True)
    sizelqty = models.IntegerField(db_column='SizeLQty', blank=True, null=True)
    sizexlqty = models.IntegerField(
        db_column='SizeXLQty', blank=True, null=True)
    sizexxlqty = models.IntegerField(
        db_column='SizeXXLQty', blank=True, null=True)
    size3xlqty = models.IntegerField(
        db_column='Size3XLQty', blank=True, null=True)
    refsubcat2id = models.ForeignKey(
        'Subcategories2', models.DO_NOTHING, db_column='RefSubCat2Id', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    createdon = models.DateTimeField(
        db_column='CreatedOn', blank=True, null=True)
    modifyedby = models.IntegerField(
        db_column='ModifyedBy', blank=True, null=True)
    modifyedon = models.DateTimeField(
        db_column='ModifyedOn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductDetails'


class Productimagemaster(models.Model):
    prodimgid = models.AutoField(db_column='ProdImgId', primary_key=True)
    refproductid = models.IntegerField(
        db_column='RefProductId', blank=True, null=True)
    imgorder = models.IntegerField(db_column='ImgOrder', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    createdon = models.DateTimeField(
        db_column='CreatedOn', blank=True, null=True)
    modifyedby = models.IntegerField(
        db_column='ModifyedBy', blank=True, null=True)
    modifyedon = models.DateTimeField(
        db_column='ModifyedOn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductImageMaster'


class Rating(models.Model):
    ratingid = models.AutoField(db_column='RatingId', primary_key=True)
    rating = models.DecimalField(
        db_column='Rating', max_digits=7, decimal_places=2, blank=True, null=True)
    refuserid = models.IntegerField(
        db_column='RefUserId', blank=True, null=True)
    refproductid = models.IntegerField(
        db_column='RefProductId', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    createdon = models.DateTimeField(
        db_column='CreatedOn', blank=True, null=True)
    modifyedby = models.IntegerField(
        db_column='ModifyedBy', blank=True, null=True)
    modifyedon = models.DateTimeField(
        db_column='ModifyedOn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rating'


class Role(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isactive = models.BooleanField(db_column='IsActive')
    createddate = models.DateTimeField(db_column='CreatedDate')
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(
        db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Role'


class Subcategories1(models.Model):
    subcatid1 = models.AutoField(db_column='SubCatId1', primary_key=True)
    subcatname1 = models.CharField(db_column='SubCatName1', max_length=250,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    refcatidmast = models.ForeignKey(
        CategoryMaster, models.DO_NOTHING, db_column='RefCatIdMast', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SubCategories1'


class Subcategories2(models.Model):
    subcatid2 = models.AutoField(db_column='SubCatId2', primary_key=True)
    subcatname2 = models.CharField(db_column='SubCatName2', max_length=250,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    refsubcat1id = models.ForeignKey(
        Subcategories1, models.DO_NOTHING, db_column='RefSubCat1Id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SubCategories2'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=150,
                            db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(
        db_column='Email', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(db_column='Password', max_length=500,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=20,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    profilepicture = models.TextField(
        db_column='ProfilePicture', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isactive = models.BooleanField(db_column='IsActive')
    isdeleted = models.BooleanField(
        db_column='IsDeleted', blank=True, null=True)
    lastlogindate = models.DateTimeField(
        db_column='LastLoginDate', blank=True, null=True)
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(
        db_column='ModifiedBy', blank=True, null=True)
    resetcode = models.CharField(db_column='ResetCode', max_length=6,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Userinrole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.IntegerField(db_column='UserID')
    roleid = models.IntegerField(db_column='RoleID')
    createddate = models.DateTimeField(db_column='CreatedDate')
    createdby = models.IntegerField(
        db_column='CreatedBy', blank=True, null=True)
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)
    modifiedby = models.IntegerField(
        db_column='ModifiedBy', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInRole'
