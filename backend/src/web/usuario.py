# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton import router


def index(_handler):
    path = router.to_path(salvar, 'Renzo', 'Nuccitelli')
    _handler.redirect(path)


def salvar(_resp, nome, sobrenome):
    _resp.write("Olá %s %s" % (nome, sobrenome))