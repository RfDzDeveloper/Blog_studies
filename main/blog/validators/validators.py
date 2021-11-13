import re


class PasswordValidator:
    def __init__(self, min_length: int) -> bool:
        self.min_length = min_length

    # length validation

    def _is_password_length(self, password: str) -> bool:
        if len(password) < self.min_length:
            raise Exception(
                f"Password is too short. Password length should be longer then {self.min_length}"
                )
        else:
            return True
        

   # does contains regular expression

    def _is_password_contain_regular_expression(self, password, user= None) -> bool:
        if re.search('[A-Z]', password)== None and re.search('[0-9]', 
        password) == None and re.search('[^A-Za-z0-9]', password) == None:
            raise Exception(
                "Your password must contain one number, one uppercase letter and one non-alphanumeric character.)"
            )
        else:
            return True

    # confirmation password 

    def _is_password_well_confirm(self, password: str, confirmation_password: str) -> bool:
        if password == confirmation_password:
            return True
        else:
            raise Exception("Your password doesn't match!")
    
    
    def make_full_password_validation(self, password: str, confirm_password: str) -> str:
        if self._is_password_length(password):
            if self._is_password_well_confirm(password, confirm_password):
                if self._is_password_contain_regular_expression(password):
                    return True
    
class EmailValidator:
    def check_email_length(self, email: str) -> bool:
        if len(email) > 100:
            raise ValueError("Email must be shorter then 100 signs!")
        
        else: return True

    
    def check_email_form(self, email: str) -> bool:        
        number: int = 0
        for item in email:
            if item == "@":
                number = number + 1
                if number > 1:
                    raise ValueError("Email can't contains more then one '@' sign!")
        if number == 0:
            raise ValueError("Email must contains exacly one '@' sign!")
        
        return True

    
    def check_email_contains_not_allowed_re(self, email: str) -> bool:
        pattern = re.compile("[/\!#$%^&*()=+{};:'<>,?]")
        if bool(re.search(pattern, email)):
            raise ValueError(f"Email: {email} can't contains any of this"
                "\nregular expression!"
                "\nlike: [/\!#$%^&*()=+{};:'<>,?]")
        return True

class UserValidator:
    def _check_username_length(self, username: str) -> bool:
        if len(username) > 25:
            raise ValueError(f"Username is too long: {len(username)}. Max 25 signs!")
        
        if len(username) < 6:
            raise ValueError(f"Username is too short: {len(username)}. Min 6 sings!")
        
        return True
        
    def _first_name_length(self, first_name: str) -> bool:
        if len(first_name) > 25:
            raise ValueError(f"First name is too long: {len(first_name)}. Max 25 signs!")
        
        if len(first_name) < 3:
            raise ValueError(f"First name is too short: {len(first_name)}. Min 3 signs!")
        
        return True 
    

    def _last_name_length(self, first_name: str) -> bool:
        if len(first_name) > 25:
            raise ValueError(f"First name is too long: {len(first_name)}. Max 25 signs!")
        
        if len(first_name) < 3:
            raise ValueError(f"First name is too short: {len(first_name)}. Min 3 signs!")

        return True    
    
    def check_email_contains_not_allowed_re(self, email: str) -> bool:
        pattern = re.compile("[/\!#$%^&*()=+{};:'<>,?]")
        if bool(re.search(pattern, email)):
            raise ValueError(f"Email: {email} can't contains any of this"
                "\nregular expression!"
                "\nlike: [/\!#$%^&*()=+{};:'<>,?]")
        return True

    
    def check_string_contains_re(self, string_tuple: tuple) -> bool:
        pattern = re.compile("[/\!@#$%^&*()_=+{};:'<>,.?]")
        for item in string_tuple:
            if bool(re.search(pattern, item)):
                raise Exception(f"This position: {item} can't contains any regular expression!"
                "\nlike('!@#$%^&*()_+[];:',.<>?!')")

        return True

    
    def is_string_contains_numbers(self, string_tuple: tuple) -> bool:
        for text in string_tuple:
            if bool(re.search(r'\d', text)):
                raise Exception(f"This position: {text} can't contains numbers!")            
        return True

    def make_full_user_validation(self, user_data: dict) -> bool:
        if EmailValidator().check_email_length(user_data['email']):
            if EmailValidator().check_email_form(user_data['email']):
                if self._check_username_length(user_data['username']):
                    if self._first_name_length(user_data['first_name']):
                        if self._last_name_length(user_data['last_name']):
                            if self.is_string_contains_numbers((
                                user_data['last_name'], user_data['first_name'])):
                                if self.check_string_contains_re((user_data["last_name"],
                                    user_data["first_name"])):                     
                                    if self.check_email_contains_not_allowed_re(
                                        user_data["email"]):    
                                        return True