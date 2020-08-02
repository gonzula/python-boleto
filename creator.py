#!/usr/bin/env python3

import os
from datetime import date

from pyboleto.bank.bradesco import BoletoBradesco
from pyboleto.pdf import BoletoPDF

b = BoletoBradesco()
b.data_documento = date(2020, 6, 10)
b.data_vencimento = date(2020, 6, 15)
b.valor_documento = '123.45'
b.agencia_cedente = '490'
b.conta_cedente = '20440'
b.cedente_endereco = 'Ribeirão Preto - SP Av. Presidente Vargas, 1265'
b.sacado = ['Mercadinho da Jurema', 'Avenida Jurema']
b.instrucoes = 'Pagar até a data de vencimento'
b.nosso_numero = '98765'
b.cedente = 'LIBER CAPITAL LTDA'
b.cedente_documento = '26.961.015/0001-00'
b.numero_documento = '321654'
b.carteira = '9'
b.acrescimo = '3.14'

path = '/Users/gonzo/Downloads/boleto.pdf'
with open(path, 'wb') as fout:
    pdf = BoletoPDF(fout)
    pdf.drawBoleto(b)
    pdf.save()
os.system(f'open {path}')
