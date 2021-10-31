---
id: 3561
name: "ucr-singularity/asterixdb"
branch: "master"
tag: "latest"
commit: "0cd946f590b40086cb0730bd546bc20449aa3e0b"
version: "98546ff6ba6822c867338bfcf6b22dc8"
build_date: "2018-08-28T03:21:34.326Z"
size_mb: 3547
size: 1008467999
sif: "https://datasets.datalad.org/shub/ucr-singularity/asterixdb/latest/2018-08-28-0cd946f5-98546ff6/98546ff6ba6822c867338bfcf6b22dc8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/asterixdb/latest/2018-08-28-0cd946f5-98546ff6/
recipe: https://datasets.datalad.org/shub/ucr-singularity/asterixdb/latest/2018-08-28-0cd946f5-98546ff6/Singularity
collection: ucr-singularity/asterixdb
---

# ucr-singularity/asterixdb:latest

```bash
$ singularity pull shub://ucr-singularity/asterixdb:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7.5.1804

%help
Singularity container for the 0.9.4 snapshot of AsterixDB

This environment utilizes the config and log files within your home directory.
If you want to change the config of AsterixDB, use the files in /opt/asterix/asterixdb-files/conf.
Logs for the program are located in /opt/asterix/asterixdb-files/logs.
Data files for the database are located in /opt/asterix/asterixdb-files/data.

Files located in the asterix user home directory under /opt/asterix can be changed freely, however
any other files located within the singularity instance are immutable.

%post
    yum -y update

    # Installs the requirements for building AsterixDB
    yum -y install git
    yum -y install java-1.8.0-openjdk-devel
    yum -y install centos-release-scl
    yum -y install rh-maven35
    yum -y install iproute
    yum -y install net-tools

    # Clones the AsterixDB repository to /opt
    cd /opt
    git clone https://github.com/apache/asterixdb.git

    # Sets the environment variables for maven
    export PATH="/opt/rh/rh-maven35/root/usr/bin:${PATH:-/bin:/usr/bin}"
    export MANPATH="/opt/rh/rh-maven35/root/usr/share/man:${MANPATH}"
    export PYTHONPATH="/opt/rh/rh-maven35/root/usr/lib/python2.7/site-packages${PYTHONPATH:+:}${PYTHONPATH:-}"
    export JAVACONFDIRS="/opt/rh/rh-maven35/root/etc/java${JAVACONFDIRS:+:}${JAVACONFDIRS:-}"
    export XDG_CONFIG_DIRS="/opt/rh/rh-maven35/root/etc/xdg:${XDG_CONFIG_DIRS:-/etc/xdg}"
    export XDG_DATA_DIRS="/opt/rh/rh-maven35/root/usr/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"

    # Builds AsterixDB
    cd /opt/asterixdb
    mvn clean package -DskipTests

    # Chowns the /opt/asterixdb folder to user with uid and gid 8889
    chown -R 8889:8889 /opt/asterixdb

%environment
    umask 022
```

## Collection

 - Name: [ucr-singularity/asterixdb](https://github.com/ucr-singularity/asterixdb)
 - License: None

