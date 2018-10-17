# hello-senzing-ibm-node-red

## Overview

This demonstration shows how to wrap Senzing with Python Flask to create a HTTP API and a simple application with Node-RED.

## Install and run service

These instructions will install and run the web services.

1. [Debian-based installation](doc/debian-based-installation.md) - For Ubuntu and [others](https://en.wikipedia.org/wiki/List_of_Linux_distributions#Debian-based)
1. [RPM-based installation](doc/rpm-based-installation.md) - For Red Hat, CentOS, openSuse and [others](https://en.wikipedia.org/wiki/List_of_Linux_distributions#RPM-based).

## Test

The following tests assume that the services are running.
To start and run the services, see either
[Debian-based "Run Services"](doc/debian-based-installation.md#run-services) or
[RPM-based "Run Services"](doc/rpm-based-installation.md#run-services).

For a future step, find the value of GIT_REPOSITORY_DIR.  Example:

```console
echo $GIT_REPOSITORY_DIR
```

### Test Senzing service

To test the Senzing service, open a web browser (e.g. FireFox, Chrome, Safari, MS Explorer, Opera) to
`http://localhost:5000/getVersion`, replacing `localhost` if needed.

### Test Node-RED service

To test the Node-Red service, open a web browser (e.g. FireFox, Chrome, Safari, MS Explorer, Opera) to
`http://localhost:1880`, replacing `localhost` if needed.

### Try Senzing-Node-RED

1. Load sample data:
    1. In a web browser, visit `http://localhost:1880/LoadG2`.
    1. In "Input file name (CSV)" field, enter `${GIT_REPOSITORY_DIR}/src/demo_g2_http_interface/data/SENZING.csv`. Replace GIT_REPOSITORY_DIR with the actual value.
    1. Click "Load G2" button.
    1. Wait a few minutes for the data load to complete.
        1. This may take 5 minutes.

1. Run the sample application:
    1. In a web browser, visit `http://localhost:1880/g2embed`
    1. In "Name:" field, enter "Marisol Smith" and press [Enter].
        1. This returns results of Senzing Entity Resolution showing that this person exists in three different source system.
    1. In "Search Results", click on the resolved entity "Marisol Smith".
        1. Shows the different records across the source systems: ADULT_SERVICES, WELFARE_WORK, and CHILD_WELFARE.
    1. Click on "Related Records".
        1. Shows disclosed relationship.
            1. Bill Smith is the father of Marisol Smith.
        1. Note:  This may not work on FireFox.
