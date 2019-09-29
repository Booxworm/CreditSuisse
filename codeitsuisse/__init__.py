from flask import Flask;
#import os

app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.chessgame
import codeitsuisse.routes.encryption


#directory = os.getcwd()
#for file in os.listdir(directory):
#    filename = os.fsdecode(file)
#    if filename.endswith(".py"): 
#        mod = "codeitsuisse.routes." + filename[:-3]
#	import mod
#        continue
#    else:
#        continue



