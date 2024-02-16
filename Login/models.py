from django.db import models

# Create your models here.
class tbl_login(models.Model):
    username=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=30,null=True)
    dt=models.DateField(auto_now_add=True,null=True)
    tm=models.TimeField(auto_now_add=True,null=True)


class tbl_basic_info_cmp(models.Model):
    cin=models.CharField(max_length=50,null=True)
    CompanyName=models.CharField(max_length=50,null=True)
    reg_no=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=500,null=True)
    mobile1=models.CharField(max_length=50,null=True)
    mobile2=models.CharField(max_length=50,null=True)
    email1=models.EmailField(null=True)
    email2=models.EmailField(null=True)
    date_incorporation=models.DateField(null=True)
    roc=models.CharField(max_length=50,null=True)
    gstin=models.CharField(max_length=50,null=True)
    website=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=50,null=True)
    sub_category=models.CharField(max_length=50,null=True)
    class_company=models.CharField(max_length=50,null=True)
    start_date=models.DateField(null=True)
    activity=models.CharField(max_length=500,null=True)
    age_company=models.CharField(max_length=50,null=True)
    total_members=models.IntegerField(null=True)
    logo=models.ImageField(upload_to="pictures",null=True)


class tbl_bank_info(models.Model):
    bank_name=models.CharField(max_length=100,null=True)
    branch_name=models.CharField(max_length=100,null=True)
    address=models.TextField(null=True)
    account_no=models.CharField(max_length=100,null=True)
    ifsc_code=models.CharField(max_length=100,null=True)
    bank_open_balance=models.CharField(max_length=50,null=True)
    dt=models.DateField(auto_now_add=True,null=True)
    status=models.BooleanField(null=True,default=True)

class tbl_licenses(models.Model):
    license_name=models.CharField(max_length=100,null=True)
    license_number=models.CharField(max_length=100,null=True)
    expiry_reminder=models.DateField(null=True)
    expiry_date=models.DateField(null=True)
    license_file=models.ImageField(upload_to="license",null=True)
    status=models.BooleanField(default=True,null=True)
    dt=models.DateField(auto_now_add=True)


class tbl_Director(models.Model):
    director_name = models.CharField(max_length=100, null=True)
    director_designation = models.CharField(max_length=100, null=True)
    director_address = models.CharField(max_length=255, null=True)
    director_email = models.CharField(max_length=100, null=True)
    director_pan = models.CharField(max_length=120, null=True)
    director_aadhaar = models.CharField(max_length=250, null=True)
    director_din = models.CharField(max_length=255, null=True)
    director_phone = models.CharField(max_length=20, null=True)
    director_father_name = models.CharField(max_length=100, null=True)
    director_status = models.BooleanField(null=True)
    director_dob = models.DateField(null=True, blank=True)
    director_photo = models.CharField(max_length=200, null=True, blank=True)
    director_signature = models.CharField(max_length=200, null=True, blank=True)
    dt=models.DateField(auto_now_add=True,null=True)


class tbl_shareholders(models.Model):
    Shareholder_id = models.CharField(max_length=100,null=True)
    SHAREHOLDER_NAME = models.CharField(max_length=255,null=True)
    PIN=models.CharField(max_length=255,null=True)
    AGE=models.CharField(max_length=255,null=True)
    DATE_OF_BIRTH = models.DateField(null=True)
    ADDRESS = models.TextField(null=True)
    PHONE_NUMBER = models.CharField(max_length=15, null=True)
    AADHAAR_NO = models.CharField(max_length=12, null=True)
    PAN_NO = models.CharField(max_length=10, null=True)
    SHARES_HELD = models.IntegerField(null=True)
    DATE_OF_JOINING = models.DateField(null=True)
    BANK_NAME = models.CharField(max_length=255, null=True)
    BRANCH_NAME = models.CharField(max_length=255, null=True)
    BANK_ACCNO = models.IntegerField( null=True)
    BANK_IFSC = models.CharField(max_length=255, null=True)
    NAME_REFERENCE=models.CharField(max_length=255, null=True)
    NOMINEE_NAME = models.CharField(max_length=255, null=True)
    NOMINEE_RELATION = models.CharField(max_length=255, null=True)
    NOMINEE_ADDRESS = models.CharField(max_length=255, null=True)
    OPENING_BALANCE = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    CURRENT_BALANCE = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    SIGNATURE=models.ImageField(upload_to="shareholder",null=True)
    SHAREHOLDER_IMAGE=models.ImageField(upload_to="share_image",null=True)
    dt=models.DateField(auto_now_add=True,null=True)

