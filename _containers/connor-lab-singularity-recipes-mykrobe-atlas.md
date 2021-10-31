---
id: 6989
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "mykrobe-atlas"
commit: "d5710c095065a9aa78f89c03835bd96ff0ae8d01"
version: "5dce8dfe995489ef77b0ffa74bed2cb4"
build_date: "2019-06-17T19:35:29.690Z"
size_mb: 1006
size: 409239583
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mykrobe-atlas/2019-06-17-d5710c09-5dce8dfe/5dce8dfe995489ef77b0ffa74bed2cb4.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mykrobe-atlas/2019-06-17-d5710c09-5dce8dfe/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mykrobe-atlas/2019-06-17-d5710c09-5dce8dfe/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:mykrobe-atlas

```bash
$ singularity pull shub://connor-lab/singularity-recipes:mykrobe-atlas
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%post
    yum -y update
    yum -y install epel-release
    yum -y install gcc gcc-c++ git make wget zlib-devel 
    yum -y install python34 python34-devel python34-pip

    curl -fsSL 'https://repo.mongodb.org/yum/redhat/mongodb-org-3.0.repo' -o /etc/yum.repos.d/mongodb-org-3.0.repo

    yum install -y mongodb-org
    
    cd /usr/local/bin
    git clone --recursive -b geno_kmer_count https://github.com/phelimb/mccortex mccortex-geno_kmer_count
    cd mccortex-geno_kmer_count && make clean && make
    ln -s /usr/local/bin/mccortex-geno_kmer_count/bin/mccortex31 /usr/local/bin/

    cd /usr/local/bin
    git clone https://github.com/Mykrobe-tools/mykrobe-atlas-cli.git mykrobe-latest
    cd mykrobe-latest
    wget -O mykrobe-data.tar.gz http://s3.climb.ac.uk/mykrobe/mykrobe-data.tgz && tar -zxvf mykrobe-data.tar.gz && rm -fr src/mykrobe/data && mv mykrobe-data src/mykrobe/data
    pip3.4 install .

    curl -fsSL 'https://raw.githubusercontent.com/iqbal-lab/Mykrobe-predictor/master/scripts/json_to_tsv.py' -o /usr/local/bin/json_to_tsv.py
    chmod +x /usr/local/bin/json_to_tsv.py

    ln -s /usr/local/bin/mccortex31 /usr/bin/

%labels
    Maintainer m-bull
    Version mykrobe-atlas-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

