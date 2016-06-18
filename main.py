import os
import webapp2
import re
import hashlib
import hmac
import json
import time

from models import User,AdminUser,CollectionCenter,DonationItem,Reward
from google.appengine.ext import ndb
from google.appengine.api import images

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                            autoescape = True)

SECRET = "mysecretkey"

def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s,hash_str(s))

def check_secure_val(h):
    val = h.split("|")[0]
    if h == make_secure_val(val):
        return val

USERNAME_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USERNAME_RE.match(username)


PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)


EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


def check_for_valid_cookie(self):
    user_email_cookie = self.request.cookies.get('user_email')
    if user_email_cookie:
        if_valid_cookie = check_secure_val(user_email_cookie)
        if if_valid_cookie:
             return self.request.cookies.get('user_email').split("|")[0]
        else:
            return None
    else:
        return None

def filterKey(key):
    return key.id()

jinja_env.filters['filterKey'] = filterKey


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Home Page!')


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/home', HomeHandler)
], debug=True)
