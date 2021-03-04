from app import db
#from flask_bcrypt import generate_password_hash, check_password_hash
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
import datetime



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')


    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')