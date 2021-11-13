from django.http.request import HttpRequest
from django.contrib.auth.models import User
from blog.models import Post, Comment, EmailToken, UserRatings
from blog.validators.validators import UserValidator, PasswordValidator


class DatabaseService:
    def add_user(self, request: HttpRequest) -> User:    
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
    
    def _get_post_data(self, request: HttpRequest) -> Post:
        post: Post = Post(text=request.POST['text'], title=request.POST['tile'],
                          user=request.user)        
        
        if len(post.text) == 0 or post.text == '' or post.text == ' ':
            raise ValueError("Text can't be empty!")
        
        if len(post.title) == 0 or post.title == '' or post.title ==' ':
            raise ValueError("Title can't be empty!")
        
        text_len: int = len(post.text)
        if text_len > 1500:
            raise ValueError(
                f"Post can't contains more then 1500 characters. \nNow it's: {text_len}")
            
        if text_len < 20:
            raise ValueError(
                f"Post can't contains less then 20 characters.\nNow it's: {text_len}")
        
        title_len: int = len(post.title)
        if title_len > 500:
            raise ValueError(
                f"Title can't contains more then 500 characters.\nNow it's: {title_len}")
            
        if title_len < 5:
            raise ValueError(
                f"Title can\t contains less then 5 characters.\nNow it's: {title_len}")
        return post            
        
    
    def add_post(self, request: HttpRequest) -> Post:        
        post: Post = self._get_post_data(request)        
        
        response: tuple = Post.objects.get_or_create(
            text=post.text, title=post.title, user=post.user)
        if response[1] == False:
            raise ValueError(f"This title: {post.title} exist.\nPlease chooce diffrent.")        
        
        return response[0]
    
    def edit_post(self, request: HttpRequest) -> Post:
        post_id: int = request.POST['post_id']
        post: Post = self._get_post_data(request)        
        response: bool = Post.objects.filter(id=post_id).exists()
        if not response:
            raise Post.DoesNotExist("You can't edit non existing post!")
        post = Post.objects.filter(id=post_id)[0]
        
        post.save()
        
        return post        
        
    def delete_post(self, request: HttpRequest) -> bool:
        post_id: int = request.POST['post_id']
        
        response: bool = Post.objects.filter(id=post_id).exists()
        if not response:
            raise Post.DoesNotExist(f"This post: {post_id} do not exists!\n")
        Post.objects.filter(id=post_id).delete()
        
        return True
    
    def _get_comment_data(self, request: HttpRequest) -> str:
        text: str = request.POST['text']
        text_len: int = len(text)
        if text_len > 500:
            raise ValueError("Comment text can't contains more then 500 characters.\n"
                             f"Now its: {text_len}")
        if text_len < 1:
            raise ValueError(
                f"Comment can;t contains less then 1 character.\nNow it's: {text_len}")
             
        return text
    
    def add_comment(self, request: HttpRequest) -> Comment:
        comment: Comment = Comment(text=self._get_comment_data(request),
                                   user=request.user,
                                   post=request.POST['post_id'])
        comment.save()
        return comment
    
    def edit_comment(self, request: HttpRequest) -> Comment:
        response: bool = Post.objects.filter(id=request.POST['post_id']).exists()
        if not response:
            raise Post.DoesNotExist(f"You can't add comment to post which doesn' exists")
        post: Post = Post.objects.filter(id=request.POST['post_id'])[0]
        comment: Comment = Comment(text=self._get_comment_data(),
                                   user=request.user,
                                   post=post)
        response = Comment.objects.filter(id=request.POST['post_id']).exists()
        if not response:
            raise Comment.DoesNotExist(
                f"Can't edit this: {request.POST['comment_id']}.\nThis comment don't exists!")
        com_db: Comment = Comment.objects.filter(id=request.POST['comment_id'])[0]
        com_db = comment
        com_db.save()
        return com_db    
    
    def delete_comment(self, request: HttpRequest) -> bool:
        response: bool = Comment.objects.filter(id=request.POST['comment_id']).exists()
        if not response:
            raise Comment.DoesNotExist(
                f"Comment id: {request.POST['comment_id']} doesn't exist!")
        Comment.objects.filter(id=request.POST['comment_id']).delete()
        return True  
    
    def get_new_posts(self) -> list[Post]:
        return Post.objects.all().order_by(
               'publish_date').values_list('id', 'title', 'publish_date')[:10]
        
    def get_all_posts(self, number_post: int) -> list[Post]:
        return Post.objects.all().order_by(
               'publish_date').values_list(
                   'id', 'title', 'publish_date', 'post_rating')[:number_post]
               
    def get_user_by_email(self, request: HttpRequest) -> User:
        check: bool = User.objects.filter(email=request.POST['email']).exists()        
        if not check:
            raise User.DoesNotExist(f"Can't fine user by email: {request.POST['email']}")
        return User.objects.get(email=request.POST['email'])
        
    def check_exists_token(self, token: str) -> str:
        response: EmailToken = EmailToken.objects.filter(token=token)
        if len(response) == 0:
            raise EmailToken.DoesNotExist("Try again reset password!\nToken Error!")
        response.delete()
        return response.email
    
    def add_rating(self, post_id: int, user: User, rating: int) -> None:
        response: list[UserRatings] = UserRatings.objects.filter(
            user__id=user.pk).filter(post__id=post_id)
        if len(response) > 0:
            raise Exception("You can't rate again this post!")
    
        post: Post = Post.objects.get(id=post_id)
        UserRatings(ratings=rating, user=user, post=post).save()
        
    def get_post_ratings(self, post_id: int) -> float:
        response: list[UserRatings] = UserRatings.objects.filter(post__id=post_id)
        sum_value: int = 0
        for item in response:
            sum_value += item.ratings
        average: float = sum_value/len(response)
        return average
        