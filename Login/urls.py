from django.urls import path
from . import views

urlpatterns=[
    path("",views.login_page,name="login_page"),
    path("login_check/",views.login_check,name="login_check"),
    path("dashboard/",views.dashboard,name="dashboard"),
    # ###############################################################
    path("basic_info_cmp/",views.basic_info_cmp),
    path("update_company/",views.update_company),
    path("save_company/",views.save_company),
    ##################################################################
    path("bank_info/",views.bank_info),
    path("add_bank/",views.add_bank),
    path("edit_bank/<id>",views.edit_bank),
    path("delete_bank/<id>",views.delete_bank),
    ##################################################################
    path("licenses/",views.licenses),
    path("add_license/",views.add_license),
    path("print_license/<id>",views.print_license),
    path("edit_license/<id>",views.edit_licenses),
    path("delete_licenses/<id>",views.delete_licenses),
    ###################################################################
    path("directors/",views.directors),
    path("add_directors/",views.add_directors),
    path("edit_directors/<id>",views.edit_directors),
    path("delete_directors/<id>",views.delete_directors),
    path("shareholders/",views.shareholders),
    path("add_shareholder/",views.add_shareholder),
    path("edit_shareholder/<id>",views.edit_shareholder)
]