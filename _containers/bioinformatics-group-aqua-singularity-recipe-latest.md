---
id: 9764
name: "bioinformatics-group/aqua-singularity-recipe"
branch: "master"
tag: "latest"
commit: "2acf463905ac15c051f7a3a109974b8a13416bfb"
version: "e1f7bcdf3a684df6aff3ad174e6ca1f1"
build_date: "2020-04-24T22:56:19.791Z"
size_mb: 588
size: 249143327
sif: "https://datasets.datalad.org/shub/bioinformatics-group/aqua-singularity-recipe/latest/2020-04-24-2acf4639-e1f7bcdf/e1f7bcdf3a684df6aff3ad174e6ca1f1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bioinformatics-group/aqua-singularity-recipe/latest/2020-04-24-2acf4639-e1f7bcdf/
recipe: https://datasets.datalad.org/shub/bioinformatics-group/aqua-singularity-recipe/latest/2020-04-24-2acf4639-e1f7bcdf/Singularity
collection: bioinformatics-group/aqua-singularity-recipe
---

# bioinformatics-group/aqua-singularity-recipe:latest

```bash
$ singularity pull shub://bioinformatics-group/aqua-singularity-recipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: stretch
MirrorURL: http://ftp.ca.debian.org/debian/

%files
    norMD1_3.tar.gz
    mafft-6.611-without-extensions-src.tgz
    muscle3.7.tar.gz
    rascal1.34.tar.gz
    AQUA.tcl

%environment

%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get install -y curl gnupg2 build-essential
    apt-get install -y ca-certificates lsb-release apt-transport-https 
    curl --silent -o apt.gpg https://packages.sury.org/php/apt.gpg
    apt-key add /apt.gpg
    apt-get -qqq update
    apt-get -qqq upgrade
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
    dpkg-reconfigure --frontend noninteractive tzdata    
    apt-get -y install g++ perl tcl
    tar -xzf norMD1_3.tar.gz
    cd normd_noexpat
    make
    cp normd /usr/bin
    cp normd_sw /usr/bin
    cp normd_range /usr/bin
    cp normd_aln /usr/bin
    cp normd_subaln /usr/bin
    cp normd_aln1 /usr/bin
    cd ..
    tar -xzf mafft-6.611-without-extensions-src.tgz
    cd mafft-6.611-without-extensions
    cd core
    make clean
    make
    make install
    cd ../..   
    tar -xzf muscle3.7.tar.gz
    cd muscle3.7
    make
    cp muscle /usr/bin
    cd ..
    tar -xzf rascal1.34.tar.gz
    cd rascal1.34
    make
    cd cluspack
    make
    cd ..
    mkdir /usr/bin/rascal1.34
    cp tomsf /usr/bin/rascal1.34
    cp cluspack/cluspack /usr/bin/rascal1.34
    cp scan_seqerrs /usr/bin/rascal1.34
    cp realign_seqerrs /usr/bin/rascal1.34
    cp scan_blockerrs /usr/bin/rascal1.34
    cp realign_blockerrs /usr/bin/rascal1.34
    cp scan_orphanerrs /usr/bin/rascal1.34
    cp realign_orphanerrs /usr/bin/rascal1.34
    cp scan_coreblocks /usr/bin/rascal1.34
    cp realign_nonblock /usr/bin/rascal1.34
    cp totfa /usr/bin/rascal1.34
    sed -i 's/^RASCALPATH=.*$/RASCALPATH=\/usr\/bin\/rascal1.34/g' rascal
    sed -i 's/^CLUSPACKPATH=.*$/CLUSPACKPATH=\/usr\/bin\/rascal1.34/g' rascal
    cp rascal /usr/bin
    cd ..
    apt-get install tcl
    cp AQUA.tcl /usr/bin
    chmod 755 /usr/bin/AQUA.tcl

    apt-get update && apt-get install -y && \
	   apt-get install -y locales locales-all && \
            export LANGUAGE=en_US.UTF-8 && \
            export LANG=en_US.UTF-8 && \
            export LC_ALL=en_US.UTF-8 && \
            locale-gen en_US.UTF-8 && \
            dpkg-reconfigure locales
    rm -r /var/lib/apt/lists/*
    apt-get -yq purge curl gnupg2 build-essential ca-certificates lsb-release apt-transport-https g++
    apt-get -yq autoremove

%runscript
    echo "The following tools are available:"
    echo "\e[91mAQUA.tcl\033[0;0m"
    AQUA.tcl | sed -e 's/^/\t/'
    echo
    echo "\e[91mnormd\033[0;0m"
    normd 2>&1 >/dev/null | sed -e 's/^/\t/'
    echo
    echo "\e[91mmafft\033[0;0m"
    mafft --help 2>&1 >/dev/null | sed -e 's/^/\t/'
    echo
    echo "\e[91mmuscle\033[0;0m"
    muscle 2>&1 >/dev/null | sed -e 's/^/\t/'
    echo
    echo "\e[91mrascal\033[0;0m"
    rascal | sed -e 's/^/\t/'
```

## Collection

 - Name: [bioinformatics-group/aqua-singularity-recipe](https://github.com/bioinformatics-group/aqua-singularity-recipe)
 - License: [MIT License](https://api.github.com/licenses/mit)

