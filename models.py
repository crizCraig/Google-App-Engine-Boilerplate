from google.appengine.ext import ndb

#class Post(ndb.Model):
#  author = ndb.StringProperty()
#  time = ndb.DateTimeProperty(auto_now_add=True)
#  title = ndb.StringProperty()
#  description = ndb.TextProperty(default='')
#  categories = ndb.StringProperty(repeated=True)
#  last_modified = ndb.DateTimeProperty(auto_now=True)
#
#  @property
#  def agoTime(self):
#    return agoTime(self.time)