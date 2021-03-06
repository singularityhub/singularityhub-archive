---
id: 3333
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "rooting_nj"
commit: "d423db2699912cdaf2c70dee7c3a92a22353ade0"
version: "6f728f954c165ed117c1928a4d901d7c"
build_date: "2018-08-24T05:04:45.142Z"
size_mb: 899
size: 287383583
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/rooting_nj/2018-08-24-d423db26-6f728f95/6f728f954c165ed117c1928a4d901d7c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CompBio-TDU-Japan/containers/rooting_nj/2018-08-24-d423db26-6f728f95/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/rooting_nj/2018-08-24-d423db26-6f728f95/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:rooting_nj

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:rooting_nj
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: alpine

%post
    apk --update --no-cache add --virtual=build-deps ca-certificates build-base git
    apk --no-cache add libbz2 bash python3-dev python3 openjdk8 wget file
    pip3 install --upgrade pip
    pip3 install --upgrade setuptools
    LANG="en_US.UTF-8"
    pip3 install biopython
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-2.27-r0.apk
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-bin-2.27-r0.apk
    apk --no-cache add -v glibc-2.27-r0.apk
    apk --no-cache add -v glibc-bin-2.27-r0.apk
    export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
## mafft install
    wget https://mafft.cbrc.jp/alignment/software/mafft-7.394-without-extensions-src.tgz
    tar xfvz mafft-7.394-without-extensions-src.tgz
    rm mafft-7.394-without-extensions-src.tgz
    cd mafft-7.394-without-extensions/core
    make clean
    make -j 3
    make install
    cd /
    rm -r mafft-7.394-without-extensions
# EMBOSS install
    mkdir -p /usr/local/emboss
    wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz
    tar xfvz EMBOSS-6.6.0.tar.gz
    rm -f EMBOSS-6.6.0.tar.gz
    cd EMBOSS-6.6.0
    ./configure --without-x -prefix=/usr/local/emboss \
    --without-dbapi  --without-fastcgi  --without-ncbi-c  \
    --without-sss --without-internal --without-sssdb --without-gui
    make -j 3
    make install
    cd /
    rm -r EMBOSS-6.6.0
## PHYLIPNEW install
    wget ftp://emboss.open-bio.org/pub/EMBOSS/PHYLIPNEW-3.69.660.tar.gz
    tar xfvz PHYLIPNEW-3.69.660.tar.gz
    rm -rf PHYLIPNEW-3.69.660.tar.gz
    cd PHYLIPNEW-3.69.650
    ./configure --without-x -prefix=/usr/local/emboss
    make -j 3
    make install
    cd /
    rm -r PHYLIPNEW-3.69.650
    cp -a  /usr/local/emboss/bin/fprotdist /usr/local/bin/
    cp -a  /usr/local/emboss/bin/fneighbor /usr/local/bin/
    cp -a  /usr/local/emboss/lib/* /usr/local/lib/
    export PATH=$PATH:/usr/local/emboss/bin
## blast+ install
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.4.0/ncbi-blast-2.4.0+-x64-linux.tar.gz
    tar xfvz ncbi-blast-2.4.0+-x64-linux.tar.gz
    mv ncbi-blast-2.4.0+/bin/psiblast /usr/local/bin/
    mv ncbi-blast-2.4.0+/bin/blastdbcmd /usr/local/bin/
    mv ncbi-blast-2.4.0+/bin/makeblastdb /usr/local/bin/
## Rooting_NJ install
   git clone https://github.com/CompBio-TDU-Japan/Rooting_NJ.git
##clean
    rm glibc*.apk
    rm "/root/.wget-hsts"
    rm ncbi-blast-2.4.0+-x64-linux.tar.gz
    rm -r ncbi-blast-2.4.0+
    rm "/etc/apk/keys/sgerrand.rsa.pub"
    apk del build-deps
    rm -r /usr/glibc-compat/bin
    rm -r /usr/glibc-compat/sbin

%help

bio tools v1.7
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

