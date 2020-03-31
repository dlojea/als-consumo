#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = float(self.request.get("kilometros"))
        tiempo = float(self.request.get("tiempo"))
        consumo = float(self.request.get("consumo"))

        velocidad_media = kilometros / tiempo
        consumo_total = consumo * kilometros

        response = ("<div>Velocidad media = " + str(velocidad_media) + " km/h<div>" +
                    "<div>Consumo total = " + str(consumo_total) + " L<div>")

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
