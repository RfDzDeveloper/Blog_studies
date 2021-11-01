from django.http.request import HttpRequest
from django.contrib.auth.models import User
from validators.validators import UserValidator, PasswordValidator


class DatabaseService:
    def add_user(request: HttpRequest) -> User:    
        password: str = request.POST['password']
        confirm_password: str = request.POST['confirm_password']
        username: str = request.POST['username']
        first_name:str = request.POST['first_name']
        email: str = request.POST['email']
        last_name: str = request.POST['last_name']

        user: User = User()
        user_dictionary = {
            'password': password,
            'confirm_password': confirm_password,
            'username': username.capitalize(),
            'first_name': first_name.capitalize(),
            'email': email.lower(),
            'last_name': last_name.capitalize(),
        }
        result: bool = User.objects.filter(username==user_dictionary['username']).exists()

        if password == None or password == " ":
            raise ValueError("Password can't be empty!")

        if result:
            raise ValueError("Username is already taken!")

        is_password_valid: bool = PasswordValidator(6).make_full_password_validation(
            user_dictionary['password'], user_dictionary['confirm_password'])
        
        is_user_valid: bool = UserValidator().make_full_user_validation(user_dictionary)

        user.set_password(user_dictionary['password'])   
        user.username = user_dictionary['username']
        user.first_name = user_dictionary['first_name']     
        user.last_name = user_dictionary['last_name']
        user.email = user_dictionary['email'] 
        if is_password_valid and is_user_valid:                 
            user.save()     

        return user