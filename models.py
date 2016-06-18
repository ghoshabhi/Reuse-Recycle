from google.appengine.ext import ndb

class User(ndb.Model):
	full_name = ndb.StringProperty(required=True)
	user_name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	contact_no = ndb.StringProperty(required=True)
	address_line_1 = ndb.StringProperty(required=True)
	address_line_2 = ndb.StringProperty()
	area = ndb.StringProperty(required=True)
	city = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=True)

class AdminUser(ndb.Model):
	full_name = ndb.StringProperty(required=True)
	user_name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	contact_no = ndb.StringProperty(required=True)

class CollectionCenter(ndb.Model):
	name = ndb.StringProperty(required=True)
	address_line_1 = ndb.StringProperty(required=True)
	address_line_2 = ndb.StringProperty()
	area = ndb.StringProperty(required=True)
	city = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=True)
	admin = ndb.KeyProperty(kind=AdminUser)

class DonationItem(ndb.Model):
	donor = ndb.KeyProperty(kind=user)
	collector = ndb.KeyProperty(kind=user)
	item_name = ndb.StringProperty(required=True)
	item_type = ndb.StringProperty(required=True)
	metric = ndb.StringProperty(required=True)
	time_limit = ndb.DateTimeProperty(required=True)


class Reward(ndb.Model):
	user = ndb.KeyProperty(kind=user)
	points = ndb.IntegerProperty(default=0)