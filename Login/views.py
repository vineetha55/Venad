from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def login_page(request):
    return render(request, "login_page.html")


def login_check(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/dashboard/")
    else:
        return redirect("/login_page/")


def dashboard(request):
    return render(request, "dashboard.html")


def basic_info_cmp(request):
    data = tbl_basic_info_cmp.objects.get(id=1)
    return render(request, "basic_info_cmp.html",{"data":data})
def update_company(request):
    d=tbl_basic_info_cmp.objects.get(id=1)
    return render(request, "update_company.html",{"d":d})

def save_company(request):
    d=tbl_basic_info_cmp.objects.get(id=1)
    if request.method == "POST":
        d.cin = request.POST.get("cin")
        d.reg_no = request.POST.get("reg_no")
        d.CompanyName = request.POST.get("CompanyName")
        d.address = request.POST.get("address")
        d.mobile1 = request.POST.get("mobile1")
        d.mobile2 = request.POST.get("mobile2")
        d.email1 = request.POST.get("email1")
        d.email2 = request.POST.get("email2")
        d.start_date = request.POST.get("start_date")
        d.roc = request.POST.get("roc")
        d.gstin = request.POST.get("gstin")
        d.website = request.POST.get("website")
        d.category = request.POST.get("category")
        d.sub_category = request.POST.get("sub_category")
        d.class_company = request.POST.get("class_company")

        d.activity = request.POST.get("activity")
        d.age_company = request.POST.get("age_company")
        d.total_members = request.POST.get("total_members")

        d.save()
        try:
            logo_file = request.FILES['logo']
            if logo_file:

                fs = FileSystemStorage()
                h = fs.save(logo_file.name, logo_file)
                url = fs.url(h)
                d.logo = url
                d.save()
        except:
            pass

        return redirect("/basic_info_cmp/")

def bank_info(request):
    data = tbl_bank_info.objects.all().order_by('-id')
    return render(request,"bank_info.html",{"data":data})

def add_bank(request):
    if request.method=="POST":
        d=tbl_bank_info()
        d.bank_name=request.POST.get("bank_name")
        d.branch_name=request.POST.get("bank_branch")
        d.address=request.POST.get("bank_address")
        d.account_no=request.POST.get("bank_accno")
        d.ifsc_code=request.POST.get("bank_opening_balance")
        d.status=True
        d.bank_open_balance=request.POST.get("bank_opening_balance")
        d.save()
        return redirect("/bank_info/")
    else:

        return render(request,"add_bank.html")

def edit_bank(request,id):
    d=tbl_bank_info.objects.get(id=id)
    if request.method=="POST":
        d.bank_name = request.POST.get("bank_name")
        d.branch_name = request.POST.get("bank_branch")
        d.address = request.POST.get("bank_address")
        d.account_no = request.POST.get("bank_accno")
        d.ifsc_code = request.POST.get("bank_opening_balance")
        d.status = True
        d.bank_open_balance = request.POST.get("bank_opening_balance")
        d.save()
        return redirect("/bank_info/")
    else:
        return render(request,"edit_bank.html",{"d":d})


def delete_bank(request,id):
    d = tbl_bank_info.objects.get(id=id)
    d.delete()
    return redirect("/bank_info/")


def licenses(request):
    data=tbl_licenses.objects.all().order_by('-id')
    return render(request,"licenses.html",{"data":data})

def add_license(request):
    if request.method=="POST":
        d=tbl_licenses()
        d.license_name=request.POST.get("lic_name")
        d.license_number=request.POST.get("lic_number")
        d.expiry_date=request.POST.get("lic_expiry")
        d.expiry_reminder=request.POST.get("lic_reminder")
        d.status=True
        lic_file = request.FILES['lic_file']
        fs=FileSystemStorage()
        f=fs.save(lic_file.name,lic_file)
        url=fs.url(f)
        d.license_file=url
        d.save()
        return redirect("/licenses/")
    else:
        return render(request,"add_license.html")


def print_license(request,id):
    p=tbl_licenses.objects.get(id=id)
    return render(request,"print_license.html",{"p":p})


def edit_licenses(request,id):
    d =tbl_licenses.objects.get(id=id)
    if request.method=="POST":
        d.license_name=request.POST.get("lic_name")
        d.license_number=request.POST.get("lic_number")
        d.expiry_date=request.POST.get("lic_expiry")
        d.expiry_reminder=request.POST.get("lic_reminder")
        d.status=True
        d.save()
        try:
            lic_file = request.FILES['lic_file']
            if lic_file:
                fs = FileSystemStorage()
                f = fs.save(lic_file.name, lic_file)
                url = fs.url(f)
                d.license_file = url
                d.save()
        except:
            pass
        return redirect("/licenses/")
    else:
        print(d.expiry_reminder)
        return render(request,"edit_licenses.html",{"d":d})


def delete_licenses(request,id):
    d=tbl_licenses.objects.get(id=id)
    d.delete()
    return redirect("/licenses/")

def directors(request):
    directors=tbl_Director.objects.all().order_by('-id')
    return render(request,"directors.html",{"directors":directors})

def add_directors(request):
    if request.method=="POST":
        d=tbl_Director()
        d.director_name=request.POST.get("name")
        d.director_email=request.POST.get("email")
        d.director_dob=request.POST.get("dob")
        d.director_aadhaar=request.POST.get("aadhar")
        d.director_din=request.POST.get("din")
        d.director_address=request.POST.get("address")
        d.director_designation=request.POST.get("d_details_designation")
        d.director_father_name=request.POST.get("father")
        d.director_pan=request.POST.get("pan")
        d.director_phone=request.POST.get("phone")
        d.director_status=True
        photo=request.FILES['photo']
        sign=request.FILES['signature']
        fs=FileSystemStorage()
        p=fs.save(photo.name,photo)
        pu=fs.url(p)
        d.director_photo=pu
        s=fs.save(sign.name,sign)
        su=fs.url(s)
        d.director_signature=su
        d.save()
        return redirect("/directors/")
    else:
        return render(request,"add_directors.html")

def edit_directors(request,id):
    d=tbl_Director.objects.get(id=id)
    if request.method=="POST":
        d.director_name = request.POST.get("name")
        d.director_email = request.POST.get("email")
        d.director_dob = request.POST.get("dob")
        d.director_aadhaar = request.POST.get("aadhar")
        d.director_din = request.POST.get("din")
        d.director_address = request.POST.get("address")
        d.director_designation = request.POST.get("d_details_designation")
        d.director_father_name = request.POST.get("father")
        d.director_pan = request.POST.get("pan")
        d.director_phone = request.POST.get("phone")
        d.director_status = True
        d.save()
        try:
            photo = request.FILES['photo']
            sign = request.FILES['signature']
            fs = FileSystemStorage()
            p = fs.save(photo.name, photo)
            pu = fs.url(p)
            d.director_photo = pu
            s = fs.save(sign.name, sign)
            su = fs.url(s)
            d.director_signature = su
            d.save()
            return redirect("/directors/")

        except:
            pass
    else:
        return render(request,"edit_directors.html",{"d":d})


def delete_directors(request,id):
    d=tbl_Director.objects.get(id=id)
    d.delete()
    return redirect("/directors/")


def shareholders(request):
    data=tbl_shareholders.objects.all().order_by('-id')
    return render(request,"shareholders.html",{"data":data})

def add_shareholder(request):
    if request.method=="POST":
        d=tbl_shareholders()
        d.Shareholder_id=request.POST.get("member_mid")
        d.SHAREHOLDER_NAME=request.POST.get("member_name")
        d.SHARES_HELD=request.POST.get("share_shares")
        d.AADHAAR_NO=request.POST.get("share_aadhar")
        d.ADDRESS=request.POST.get("member_address")
        d.AGE=request.POST.get("member_age")
        d.DATE_OF_BIRTH=request.POST.get("member_dob")
        d.PIN=request.POST.get("member_pincode")
        d.PHONE_NUMBER=request.POST.get("member_pnumber")
        d.DATE_OF_JOINING=request.POST.get("member_joindate")
        d.BANK_ACCNO=request.POST.get("member_account")
        d.BANK_NAME=request.POST.get("member_bank")
        d.BANK_IFSC=request.POST.get("member_ifsc")
        d.BRANCH_NAME=request.POST.get("member_bank")
        d.NOMINEE_NAME=request.POST.get("member_nominee")
        d.NOMINEE_ADDRESS=request.POST.get("member_nominee_address")
        d.NOMINEE_RELATION=request.POST.get("member_nominee_relation")
        d.NAME_REFERENCE=request.POST.get("member_dhalam")
        photo = request.FILES['member_img']
        sign = request.FILES['member_signature']
        fs = FileSystemStorage()
        p = fs.save(photo.name, photo)
        pu = fs.url(p)
        d.SHAREHOLDER_IMAGE = pu
        s = fs.save(sign.name, sign)
        su = fs.url(s)
        d.SIGNATURE = su
        d.PAN_NO=request.POST.get("share_pan")
        d.OPENING_BALANCE=request.POST.get("member_sale_balance")
        d.CURRENT_BALANCE=request.POST.get("member_sale_balance")
        d.save()
        return redirect("/shareholders/")
    else:
        d=tbl_shareholders.objects.all().last()
        print(d)

        if d == None:
            share='KAPCO/SH00'+'1'
            print(share)
        else:
            d1=d.id
            d2=d1+1
            share = 'KAPCO/SH00' + str(d2)
            print(share)
        return render(request,"add_shareholder.html",{"share":share})


def edit_shareholder(request,id):
    d=tbl_shareholders.objects.get(id=id)
    if request.method=="POST":
        pass

    else:
        return render(request,"edit_shareholder.html",{"d":d})
