from samoyed.model import session
from samoyed.model.graduated_application import GraduatedApplication
from samoyed.model.school import School
from samoyed.model.ungraduated_application import UnGraduatedApplication


def print_apply_type(apply_type):
    if apply_type == "COMMON":
        return "일반전형"
    elif apply_type == "MEISTER":
        return "마이스터전형"
    elif apply_type[:5] == ['SOCIAL'] :
        return "사회통합전형"


def print_social_type(apply_type):
    if apply_type == "SOCIAL_ONE_PARENT":
        return "한부모가족_"
    elif apply_type == "SOCIAL_FROM_NORTH":
        return "북한이탈주민_"
    elif apply_type == "SOCIAL_MULTICULTURAL":
        return "다문화가정_"
    elif apply_type == "SOCIAL_BASIC_LIVING":
        return "기초생활수급자_"
    elif apply_type == "SOCIAL_LOWEST_INCOME":
        return "차상위계층_"
    elif apply_type == "SOCIAL_TEEN_HOUSEHOLDER":
        return "소년소녀가장_"
    else:
        return ""


def print_additional_type(additional_type):
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
