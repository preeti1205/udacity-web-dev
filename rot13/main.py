# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import cgi
form="""
<body>
 <form method = "post" >
  <h2>Enter some text to ROT13:</h2>
    <textarea name = "text" style = "height: 100px; width:400px;"></textarea>
    <br>
        <input type = "submit" >
    </form>
</body>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #content type shouldn't be plain if we want to embed html in here
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write("Hello Udacity !")
        self.response.write(form)

    def post(self):    #put what you want here - get or post ?
        #q = self.request.get("data")
        rot = self.rot13(self.request.get("text"))
        rot = self.escape_html(rot)
        self.response.write(rot)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request)

    def rot13(self, str):
        mylist = []
        for i in str:
            i = ord(i)
            if (i >= 65 and i<=77) or (i >= 97 and i<=109):
                mylist.append(chr(i+13))
            elif (i >= 78 and i<=90) or (i >= 110 and i<=122):
                mylist.append(chr(i-13))
            else:
                mylist.append(chr(i))
        return "".join(mylist)

    def escape_html(self,s):
        return cgi.escape(s, quote=True)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
