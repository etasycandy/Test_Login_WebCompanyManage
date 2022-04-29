def txt_username():
    return "//input[@id = 'loginEmail']"


def txt_password():
    return "//input[@id = 'loginPass']"


def btn_login():
    return "//input[@value = 'Sign In']"


def btn_companyMenu():
    return "//*[@id=\"sidenav-collapse-main\"]/ul/li[2]/a"


def btn_addCompany():
    return "//*[@id=\"btn-add-company\"]"


def txt_compName():
    return "//*[@id=\"name\"]"


def txt_compEmail():
    return "//*[@id=\"email\"]"


def txt_compAddress():
    return "//*[@id=\"address\"]"


def txt_compLogo():
    return "//*[@id=\"logo\"]"


def txt_compReview():
    return "//*[@id=\"review\"]"


def btn_compSubmit():
    return "//*[@id=\"addCompanyForm\"]/div[2]/input"


def msg_result():
    return "//tr[5]/td[1]/div/div[2]/h6"
