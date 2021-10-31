---
id: 2596
name: "ISU-HPC/mysql"
branch: "master"
tag: "latest"
commit: "b18d7c8ce93ca26133b291d819a273c319f3748f"
version: "7821837f450e8562d99796f721525c89"
build_date: "2021-04-16T21:45:34.990Z"
size_mb: 364
size: 118747167
sif: "https://datasets.datalad.org/shub/ISU-HPC/mysql/latest/2021-04-16-b18d7c8c-7821837f/7821837f450e8562d99796f721525c89.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/mysql/latest/2021-04-16-b18d7c8c-7821837f/
recipe: https://datasets.datalad.org/shub/ISU-HPC/mysql/latest/2021-04-16-b18d7c8c-7821837f/Singularity
collection: ISU-HPC/mysql
---

# ISU-HPC/mysql:latest

```bash
$ singularity pull shub://ISU-HPC/mysql:latest
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

 - Name: [ISU-HPC/mysql](https://github.com/ISU-HPC/mysql)
 - License: None

