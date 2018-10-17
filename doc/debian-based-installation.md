# Debian-based installation

The following instructions are meant to be "copy-and-paste" to install and demonstrate.
If a step requires you to think and make a decision, it will be prefaced with :warning:.

The instructions have been tested against a bare
[ubuntu-18.04.1-server-amd64.iso](http://cdimage.ubuntu.com/ubuntu/releases/bionic/release/ubuntu-18.04.1-server-amd64.iso)
image.

## Overview

1. [Install prerequisites](#prerequisites)
1. [Set environment variables](#set-environment-variables)
1. [Clone repository](#clone-repository)
1. [Install](#install)
1. [Customize](#customize)
1. [Run services](#run-services)
1. [Clean up](#clean-up)

## Prerequisites

These programs will be used in the installation and demonstration of
[Senzing](http://senzing.com) and
[Node-RED](https://nodered.org/).
They need to be installed first.

1. APT installs

    ```console
    sudo apt update
    sudo apt -y install git
    ```

## Set Environment variables

1. :warning: Set environment variables.
   These variables may be modified, but do not need to be modified.
   The variables are used throughout the installation procedure.

    ```console
    export GIT_ACCOUNT=docktermj
    export GIT_REPOSITORY=hello-senzing-ibm-node-red
    export SENZING_DEMO_URL="http://localhost:5000"
    export SENZING_DIR=/opt/senzing
    ```

1. Synthesize environment variables.

    ```console
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    export GIT_REPOSITORY_URL="https://github.com/${GIT_ACCOUNT}/${GIT_REPOSITORY}.git"
    export FLASK_APP=${GIT_REPOSITORY_DIR}/src/demo_g2_http_interface/run.py
    export LD_LIBRARY_PATH=${SENZING_DIR}/g2/lib:${SENZING_DIR}/g2/lib/debian:$LD_LIBRARY_PATH
    export PYTHONPATH=${SENZING_DIR}/g2/python
    ```

## Clone repository

1. Get repository.

    ```console
    mkdir --parents ${GIT_ACCOUNT_DIR}
    cd  ${GIT_ACCOUNT_DIR}
    git clone ${GIT_REPOSITORY_URL}
    ```

## Install

1. APT installs

    ```console
    sudo xargs apt -y install < ${GIT_REPOSITORY_DIR}/src/apt-packages.txt
    ```

1. NPM installs

    :warning: If using earlier Linux distributions, be sure that `node --version` shows `v5.0.0` or greater.

    ```console
    cd ${GIT_REPOSITORY_DIR}/src/node-red
    sudo npm install --unsafe-perm
    ```

1. PIP installs

    ```console
    sudo pip install -r ${GIT_REPOSITORY_DIR}/src/demo_g2_http_interface/requirements.txt
    ```

1. Download [Senzing_API.tgz](https://s3.amazonaws.com/public-read-access/SenzingComDownloads/Senzing_API.tgz).

    ```console
    curl -X GET \
      --output ${GIT_REPOSITORY_DIR}/Senzing_API.tgz \
      https://s3.amazonaws.com/public-read-access/SenzingComDownloads/Senzing_API.tgz
    ```

1. Create directory for Senzing.

    ```console
    sudo mkdir ${SENZING_DIR}
    ```

1. Uncompress `Senzing_API.tgz` into Senzing directory.

    ```console
    sudo tar \
      --extract \
      --verbose \
      --owner=root \
      --group=root \
      --no-same-owner \
      --no-same-permissions \
      --directory=${SENZING_DIR} \
      --file=${GIT_REPOSITORY_DIR}/Senzing_API.tgz
    ```

1. Change permissions for database.

    ```console
    sudo chmod -R 777 ${SENZING_DIR}/g2/sqldb
    ````

## Customize

1. Copy G2 configuration file to accommodate demo data.

    ```console
    sudo cp ${GIT_REPOSITORY_DIR}/src/g2/g2config.json ${SENZING_DIR}/g2/python/g2config.json
    ```

## Run Services

1. In a separate console, run Senzing service.
    1. Set environment variables.
        1. See [Set Environment variables](#set-environment-variables).
    1. Run [Flask](http://flask.pocoo.org/)

        ```console
        cd ${GIT_REPOSITORY_DIR}/src/demo_g2_http_interface
        flask run --host=0.0.0.0
        ```

1. In a separate console, run Node-RED service.
    1. Set environment variables.
        1. See [Set Environment variables](#set-environment-variables).
    1. Run [Node-Red](https://nodered.org/)

        ```console
        node-red "${GIT_REPOSITORY_DIR}/src/node-red/flows/flows.json"
        ```

1. [Test the services](../README.md#test).

## Clean up

After the demonstration is complete,
you may want to remove all files used in the demonstration.

1. Remove all files.

    ```console
    sudo rm -rf ${SENZING_DIR}
    rm -rf ${GIT_REPOSITORY_DIR}
    ```
