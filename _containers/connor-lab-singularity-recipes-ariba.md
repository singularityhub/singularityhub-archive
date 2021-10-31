---
id: 6950
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "ariba"
commit: "a43cefa7f62c25a6726a49f5634f285ba75ea6a9"
version: "78e3c33a5b393288cefa4c703faf9e10"
build_date: "2019-02-07T11:31:15.361Z"
size_mb: 1107
size: 453885983
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/ariba/2019-02-07-a43cefa7-78e3c33a/78e3c33a5b393288cefa4c703faf9e10.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/ariba/2019-02-07-a43cefa7-78e3c33a/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/ariba/2019-02-07-a43cefa7-78e3c33a/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:ariba

```bash
$ singularity pull shub://connor-lab/singularity-recipes:ariba
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest


%post
    yum -y update
    yum -y install epel-release
    yum install -y bzip2 bzip2-devel gcc gcc-c++ git ncurses-devel make unzip xz-devel zlib-devel
    yum install -y python36 python36-devel python36-setuptools

    easy_install-3.6 pip
  
    ## MUMmer 4 
    curl -fsSL 'https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz' | tar -xz -C /usr/local/bin
    cd /usr/local/bin/mummer-4.0.0beta2 && ./configure && make install
 
    ## Bowtie2
    curl -fsSL 'https://github.com/BenLangmead/bowtie2/releases/download/v2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip' -o /usr/local/bin/bowtie2-2.3.4.3.zip
    cd /usr/local/bin/ && unzip bowtie2-2.3.4.3.zip
    find /usr/local/bin/bowtie2-2.3.4.3-linux-x86_64 -type f -executable -exec ln -s {} /usr/local/bin \; 
    ## SPAdes
    curl -fsSL 'http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz' | tar -xz -C /usr/local/bin/
    find /usr/local/bin/SPAdes* -name "spades.py" -type f -executable -exec ln -s {} /usr/local/bin \;


    ## CD-HIT
    curl -fsSL 'https://github.com/weizhongli/cdhit/releases/download/V4.6.8/cd-hit-v4.6.8-2017-1208-source.tar.gz' | tar -xz -C /usr/local/bin
    cd /usr/local/bin/cd-hit-v4.6.8-2017-1208 && make && make install

    pip3 install ariba

%runscript
    exec ariba "$@"
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

