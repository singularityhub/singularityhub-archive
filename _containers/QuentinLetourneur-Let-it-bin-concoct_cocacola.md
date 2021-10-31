---
id: 4613
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "concoct_cocacola"
commit: "647c7b5e55f98b734d8bcb0be2bbc1953b9bb875"
version: "5cb025b8ad0282ae12c0a879fb9cbcd3"
build_date: "2018-09-02T17:27:42.152Z"
size_mb: 1092
size: 418054175
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/concoct_cocacola/2018-09-02-647c7b5e-5cb025b8/5cb025b8ad0282ae12c0a879fb9cbcd3.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/concoct_cocacola/2018-09-02-647c7b5e-5cb025b8/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/concoct_cocacola/2018-09-02-647c7b5e-5cb025b8/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:concoct_cocacola

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:concoct_cocacola
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%files
    bin/cluster_to_fasta.py
    bin/fasta.py

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget zip gawk build-essential python python-pip gsl-bin libgsl0-dev libblas-dev liblapack-dev
    
    cd /home
    wget https://github.com/BinPro/CONCOCT/archive/0.4.0.tar.gz
    tar -xzf 0.4.0.tar.gz
    pip install bcbio-gff biopython distribute nose pandas pysam scikit-learn cvxopt
    cd CONCOCT-0.4.0
    make
    python setup.py install
    cp -r scripts/* /usr/local/bin
    
    cd /home
    
    wget https://www.dropbox.com/s/ciebt2y5h7pb9r2/COCACOLA-python.zip?dl=0
    unzip COCACOLA-python.zip?dl=0
    rm COCACOLA-python.zip?dl=0
    cd COCACOLA-python
    rm -r data
    sed -i '1s/^/#! \/usr\/bin\/env python\n/' cocacola.py
    chmod +x cocacola.py
    ln -s /home/COCACOLA-python/cocacola.py /usr/local/bin/cocacola.py
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

