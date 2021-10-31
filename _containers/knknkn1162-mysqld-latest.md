---
id: 9521
name: "knknkn1162/mysqld"
branch: "master"
tag: "latest"
commit: "fc4a7e05553ea11f0e93537ddad6b3f3a622e152"
version: "a13fb7da0205b44ba4140e0e85868832"
build_date: "2021-02-19T03:18:54.533Z"
size_mb: 206
size: 62238751
sif: "https://datasets.datalad.org/shub/knknkn1162/mysqld/latest/2021-02-19-fc4a7e05-a13fb7da/a13fb7da0205b44ba4140e0e85868832.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/knknkn1162/mysqld/latest/2021-02-19-fc4a7e05-a13fb7da/
recipe: https://datasets.datalad.org/shub/knknkn1162/mysqld/latest/2021-02-19-fc4a7e05-a13fb7da/Singularity
collection: knknkn1162/mysqld
---

# knknkn1162/mysqld:latest

```bash
$ singularity pull shub://knknkn1162/mysqld:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
# Fork from ISU-HPC/mysql, because The error occurs, `innodb: Table `mysql`.`innodb_table_stats` not found`, which is bug with above mysql:5.6.
From: mysql:5.5

%help
MariaDB (MySQL) server.


%labels
    AUTHOR Kenta Nakajima knknkn1162@gmail.com
    MAINTAINER Kenta Nakajima
    VERSION  v1.0

%setup
    touch ${SINGULARITY_ROOTFS}/my.cnf
    touch ${SINGULARITY_ROOTFS}/mysqlrootpw
    touch ${SINGULARITY_ROOTFS}/usr/local/bin/create_remote_admin_user.sh


%files
    assets/my.cnf /my.cnf
    assets/mysqlrootpw /mysqlrootpw
    assets/create_remote_admin_user.sh /usr/local/bin/create_remote_admin_user.sh


%post
    chmod +x /usr/local/bin/create_remote_admin_user.sh
    echo "export DATADIR=/var/lib/mysql" >> $SINGULARITY_ENVIRONMENT
    echo "export MYSQL_PORT=3306" >> $SINGULARITY_ENVIRONMENT


%runscript
    # Check that mysql directory is writeable.  If not, inform user of documentation and exit.
    touch ${DATADIR}/write_test
    if [ ! -f ${DATADIR}/write_test ]
    then
        echo '/var/lib/mysql is not writable.  Please see https://www.hpc.iastate.edu/guides/containers/mysql-server'
        echo 'for instructions on bind-mounting host directories into this container.'
        exit 1
    fi
    rm -f ${DATADIR}/write_test

    # copy setting files
    cp /my.cnf ${HOME}/.my.cnf
    cp /mysqlrootpw ${HOME}/.mysqlrootpw

    # Check for initialization
    if [ ! -d ${DATADIR}/mysql ]
    then
        echo "Initializing mysqld"
        mysql_install_db --basedir=/usr/local/mysql --datadir=${DATADIR}
    fi

    # Finally, launch mysqld
    echo "Start mysqld"
    mysqld  --init-file=${HOME}/.mysqlrootpw --port=${MYSQL_PORT} &
```

## Collection

 - Name: [knknkn1162/mysqld](https://github.com/knknkn1162/mysqld)
 - License: None

