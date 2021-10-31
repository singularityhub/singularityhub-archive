---
id: 6957
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "iva"
commit: "2583535411903625da9ca664dd7548537bbbc2da"
version: "f53dc752c20f00359f831145524bf66c"
build_date: "2019-02-07T15:45:22.876Z"
size_mb: 676
size: 187789343
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/iva/2019-02-07-25835354-f53dc752/f53dc752c20f00359f831145524bf66c.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/iva/2019-02-07-25835354-f53dc752/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/iva/2019-02-07-25835354-f53dc752/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:iva

```bash
$ singularity pull shub://connor-lab/singularity-recipes:iva
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%environment
    PATH=$PATH:/usr/local/bin/MUMmer3.23
    export PATH

%post
    apk update
    apk upgrade
    apk add bash bzip2-dev g++ gcc libc-dev make ncurses-dev openjdk8-jre-base perl xz-dev zlib-dev
    apk add python3 python3-dev py3-pip
    
    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 -O /tmp/samtools.tar.bz2
    cd /tmp
    tar xvjf samtools.tar.bz2
    cd samtools-1.9 && ./configure && make && make install

    wget 'https://downloads.sourceforge.net/project/smalt/smalt-0.7.6-static.tar.gz' -O /tmp/smalt-0.7.6-static.tar.gz
    cd /tmp && tar xvzf smalt-0.7.6-static.tar.gz
    cd smalt-0.7.6 && ./configure && make && make install

    wget https://github.com/refresh-bio/KMC/releases/download/v3.1.0/KMC3.1.0.linux.tar.gz -O /tmp/KMC3.1.0.linux.tar.gz
    cd /tmp && tar xvzf KMC3.1.0.linux.tar.gz
    mv kmc* /usr/local/bin

    wget https://github.com/tcsh-org/tcsh/archive/cvs2git-20170131.tar.gz -O /tmp/cvs2git-20170131.tar.gz
    cd /tmp && tar xvzf cvs2git-20170131.tar.gz
    cd tcsh-cvs2git-20170131 && ./configure && make && make install
    ln -s /usr/local/bin/tcsh /usr/local/bin/csh

    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip -O /usr/local/bin/Trimmomatic-0.38.zip
    cd /usr/local/bin && unzip Trimmomatic-0.38.zip
    ln -s /usr/local/bin/Trimmomatic-0.38/trimmomatic-0.38.jar /usr/local/bin

    wget https://downloads.sourceforge.net/project/mummer/mummer/3.23/MUMmer3.23.tar.gz -O /usr/local/bin/MUMmer3.23.tar.gz
    cd /usr/local/bin && tar xvzf MUMmer3.23.tar.gz
    cd MUMmer3.23 && make && make install 

    export PATH=$PATH:/usr/local/bin/MUMmer3.23

    pip3 install iva
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

