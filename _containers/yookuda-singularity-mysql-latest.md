---
id: 11459
name: "yookuda/singularity-mysql"
branch: "master"
tag: "latest"
commit: "0a262b60577dc57b2234c2b506d2904cd9c959f9"
version: "3020d6c57139d7497bce28341426b5fb"
build_date: "2020-06-26T07:47:32.800Z"
size_mb: 1442.0
size: 468078623
sif: "https://datasets.datalad.org/shub/yookuda/singularity-mysql/latest/2020-06-26-0a262b60-3020d6c5/3020d6c57139d7497bce28341426b5fb.sif"
url: https://datasets.datalad.org/shub/yookuda/singularity-mysql/latest/2020-06-26-0a262b60-3020d6c5/
recipe: https://datasets.datalad.org/shub/yookuda/singularity-mysql/latest/2020-06-26-0a262b60-3020d6c5/Singularity
collection: yookuda/singularity-mysql
---

# yookuda/singularity-mysql:latest

```bash
$ singularity pull shub://yookuda/singularity-mysql:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer Yoshihiro Okuda
        Version    v1.0

%environment
    PATH=/usr/local/mysql/bin:$PATH
    export PATH

%post
    echo "Hello from inside the container"
    sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list
    sed -i.bak -e "s%http://security.ubuntu.com/ubuntu/%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list
    apt-get -y update
    apt-get -y upgrade
    apt-get -y install vim wget sudo less

    # install MySQL
    MYSQL_VERSION=5.6.46
    cd /usr/local/src
    wget http://ftp.jaist.ac.jp/pub/mysql/Downloads/MySQL-5.6/mysql-${MYSQL_VERSION}.tar.gz
    tar xzvf mysql-${MYSQL_VERSION}.tar.gz
    cd mysql-${MYSQL_VERSION}
    apt-get -y install cmake libncurses5-dev make gcc g++ libssl-dev
    mkdir /usr/local/boost
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
    -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/boost -DDEFAULT_CHARSET=utf8 \
    -DDEFAULT_COLLATION=utf8_general_ci \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DMYSQL_UNIX_ADDR=/usr/local/mysql/data/mysql.sock
    make -j 4 && make install

    apt-get -y install cpanminus
    cpanm File::Copy
    cpanm Sys::Hostname
    cpanm Data::Dumper

    rm -r /usr/local/src/*
```

## Collection

 - Name: [yookuda/singularity-mysql](https://github.com/yookuda/singularity-mysql)
 - License: None

