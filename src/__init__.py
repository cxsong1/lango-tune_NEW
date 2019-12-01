"""
Functions defining behaviour of all Flask endpoints
"""
from traceback import format_exc

from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException

from .flask_utils import api_call

APP = Flask(__name__)

@APP.route('/')
def home():
    return render_template("layout.html")

@APP.route('/api')
def api():
    return api_call()

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