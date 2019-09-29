from flask import Flask;
#import os

app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.chessgame
import codeitsuisse.routes.encryption
import codeitsuisse.routes.exponent
import codeitsuisse.routes.lottery


#import importlib
#    modnames = ["square", "chess", "math"]
#    for lib in modnames:
#        globals()[lib] = importlib.import_module(lib)

#directory = os.getcwd()
#for file in os.listdir(directory):
#    filename = os.fsdecode(file)
#    if filename.endswith(".py"):
#        mod = "codeitsuisse.routes." + filename[:-3]
#	import mod
#        continue
#    else:
#        continue
