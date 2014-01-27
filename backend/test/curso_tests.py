# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from base import GAETestCase
from mock import Mock
from web.curso import rest
from web.curso.rest import Curso


class RestTests(GAETestCase):
    def test_salvar(self):
        rest.salvar('Python Pro', '13.33')
        lista = Curso.query().fetch()
        self.assertEqual(1, len(lista))
        curso = lista[0]
        self.assertEqual('Python Pro', curso.nome)
        self.assertEqual(13.33, curso.preco)

    def test_listar(self):
        cursos=[Curso(nome="Python para quem sabe Python",preco=323.45),
                Curso(nome="Python para quem estudou Java",preco=383.35)]
        ndb.put_multi(cursos)
        resp=Mock()
        rest.listar(resp)
        resp.write.assert_called_once_with('[{"preco": 323.45, "id": "1", "nome": "Python para quem sabe Python"}, {"preco": 383.35, "id": "2", "nome": "Python para quem estudou Java"}]')
