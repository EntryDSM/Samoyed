from samoyed.model import session
from samoyed.model.graduated_application import GraduatedApplication
from samoyed.model.school import School
from samoyed.model.ungraduated_application import UnGraduatedApplication


def print_excel_num(apply_type, is_daejeon, receipt_code):

    user_type = 0
    location = 0
    additional_type = 0
    num = ''

    if apply_type == "COMMON":
        user_type = 1
    elif apply_type == "MEISTER":
        user_type = 2
    elif apply_type[:5] == ['SOCIAL']:
        user_type = 3

    if is_daejeon == 1:
        location = 1
    elif is_daejeon == 0:
        location = 2

    if apply_type == "COMMON":
        additional_type = 0
    elif apply_type == "MEISTER":
        additional_type = 0
    elif apply_type == "SOCIAL_ONE_PARENT":
        additional_type = 2
    elif apply_type == "SOCIAL_FROM_NORTH":
        additional_type = 5
    elif apply_type == "SOCIAL_MULTICULTURAL":
        additional_type = 6
    elif apply_type == "SOCIAL_BASIC_LIVING":
        additional_type = 1
    elif apply_type == "SOCIAL_LOWEST_INCOME":
        additional_type = 4
    elif apply_type == "SOCIAL_TEEN_HOUSEHOLDER":
        additional_type = 3

    if receipt_code < 10:
        num = f'00{receipt_code}'
    elif receipt_code < 100:
        num = f'0{receipt_code}'
    else:
        num = receipt_code

    return f"{user_type}{location}{additional_type}{num}"


def print_apply_type(apply_type):
    if apply_type == "COMMON":
        return "일반전형"
    elif apply_type == "MEISTER":
        return "마이스터전형"
    elif apply_type.startswith('SOCIAL'):
        return "사회통합전형"


def print_additional_type(apply_type, additional_type):
    if apply_type == "SOCIAL_ONE_PARENT":
        return "한부모가족"
    elif apply_type == "SOCIAL_FROM_NORTH":
        return "북한이탈주민"
    elif apply_type == "SOCIAL_MULTICULTURAL":
        return "다문화가정"
    elif apply_type == "SOCIAL_BASIC_LIVING":
        return "기초생활수급자"
    elif apply_type == "SOCIAL_LOWEST_INCOME":
        return "차상위계층"
    elif apply_type == "SOCIAL_TEEN_HOUSEHOLDER":
        return "소년소녀가장"
    else:
        if additional_type == "NOT_APPLICABLE":
            return "일반"
        elif additional_type == "PRIVILEGED_ADMISSION":
            return "특례입학대상"
        elif additional_type == "NATIONAL_MERIT":
            return "국가유공자"


def print_grade_type(grade_type):
    if grade_type == "GED":
        return "검정고시합격자"
    elif grade_type == "UNGRADUATED":
        return "졸업예정자"
    elif grade_type == "GRADUATED":
        return "졸업자"


def print_is_daejeon(is_daejeon):
    if is_daejeon == 1:
        return "대전"
    elif is_daejeon == 0:
        return "전국"


def print_sex(sex):
    if sex == "MALE":
        return "남"
    elif sex == "FEMALE":
        return "여"


def print_graduated_year(receipt_code, grade_type):
    if grade_type == "UNGRADUATED":
        return "2021"
    elif grade_type == "GED":
        return ""
    elif grade_type == "GRADUATED":
        user_info = session.query(GraduatedApplication).filter(
                    GraduatedApplication.user_receipt_code == receipt_code).first()
        return f"{user_info.graduated_date}"


def print_origin_school(receipt_code, grade_type):
    try:
        if grade_type == "GED":
            return ""
        elif grade_type == "UNGRADUATED":
            user_info = session.query(UnGraduatedApplication).filter(
                        UnGraduatedApplication.user_receipt_code == receipt_code).first()
            school_info = session.query(School).filter(School.school_code == user_info.school_code).first()
            return school_info.school_name
        elif grade_type == "GRADUATED":
            user_info = session.query(GraduatedApplication).filter(
                        GraduatedApplication.user_receipt_code == receipt_code).first()
            school_info = session.query(School).filter(School.school_code == user_info.school_code).first()
            return school_info.school_name
    except AttributeError:
        return ''


def print_student_number(receipt_code, grade_type):
    if grade_type == "GED":
        return ""

    elif grade_type == "UNGRADUATED":
        ungraduated_application = session.query(UnGraduatedApplication) \
                .filter(UnGraduatedApplication.user_receipt_code == receipt_code).first()
        return f"{ungraduated_application.student_number}"

    elif grade_type == "GRADUATED":
        graduated_application = session.query(GraduatedApplication) \
            .filter(GraduatedApplication.user_receipt_code == receipt_code).first()
        return f"{graduated_application.student_number}"


def create_str_cell_location(row, column):
    str_column = chr(64 | column)

    return f"{str_column}{row}"
