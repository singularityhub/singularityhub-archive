---
id: 11292
name: "pescobar/mysql-singularity-container"
branch: "master"
tag: "latest"
commit: "9efe4a8fda2def6c7256b5df8639b7779d138bad"
version: "7dd35962c6c7b5d77592d656090278c248050a91bb5f8ffdfb4f90aea80be3be"
build_date: "2020-05-29T15:00:59.214Z"
size_mb: 113.28515625
size: 118788096
sif: "https://datasets.datalad.org/shub/pescobar/mysql-singularity-container/latest/2020-05-29-9efe4a8f-7dd35962/7dd35962c6c7b5d77592d656090278c248050a91bb5f8ffdfb4f90aea80be3be.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/mysql-singularity-container/latest/2020-05-29-9efe4a8f-7dd35962/
recipe: https://datasets.datalad.org/shub/pescobar/mysql-singularity-container/latest/2020-05-29-9efe4a8f-7dd35962/Singularity
collection: pescobar/mysql-singularity-container
---

# pescobar/mysql-singularity-container:latest

```bash
$ singularity pull shub://pescobar/mysql-singularity-container:latest
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
    # in the sciCORE cluster $HOSNTNAME points to the internal cluster network
    # so by default mysql is only listening in the internal cluster network
    mysqld  --init-file=${HOME}/.mysqlrootpw --bind-address=${HOSTNAME} &
```

## Collection

 - Name: [pescobar/mysql-singularity-container](https://github.com/pescobar/mysql-singularity-container)
 - License: None

