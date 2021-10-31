---
id: 3591
name: "ISU-HPC/mysql"
branch: "master"
tag: "5.7.21"
commit: "b5ba8e289667e04e87fb5c718606fc3b293102ac"
version: "dfe353aad821839bd835ac2785055714"
build_date: "2020-06-04T07:30:55.430Z"
size_mb: 364
size: 118747167
sif: "https://datasets.datalad.org/shub/ISU-HPC/mysql/5.7.21/2020-06-04-b5ba8e28-dfe353aa/dfe353aad821839bd835ac2785055714.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/mysql/5.7.21/2020-06-04-b5ba8e28-dfe353aa/
recipe: https://datasets.datalad.org/shub/ISU-HPC/mysql/5.7.21/2020-06-04-b5ba8e28-dfe353aa/Singularity
collection: ISU-HPC/mysql
---

# ISU-HPC/mysql:5.7.21

```bash
$ singularity pull shub://ISU-HPC/mysql:5.7.21
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

