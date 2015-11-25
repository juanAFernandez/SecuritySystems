# -*- coding: utf-8 -*-

import datetime
import jinja2
import os
import webapp2
import cgi
from nihilistSimpleClass import NihilistCipher
from analytics import *

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))


class Home(webapp2.RequestHandler):
    def get(self):

        #Por ahora el único usuario que se puede registrar es el administrador del sistema.
        template = template_env.get_template('templates/home.html')

        self.response.out.write(template.render())




class Atack(webapp2.RequestHandler):
    def get(self, tipo=None, textoCifrado=None):

        if tipo=='Analizar':
            #Por ahora el único usuario que se puede registrar es el administrador del sistema.
            template = template_env.get_template('templates/atack.html')

            textoCifrado=self.request.get('texto')
            tabla=analytics(textoCifrado)
            print tabla

            import json

            templateVars = {"tabla" : tabla, 'textoCifrado':textoCifrado}
            self.response.out.write(template.render(templateVars))

        else:

            template = template_env.get_template('templates/atack.html')

            self.response.out.write(template.render())

    def post(self):
        tipo=self.request.get('tipo')
        self.get(tipo)

class Use(webapp2.RequestHandler):
    def get(self, mensaje=None, textoOriginal=None, clave=None):

        #Por ahora el único usuario que se puede registrar es el administrador del sistema.
        template = template_env.get_template('templates/use.html')

        if mensaje!=None:
            templateVars = {"mensaje" : mensaje, "textoOriginal":textoOriginal, "clave":clave }
            self.response.out.write(template.render(templateVars))
        else:
            self.response.out.write(template.render())


    def post(self):
        tipo=self.request.get('tipo')
        texto=self.request.get('texto')
        clave=self.request.get('clave')

        if tipo=='cifrar': #Ciframos y enviamos a la interfaz
            NC = NihilistCipher()
            mensajeCifrado=NC.cifrar(clave, texto)
            self.get(mensajeCifrado, texto, clave)

        if tipo=='descifrar':
            #print "descifrando"
            NC = NihilistCipher()
            mensajeDescifrado=NC.descifrar(clave, texto)
            self.get(mensajeDescifrado, texto, clave)

        if tipo=='Analizar!':
            self.redirect('/atack')



application = webapp2.WSGIApplication([
                                      ('/', Home),
                                      ('/use', Use),
                                      ('/atack', Atack)
                                      ]
                                      ,debug=True)
