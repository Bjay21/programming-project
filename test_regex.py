import re
def validate_phone_number(number):
    if re.match(r'^01[016789][1-9]\d{6,7}$', number):
        return True
    return False

print(validate_phone_number('01099017807'))
print(validate_phone_number('01694644811'))
print(validate_phone_number('01012341231'))