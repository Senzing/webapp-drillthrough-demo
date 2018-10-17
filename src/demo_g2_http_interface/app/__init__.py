# app/__init__.py

from flask import Flask
import cmd
import sys
import os
from G2Module import G2Module
from G2AnonModule import G2AnonModule
from G2AuditModule import G2AuditModule
from G2ProductModule import G2ProductModule
import G2Exception
import datetime
import os

g2_directory = os.environ.get("SENZING_DIR", "/opt/senzing")

# adds path to G2Module to System Path
sys.path.append("{0}/g2/python".format(g2_directory))

g2_initfile_location = "{0}/g2/python/G2Module.ini".format(g2_directory)

# Initialize the G2Module once per process. This will take a few seconds.
g2_module = G2Module('pyG2', g2_initfile_location, True)
g2_module.init()

g2_audit_module = G2AuditModule('pyG2Audit', g2_initfile_location, False)
g2_audit_module.init()

g2_product_module = G2ProductModule('pyG2Product', g2_initfile_location, False)
g2_product_module.init()

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

from app import views

# Load the config file
app.config.from_object('config')

# After all the modules are loaded let us know
print("Modules initialized correctly!\nTime :{0} ".format(datetime.datetime.now()))
