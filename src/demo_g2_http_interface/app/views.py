# views.py

from flask import render_template
from G2AuditModule import G2AuditModule
import G2Exception
import json
import urllib
from flask import request
from flask import jsonify
from app import app

# Importing g2_module from the __init__ function here
from app import g2_module
from app import g2_audit_module
from app import g2_product_module


@app.route('/')
def index():
    return render_template("index.html", message="home directory")


@app.route('/about')
def about():
    return render_template("index.html", message="about end point")


@app.route('/initializeG2')
def initializeG2():
    return render_template("index.html", message="init end point")


@app.route('/addRecord')
def addRecord():
    return render_template("index.html", message="add record")


@app.route('/addRecordStub')
def addRecordStub():
    requestParams = str(request.args.get('requestParams'))
    jsonString = requestParams
    jsonData = json.loads(jsonString)
    jsonDataSource = jsonData['DATA_SOURCE']
    jsonRecordID = jsonData['RECORD_ID']

    recordID = str(jsonRecordID)
    sourceID = recordID
    dataSourceCode = str(jsonDataSource)
    ret = g2_module.addRecord(dataSourceCode, sourceID, jsonString, recordID)
    messsage = ""
    if ret == 0:
        message = 'Record added successfully.'
    else:
        message = 'ERROR: G2Module processing error!'
    return render_template("index.html", message=message)


@app.route('/searchRecord')
def searchRecord():
    requestParams = str(request.args.get('requestParams'))

    jsonString = requestParams
    ret = ""
    ret = g2_module.searchByAttributes(jsonString)

    messsage = ""

    return render_template("index.html", message=ret)


@app.route('/getSummaryData')
def getSummaryData():
    ret = ""
    ret = g2_audit_module.getSummaryData()

    ret2 = str(json.dumps(ret))
    message = ""
    return render_template("index.html", message=ret2)


@app.route('/purgeRepository')
def purgeRepository():
    ret = g2_module.purgeRepository()
    return render_template("index.html", message=ret)


@app.route('/getEntityByID')
def getEntityByID():
    entityid = int(request.args.get('entityid'))
    ret = g2_module.getEntityByEntityID(entityid)
    return render_template("index.html", message=ret)


@app.route('/getEntities')
def getEntities():

    '''
# The following function throws an error in G2, we currectly do this getAuditReport using Node-red, to be fixed later.
    '''

    datasource1 = str(request.args.get('datasource1'))
    datasource2 = str(request.args.get('datasource2'))
    matchlevel = str(request.args.get('matchlevel'))

    fromDataSource = 'TEST'
    toDataSource = 'TEST'
    matchLevels = 1

    ret = audit_module.getAuditReport(fromDataSource, toDataSource, matchLevels)
    print("audit report called")

    # ret = g2_audit_module.getAuditReport('TEST','TEST',1)
    print(ret)
    return render_template("index.html", message="ret")


@app.route('/getVersion')
def getVersion():
    versionVariable = json.dumps(g2_product_module.version())
    return render_template("index.html", message=versionVariable)
