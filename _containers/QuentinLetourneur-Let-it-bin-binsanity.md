---
id: 4599
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "binsanity"
commit: "647c7b5e55f98b734d8bcb0be2bbc1953b9bb875"
version: "d72f799eb63cbe93110b703d0811ddd7"
build_date: "2018-09-02T17:27:42.144Z"
size_mb: 2878
size: 854093855
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/binsanity/2018-09-02-647c7b5e-d72f799e/d72f799eb63cbe93110b703d0811ddd7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/binsanity/2018-09-02-647c7b5e-d72f799e/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/binsanity/2018-09-02-647c7b5e-d72f799e/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:binsanity

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:binsanity
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget subread python python-pip camlp4-extra gawk libgsl0-dev libgsl0-dev \
    sqlite3 libsqlite3-dev libz-dev m4 ocaml patch ocaml-native-compilers opam zip
    pip install biopython scipy scikit-learn pandas
    
	cd /home
    wget  http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz
    tar -xzf hmmer-3.1b2-linux-intel-x86_64.tar.gz
    rm hmmer-3.1b2-linux-intel-x86_64.tar.gz
    cd hmmer-3.1b2-linux-intel-x86_64
    ./configure
    make
    make install
    cd easel
    make install
    
	cd /home
    wget https://github.com/hyattpd/Prodigal/archive/v2.6.3.tar.gz
    tar -xzf v2.6.3.tar.gz
    rm v2.6.3.tar.gz
    cd Prodigal-2.6.3
    make install
    
	cd /home
    wget https://github.com/matsen/pplacer/releases/download/v1.1.alpha18/pplacer-linux-v1.1.alpha18-2-gcb55169.zip
    unzip pplacer-linux-v1.1.alpha18-2-gcb55169.zip
    rm pplacer-linux-v1.1.alpha18-2-gcb55169.zip
    cd pplacer-Linux-v1.1.alpha18-2-gcb55169
    mv guppy pplacer rppr /usr/local/bin
    
	cd /home
    pip install pysam matplotlib dendropy screamingbackpack
    wget https://github.com/Ecogenomics/CheckM/archive/v1.0.7.tar.gz
    tar -xzf v1.0.7.tar.gz
    rm v1.0.7.tar.gz
    cd CheckM-1.0.7
    python setup.py install
    wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz
    tar -xzf checkm_data_2015_01_16.tar.gz
    rm checkm_data_2015_01_16.tar.gz
    
	# directly modify the file because cannot be done dynamicly with checkm setRoot
    sed -i 's/"dataRoot": ""/"dataRoot": "\/home\/CheckM-1.0.7\/"/' /usr/local/lib/python2.7/dist-packages/checkm/DATA_CONFIG
    
	cd /home
    wget https://github.com/edgraham/BinSanity/archive/v0.2.6.1.tar.gz
    tar -xzf v0.2.6.1.tar.gz
    cd BinSanity-0.2.6.1
    sed -i 's/README.rst/README.md/' setup.py
    python setup.py install
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

