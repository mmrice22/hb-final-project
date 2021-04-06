from flask import Flask, render_template, request

import os
import requests 

app = Flask(__name__)
app.secret_key = 'SECRETKEYSECRETKEYSECRETKEY'

API_KEY = os.environ['NPS_KEY']