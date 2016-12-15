#! /usr/bin/python2.7
from __future__ import absolute_import

import commands
import time


def verifica_ruc_valido(ruc):
    multiplos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    new_ruc = ruc[:-1]
    divide = 11
    suma = 0

    for idx, val in enumerate(new_ruc):
        suma += int(val) * multiplos[idx]

    divicion = int(suma/divide)
    result = divide - (suma- divicion * divide)

    if result == 10:
        result = 0

    if result == 11:
        result = 1

    ruc_to_verificar = '%s%s' % (new_ruc, result)

    if ruc_to_verificar == ruc:
        return True
    else:
        return False

for ruc in range(20600000595, 20600999999):
    status = verifica_ruc_valido(str(ruc))
    print('%d : %s' % (ruc, status))
    if status:
        time.sleep(60)
        command = 'scrapy crawl rapipago -a ruc=%d' % ruc
        commands.getoutput(command)
