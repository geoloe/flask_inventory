from flask import Blueprint, Flask, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from flask_mail import Mail
from . import db
from .models import *

#initialize flask app
mailing = Blueprint('mailing', __name__)