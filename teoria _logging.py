#!/home/paco/py3/bin/python
import logging

my_logger = logging.getLogger()
#my_handler = logging.FileHandler("temp.log")
my_handler = logging.StreamHandler()
my_logger.addHandler(my_handler)
#logging.basicConfig(level=logging.DEBUG)
my_logger.setLevel(logging.DEBUG)
a = 1
b = 2
c = a + b
#f.write(f' show {c} '.center(20, '='))
texto = "algo muy largo para nada"

my_logger.debug(f"debug message {a}")
my_logger.info(f"info {b}")
my_logger.warning(f"warning {c}")
my_logger.error(f"error {c+1}")
my_logger.critical(f"Critical {c+2} ")


"""
logging.debug(f"debug message {a}")
logging.info(f"info {b}")
logging.warning(f"warning {c}")
logging.error(f"error {c+1}")
logging.critical(f"Critical {c+2} ")
"""

