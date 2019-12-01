"""
Functions defining behaviour of all Flask endpoints
"""
from traceback import format_exc

from flask import Flask, render_template, jsonify, request

from werkzeug.exceptions import HTTPException

from .flask_utils import api_call

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

APP = Flask(__name__)

@APP.route('/')
def home():
    return render_template("layout.html")

@APP.route('/api')
def api():
    return api_call()

@app.route('/', methods=['POST'])
def post_song():
    api_call()
    return render_template("layout.html")

@APP.route('/health')
def health():
    return jsonify({'status': 'OK'})

@APP.route('/error')
def error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    stack_trace = format_exc()
    return jsonify({
        'error': code,
        'message': getattr(error, 'desc', None) or stack_trace
    })