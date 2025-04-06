def roman_converter(user_decimal):
    result = ''
    while user_decimal !=0:
        best_matched_roman = roman_mathcer(user_decimal)
        int_part = user_decimal // best_matched_roman[0]
        result += int_part*best_matched_roman[1]
        user_decimal = user_decimal - best_matched_roman[0]*int_part
    return result


def roman_mathcer(decimal):
    match decimal:
        case _ if decimal >= 1000:
            return (1000, 'M')
        case _ if decimal >= 900:
            return (900, 'CM')
        case _ if decimal >= 500:
            return (500, 'D')
        case _ if decimal >= 400:
            return (400, 'CD')
        case _ if decimal >= 100:
            return (100, 'C')
        case _ if decimal >= 90:
            return (90, 'XC')
        case _ if decimal >= 50:
            return (50, 'L')
        case _ if decimal >= 40:
            return (40, 'XL')
        case _ if decimal >= 10:
            return (10, 'X')
        case _ if decimal >= 9:
            return (9, 'IX')
        case _ if decimal >= 5:
            return (5, 'V')
        case _ if decimal >= 4:
            return (4, 'IV')
        case _ if decimal >= 1:
            return (1, 'I')
        case _:
            return None