from flask_wtf import Form
from wtforms import TextAreaField
from wtforms import DateTimeField
from wtforms.validators import DataRequired, Length


class TaskForm(Form):
    task_name = TextAreaField("Task Name",
                              [DataRequired(), Length(3,254)])
    task_description = TextAreaField("Task Description",
                                     [DataRequired, Length(1,1028)])
