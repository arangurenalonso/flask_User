from flask import Flask
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from flask_mail import Mail

root_dir = Path(__file__).parent.parent
template_dir = root_dir / 'resources/templates'


app = Flask(__name__, template_folder=template_dir, 
                static_url_path='/static', static_folder='../resources/static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail=Mail(app)

from app.user.userModel import User
user_manager = UserManager(app, db, User)




from app.user import userModel
from app.rol import rolModel
from app.userRol import userRolModel

from app.auth import authRouter

#from app.home import homeRouter
#from app.menu import menuModel, menuRouter
#from app.category import categoryModel, categoryRouter
#from app.post import postModel, postRouter
#
#from app.empleado import empleadoModel,empleadoRouter 
#
#from app.auth import authRouter

