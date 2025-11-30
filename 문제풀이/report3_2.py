import datetime
import re

# 지역번호 목록
AREA_CODES = {
    "02", "031", "032", "033", "041", "042", "043", "044",
    "051", "052", "053", "054", "055", "061", "062", "063", "064"
}

def check_private_data(social, phone):
    if not valid_social(social):
        return "오류"
    if not valid_phone(phone):
        return "오류"
    return "정상"


# ----------------------------------------------------
# 주민등록번호 검사
# ----------------------------------------------------
def valid_social(s):
   
    if not re.fullmatch(r"\d{6}-\d{7}", s):
        return False

    front, back = s.split('-')
    yy, mm, dd = front[:2], front[2:4], front[4:6]
    g = back[0]

    # 성별코드에 따른 연도 계산
    if g in "12":  # 1900년대
        year = 1900 + int(yy)
    elif g in "34":  # 2000년대
        year = 2000 + int(yy)
    else:
        return False

    # 날짜 
    try:
        birth = datetime.date(year, int(mm), int(dd))
    except ValueError:
        return False

    if birth > datetime.date.today():
        return False

    return True


# ----------------------------------------------------
# 전화번호 검사
# ----------------------------------------------------
def valid_phone(p):
  
    parts = p.split('-')
    if len(parts) != 3:
        return False

    area, mid, last = parts

    # 숫자 여부
    if not (area.isdigit() and mid.isdigit() and last.isdigit()):
        return False

   
    if area not in AREA_CODES:
        return False

    # 중간 번호
    if not (3 <= len(mid) <= 4):
        return False

    # 마지막 번호: 4자리
    if len(last) != 4:
        return False

    return True
