from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from . import student
from .forms import (AddTestScoreForm)
from ..models import TestScore
from .. import db

@student.route('/profile')
@login_required
def view_user_profile():
	return render_template('student/student_profile.html', user = current_user)


@student.route('/profile/add_test_score', methods=['GET', 'POST'])
@login_required
def add_test_score():
    #display list of default checklist items and option to add a new one
    form = AddTestScoreForm()
    if form.validate_on_submit():
        #create new test score from form data
        new_item = TestScore(
                    student_profile_id = current_user.id,
                    name=form.test_name.data,
                    score=form.test_score.data,
                    month=form.test_month.data,
                    year=form.test_year.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('student.view_user_profile'))

    return render_template('student/add_test_score.html', form=form)

