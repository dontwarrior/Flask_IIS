from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import Length, DataRequired, NumberRange


class CalculatorForm(FlaskForm):
    amount = StringField("Въведете сума",
                         validators=[DataRequired(),
                                     Length(min=0, max=12),
                                     NumberRange(max=999999999)])
    submit = SubmitField("Въведете сума до 9 цифри преди запетаята и 2 цифри след нея")
