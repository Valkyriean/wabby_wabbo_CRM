from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.db_models.auth_model import Company
from flaskr.setup import login_manager


bp = Blueprint('auth', __name__, url_prefix='/dashboard')

