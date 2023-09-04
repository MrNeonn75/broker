from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from datetime import datetime
from django.utils.timezone import now

# User manager
class AccountsManager(BaseUserManager):
    # Function for creating normal user
    def create_user(self, first_name, last_name, username, email, password, 
                    is_admin=False,
                    is_active=False,
                    is_staff=False,
                    is_superadmin=False):
        # If user does not import email returns error message
        if(not email):
            raise ValueError('User must have an email adress')
        # If user does not imoport username returns error message
        if(not username):
            raise ValueError('User must have an username')
        
        # Create user data
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            is_admin = is_admin,
            is_active = is_active,
            is_staff = is_staff,
            is_superadmin =is_superadmin
        )

        # Set password to user
        user.set_password(password)
        # Save user data
        user.save(using=self._db)

        return user
    
    # Function for creating superuser
    def create_superuser(self, email, username, password, first_name, last_name):
        # Create super user
        # user = self.create_user(
        #     email = self.normalize_email(email),
        #     username = username,
        #     password = password,
        #     phone_number = phone_number,
        #     first_name = first_name,
        #     last_name = last_name,
        # )

        # # User will be admin
        # user.is_admin = True
        # # User will be active
        # user.is_active = True
        # # User will be staff's member
        # user.is_staff = True
        # # User will be super admin
        # user.is_superadmin = True
        # Saving user 
        

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            is_admin = True,
            is_active = True,
            is_staff = True,
            is_superadmin = True
        )
        user.save(using=self._db)
        
        return user

# Accounts table
class Accounts(AbstractBaseUser):
    # User's first name
    first_name = models.CharField('First name', max_length=50)
    # User;s last name
    last_name = models.CharField('Last name', max_length=50)
    # User's username
    username = models.CharField('Username', max_length=50)
    # User's email
    email = models.EmailField('Email', max_length=100, unique=True)
    # User id
    id = models.AutoField(primary_key=True)
    # Password
    password = models.CharField('Password', max_length=100)
    

    # required data
    # The date when user joined
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    # The date when user has logined last time
    last_login = models.DateTimeField('Last login', auto_now_add=True)
    # Is user admin?
    is_admin = models.BooleanField('Is admin?', default=False)
    # Is user staff member?
    is_staff = models.BooleanField('Is staff?', default=False)
    # Is active?
    is_active = models.BooleanField('Is active?', default=False)
    # Is superadmin?
    is_superadmin = models.BooleanField('Is suoeradmin', default=False)

    # Login with email, username or phone number
    USERNAME_FIELD = 'email'
    # Required data
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    objects = AccountsManager()

    # function for getting full name
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'
    
# User profile data
class UserProfile(models.Model):
    # User One to One connect
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    # Profile picture
    profilePicture = models.ImageField('Profile picture', blank=True,upload_to='userProfile')
    # User's phone number
    phone_number = models.CharField('Phone number', max_length=50)
    
    def __str__(self):
        return self.user.first_name
    
    # Function for getting adress
    def full_address(self):
        return f'{self.adress}'