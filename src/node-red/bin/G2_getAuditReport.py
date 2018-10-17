from G2AuditModule import G2AuditModule
import G2Exception
import sys
import os

g2_directory = os.environ.get("SENZING_DIR", "/opt/senzing")
g2_initfile_location = "{0}/g2/python/G2Module.ini".format(g2_directory)

#Using loaded sample data in /opt/senzing/g2/demo/
fromDataSource = sys.argv[1]
toDataSource = sys.argv[2]
matchLevels = int(sys.argv[3])

#G2Module.ini path correct? i.e. must be able to find it
audit_module = G2AuditModule('pyG2Audit', g2_initfile_location, False)

audit_module.init()

#Call for PEOPLE -> COMPANIES
ret=audit_module.getAuditReport(fromDataSource, toDataSource, matchLevels)

print(ret)

audit_module.destroy()

