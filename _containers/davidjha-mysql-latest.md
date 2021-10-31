---
id: 12502
name: "davidjha/mysql"
branch: "master"
tag: "latest"
commit: "5809fcbb0c26343ee4d304a9cee88dff2fe6a566"
version: "5afae9aead509556b58e1eb150ceb4ee"
build_date: "2020-08-12T15:12:48.049Z"
size_mb: 364.0
size: 118747167
sif: "https://datasets.datalad.org/shub/davidjha/mysql/latest/2020-08-12-5809fcbb-5afae9ae/5afae9aead509556b58e1eb150ceb4ee.sif"
url: https://datasets.datalad.org/shub/davidjha/mysql/latest/2020-08-12-5809fcbb-5afae9ae/
recipe: https://datasets.datalad.org/shub/davidjha/mysql/latest/2020-08-12-5809fcbb-5afae9ae/Singularity
collection: davidjha/mysql
---

# davidjha/mysql:latest

```bash
$ singularity pull shub://davidjha/mysql:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mysql:5.7.21

%help
MariaDB (MySQL) server.
Documentation: https://www.hpc.iastate.edu/guides/containers/mysql-server


%labels
    AUTHOR Robert Grandin rgrandin@iastate.edu
    MAINTAINER Iowa State University High-Performance Computing Group
    VERSION  v1.0


%setup
    touch ${SINGULARITY_ROOTFS}/my.cnf
    touch ${SINGULARITY_ROOTFS}/mysqlrootpw
    touch ${SINGULARITY_ROOTFS}/usr/local/bin/create_remote_admin_user.sh


%files
    my.cnf /my.cnf
    mysqlrootpw /mysqlrootpw
    create_remote_admin_user.sh /usr/local/bin/create_remote_admin_user.sh


%post
    chmod +x /usr/local/bin/create_remote_admin_user.sh


%runscript
    # Check that mysql directory is writeable.  If not, inform user of documentation and exit.
    touch /var/lib/mysql/write_test
    if [ ! -f /var/lib/mysql/write_test ]
    then
        echo '/var/lib/mysql is not writable.  Please see https://www.hpc.iastate.edu/guides/containers/mysql-server'
        echo 'for instructions on bind-mounting host directories into this container.'
        exit 1
    fi
    rm -f /var/lib/mysql/write_test

    # Check for .my.cnf, and use default if necessary
    if [ ! -f ${HOME}/.my.cnf ]
    then
        echo "Copying my.cnf to ${HOME}"
        cp /my.cnf ${HOME}/.my.cnf
    else
        echo "${HOME}/.my.cnf already exists.  Using that version."
    fi

    # Check for .mysqlrootpw, and use default if necessary
    if [ ! -f ${HOME}/.mysqlrootpw ]
    then
        echo "Copying mysqlrootpw to ${HOME}"
        cp /mysqlrootpw ${HOME}/.mysqlrootpw
    else
        echo "${HOME}/.mysqlrootpw already exists.  Using that version."
    fi

    # Check for initialization
    if [ ! -d /var/lib/mysql/mysql ]
    then
        echo "Initializing mysqld"
        mysqld --initialize  --init-file=${HOME}/.mysqlrootpw
    fi

    # Finally, launch mysqld
    echo ""
    echo "Start mysqld"
    mysqld  --init-file=${HOME}/.mysqlrootpw &
```

## Collection

 - Name: [davidjha/mysql](https://github.com/davidjha/mysql)
 - License: None

