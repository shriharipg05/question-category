import logging
from random import randint
from flask_ask import Ask, statement, question
import requests
import json
import os
import re
import requests.packages.urllib3
from xml.sax import saxutils as su
from flask import Flask, render_template, jsonify
from operator import itemgetter
import threading, alexaParlLogin, alexaParlFeedback, alexaParlproduct, alexaParlsupport
from selenium import webdriver
from selenium.webdriver import ActionChains
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def welcome_message():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("loginIntent")
def loginPage():
    t = threading.Thread(target=alexaParlLogin.startPage)
    t.start()
    homePage_msg = render_template('homePage')
    return question(homePage_msg)

@ask.intent("feedbackIntent")
def feedbackList():
    t = threading.Thread(target=alexaParlFeedback.startPage)
    t.start()
    feedbackList_msg = render_template('feedbackList')
    return question(feedbackList_msg)

@ask.intent("productIntent")
def productList():
    t = threading.Thread(target=alexaParlproduct.startPage)
    t.start()
    productList_msg = render_template('productList')
    return question(productList_msg)

@ask.intent("supportIntent")
def suggestList():
    t = threading.Thread(target=alexaParlsupport.startPage)
    t.start()
    supportList_msg = render_template('supportList')
    return question(supportList_msg)

@ask.intent("NoIntent")
def not_interested():
	nomsg = render_template('notinterested')
	return statement(nomsg)

if __name__ == '__main__':
	app.run(debug=True)
