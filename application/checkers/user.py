# -*- coding: utf-8 -*-
import time


def register_params_check(content):
    """
    注册信息检查
    """
    user = content
    print(user)
    if not ('username' in user and isinstance(user['username'], str) and 6 <= len(user['username']) <= 10):
        return 'username', False
    if 'password' in user and isinstance(user['password'], str) and 6 <= len(user['password']) <= 18:
        capital = 0
        lowercase = 0
        number = 0
        for a in user['password']:
            if 'A' <= a <= 'Z':
                capital = 1
            elif 'a' <= a <= 'z':
                lowercase = 1
            elif '0' <= a <= '9':
                number = 1
            else:
                return 'password', False
        if capital != 1 or lowercase != 1 or number != 1:
            return 'password', False
    else:
        return 'password', False
    if not ('nickname' in user and isinstance(user['nickname'], str) and 2 <= len(user['nickname']) <= 8):
        return 'nickname', False
    if 'document_number' in user and isinstance(user['document_number'], str) and len(user['document_number']) == 18:
        check = 0
        for i in range(0, len(user['document_number'])):
            a = user['document_number'][i]
            if '0' <= a <= '9':
                check = (check + int(a) * (2 ** (17 - i))) % 11
            elif a == 'X' and i == 17:
                check = (check + 10) % 11
            else:
                return 'document_number', False
        if check != 1:
            return 'document_number', False
        year = int(user['document_number'][6:10])
        month = int(user['document_number'][10:12])
        day = int(user['document_number'][12:14])
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return 'document_number', False
        elif day == 31 and month in [2, 4, 6, 9, 11]:
            return 'document_number', False
        elif day == 30 and month == 2:
            return 'document_number', False
        elif day == 29 and month == 2 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
            return 'document_number', False
        localtime = time.localtime(time.time())
        if localtime.tm_year < year + 18:
            return 'document_number', False
        elif localtime.tm_year == year + 18:
            if localtime.tm_mon < month:
                return 'document_number', False
            elif localtime.tm_mon == month and localtime.tm_mday < day:
                return 'document_number', False
    else:
        return 'document_number', False
    if not ('mobile' in user and isinstance(user['mobile'], int) and 10000000000 <= user['mobile'] <= 99999999999):
        return 'mobile', False
    if 'email' in user and isinstance(user['email'], str) and '@' in user['email']:
        sections = user['email'].split('@', 1)
        if len(sections[0]) <= 63 and len(sections[1]) <= 63 and sections[0].isalnum() and '.' in sections[1]:
            tags = sections[1].split('.')
            for tag in tags:
                if len(tag) == 0 or tag[0] == '-' or tag[len(tag) - 1] == '-':
                    return 'email', False
                for a in tag:
                    if not ('A' <= a <= 'Z' or 'a' <= a <= 'z' or '0' <= a <= '9' or a == '-'):
                        return 'email', False
            num = 1
            for a in tags[len(tags) - 1]:
                if not '0' <= a <= '9':
                    num = 0
            if num == 1:
                return 'email', False
        else:
            return 'email', False
    else:
        return 'email', False
    return "ok", True
