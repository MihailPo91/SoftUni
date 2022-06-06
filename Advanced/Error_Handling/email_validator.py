class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_email(email):
    valid_domains = {'.com', '.bg', '.org', '.net'}
    at_index = email.find('@')
    name = email[:at_index]
    email_elements = email.split('.')
    domain = '.' + email_elements[-1]

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    return True


while True:
    line = input()
    if line == 'End':
        break

    current_email = line

    if validate_email(current_email):
        print('Email is valid')
