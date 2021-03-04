from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    stock = IntegerField('Stock', validators=[DataRequired('Este campo es requerido')])
    price = FloatField('Price', validators=[DataRequired('Este campo es requerido')])
    category_id = SelectField('Categoría', validators=[DataRequired('Este campo es requerido')])

    submit = SubmitField('Enviar')
