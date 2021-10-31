---
id: 6041
name: "ResearchIT/Scanfold"
branch: "master"
tag: "latest"
commit: "2c0c9b480f42f29a907c0ae802bac1b987eb7c18"
version: "9b8d0b18bad4f87206c9e829500857c3"
build_date: "2019-05-02T19:59:05.855Z"
size_mb: 996
size: 345993247
sif: "https://datasets.datalad.org/shub/ResearchIT/Scanfold/latest/2019-05-02-2c0c9b48-9b8d0b18/9b8d0b18bad4f87206c9e829500857c3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/Scanfold/latest/2019-05-02-2c0c9b48-9b8d0b18/
recipe: https://datasets.datalad.org/shub/ResearchIT/Scanfold/latest/2019-05-02-2c0c9b48-9b8d0b18/Singularity
collection: ResearchIT/Scanfold
---

# ResearchIT/Scanfold:latest

```bash
$ singularity pull shub://ResearchIT/Scanfold:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post
    yum -y update
    yum -y install epel-release wget git gcc-c++ zlib-devel make which
    yum -y install python36 python36-devel
    yum -y install python34-pip python34-devel
    wget https://bootstrap.pypa.io/get-pip.py
    python36 get-pip.py
    python36 -m pip install biopython
    python36 -m pip install numpy
    python36 -m pip install pybigwig
    python36 -m pip install requests
    python3.4 -m pip install biopython numpy requests

    # Install ViennaRNA & Python bindings
    if [ ! -f /usr/bin/RNAfold ];
    then
        wget https://www.tbi.univie.ac.at/RNA/download/epel/epel_7/perl-rna-2.4.11-1.x86_64.rpm
        wget https://www.tbi.univie.ac.at/RNA/download/epel/epel_7/viennarna-2.4.11-1.x86_64.rpm
        wget https://www.tbi.univie.ac.at/RNA/download/epel/epel_7/python3-rna-2.4.11-1.x86_64.rpm
        yum -y install viennarna-2.4.11-1.x86_64.rpm perl-rna-2.4.11-1.x86_64.rpm python3-rna-2.4.11-1.x86_64.rpm
    fi

    # Install RNAstructure 
    if [ ! -d /opt/rnastructure ];
    then
        mkdir -p /opt/rnastructure
        wget http://rna.urmc.rochester.edu/Releases/current/RNAstructureSource.tgz
        tar xzvf RNAstructureSource.tgz -C /opt/rnastructure
        pushd /opt/rnastructure/RNAstructure
        make ct2dot
        popd
    fi

    # Install ScanFold
    if [ ! -d /opt/scanfold ]
    then
        mkdir -p /opt/scanfold
        git clone https://github.com/moss-lab/ScanFold.git /opt/scanfold
        pushd /opt/scanfold
        git checkout master
        popd
    else
        pushd /opt/scanfold
        git checkout master
        git pull
        popd
    fi
 
%environment
    export PATH=/opt/rnastructure/RNAstructure/exe:/opt/scanfold:$PATH
    export DATAPATH=/opt/rnastructure/RNAstructure/data_tables

%runscript
    exec python36 $@

%apprun scan
    exec python3.4 /opt/scanfold/ScanFold-Scan_Webserver.py $@

%apprun fold
    exec python36 /opt/scanfold/ScanFold-Fold_spinoff.py $@

%help
Run this container by specifying the scan or fold step:
e.g.
$ singularity run shub://ResearchIT/scanfold fold -i input.tsv ...
```

## Collection

 - Name: [ResearchIT/Scanfold](https://github.com/ResearchIT/Scanfold)
 - License: None

