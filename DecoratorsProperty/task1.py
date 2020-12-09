
class ValidateEmail:
    def __init__(self, email):
        self.email = email

    def validate(self):
        no_valid_characters = '@'
        characters_count = 0
        if isinstance(self.email, str):
            for characters in self.email:
                if no_valid_characters in characters:
                    characters_count += 1
            if characters_count == 1:
                print('Email it\'s Ok')
            else:
                print('Too much \'@\' in email')
        else:
            print('Wrong email')


valid = ValidateEmail('parf.vetal@gmail.com')
# valid = ValidateEmail(1)
valid.validate()
