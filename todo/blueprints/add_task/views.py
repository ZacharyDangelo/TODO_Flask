from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template
)

from todo.blueprints.add_task.forms import TaskForm

add_task = Blueprint('add_task', __name__, template_folder='templates')



@add_task.route('/add_task', methods=['GET', 'POST'])
def index():
    form = TaskForm()

    if form.validate_on_submit():
        flash('Task added! Now get to it >:)', 'success')
        return redirect(url_for('add_task.index'))

    return render_template('add_task/index.html', form=form)