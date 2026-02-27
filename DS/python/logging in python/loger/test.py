from logger import logging

def add(a,b):
    logging.debug('the addition is taking place')
    return a+b

logging.debug('the addition is taking place')
add(10,15)
