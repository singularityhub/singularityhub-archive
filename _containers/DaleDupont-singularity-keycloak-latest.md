---
id: 872
name: "DaleDupont/singularity-keycloak"
branch: "master"
tag: "latest"
commit: "dd6c21c5540da72c8871db2e191ab4f2a95adf0c"
version: "2b7cb02213e680b9a13f79f1708286ed"
build_date: "2017-12-01T20:07:55.371Z"
size_mb: 1335
size: 387117087
sif: "https://datasets.datalad.org/shub/DaleDupont/singularity-keycloak/latest/2017-12-01-dd6c21c5-2b7cb022/2b7cb02213e680b9a13f79f1708286ed.simg"
url: https://datasets.datalad.org/shub/DaleDupont/singularity-keycloak/latest/2017-12-01-dd6c21c5-2b7cb022/
recipe: https://datasets.datalad.org/shub/DaleDupont/singularity-keycloak/latest/2017-12-01-dd6c21c5-2b7cb022/Singularity
collection: DaleDupont/singularity-keycloak
---

# DaleDupont/singularity-keycloak:latest

```bash
$ singularity pull shub://DaleDupont/singularity-keycloak:latest
```

## Singularity Recipe

```singularity
# Deploys the keycloak server
BootStrap: docker
From: ubuntu:latest

%environment

    DEBIAN_FRONTEND=noninteractive

%setup

    cp keycloak/keycloakAlt.sh ${SINGULARITY_ROOTFS}
    cp keycloak/keyPwdSing.sh ${SINGULARITY_ROOTFS}

%post

    # Download and install wget, unzip, and java
    apt-get update -y
    apt-get install -y --no-install-recommends apt-utils
    apt-get install -y wget unzip default-jre default-jdk iproute curl libxml2-utils 

    # Go to the srv directory
    cd /srv

    # Download and unzip Keycloak
    wget https://downloads.jboss.org/keycloak/3.4.0.Final/keycloak-3.4.0.Final.zip
    unzip keycloak-3.4.0.Final.zip
    rm keycloak-3.4.0.Final.zip

    mv /keycloakAlt.sh /srv/keycloakAlt.sh
    mv /keyPwdSing.sh /srv/keyPwdSing.sh

    # make the anchor
    # this file determines how much extra "free" space
    # will be made available on the container
    # the file is deleted at runtime to free the space
    # this free space is necessary for keycloak's database
    dd if=/dev/zero of=/srv/out.dat bs=1M count=512

    chmod a+rwx -R /srv
    umask 0


%runscript

    # Start keycloak when the container is run
    # the keycloakStart.sh script determines the local IP on which
    # the keycloak server should listen
    #exec /srv/keycloakStart.sh False CanDIG admin admin user user
    exec /srv/keycloakAlt.sh
```

## Collection

 - Name: [DaleDupont/singularity-keycloak](https://github.com/DaleDupont/singularity-keycloak)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

