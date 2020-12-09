
class ValidateEmail:
    def __init__(self, email):
        self.email = email

    def validate(self):

        if isinstance(self.email, str):
            characters_count = self.email.count('@')
            if characters_count == 0:
                print('Wrong email,  missing \'@\'')
            if characters_count == 1:
                print('Email it\'s Ok')
            else:
                print('Too much \'@\' in email')
        else:
            print('Wrong email')


valid = ValidateEmail('parf.vetal@gmail.com')
# valid = ValidateEmail(1)
valid.validate()
