---
id: 6995
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "shiver_init"
commit: "b688e9001e40f834d33f20fb4734077c5f7a21be"
version: "35d4521cd4351cdc5076db0155873080"
build_date: "2019-02-07T19:57:01.397Z"
size_mb: 1437
size: 520237087
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/shiver_init/2019-02-07-b688e900-35d4521c/35d4521cd4351cdc5076db0155873080.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/shiver_init/2019-02-07-b688e900-35d4521c/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/shiver_init/2019-02-07-b688e900-35d4521c/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:shiver_init

```bash
$ singularity pull shub://connor-lab/singularity-recipes:shiver_init
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.5.1804

%post
    yum install -y epel-release
    yum -y update
    yum install -y git make
    yum install -y bc bzip2 bzip2-devel gcc ncurses-devel java-1.8.0-openjdk-headless unzip xz-devel zlib-devel
    yum install -y python-devel python2-pip
    yum install -y python36 python36-devel python36-setuptools

    easy_install-3.6 pip

    pip2 install biopython
    pip3 install pyfastaq
   
    curl -fsSL 'https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz' | tar -xz -C /usr/local/bin
    find /usr/local/bin/ncbi-blast*/bin -maxdepth 1 -executable -type f -exec ln -s {} /usr/local/bin \;

    curl -fsSL 'https://mafft.cbrc.jp/alignment/software/mafft-7.407-without-extensions-src.tgz' | tar -xz -C /tmp/
    cd /tmp/mafft-7.407-without-extensions/core && make && make install
    
    curl -fsSL 'https://downloads.sourceforge.net/project/smalt/smalt-0.7.6-static.tar.gz' | tar -xz -C /tmp/
    cd /tmp/smalt-0.7.6 && ./configure && make && make install
 
    curl -fsSL 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/samtools-1.9 && ./configure && make && make install

    curl -fsSL 'http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip' -o /usr/local/bin/Trimmomatic-0.38.zip
    cd /usr/local/bin && unzip Trimmomatic-0.38.zip
    ln -s /usr/local/bin/Trimmomatic-0.38/trimmomatic-0.38.jar /usr/local/bin
    curl -fsSL https://raw.githubusercontent.com/connor-lab/singularity-recipes/master/scripts/trimmomatic -o /usr/local/bin/trimmomatic
    chmod 775 /usr/local/bin/trimmomatic

    git clone https://github.com/lh3/seqtk.git /tmp/seqtk
    cd /tmp/seqtk
    make
    cd
    cp /tmp/seqtk/seqtk /usr/local/bin
    rm -rf /tmp/seqtk

    git clone https://github.com/ChrisHIV/shiver/ /usr/local/bin/shiver
    #cd /usr/local/bin/shiver
    #git reset --hard ce3fc9fc05d2f4cef9e5e8ae6ec3f91e490b5165
    
    #curl -fsSL 'https://github.com/ChrisHIV/shiver/archive/v1.3.5.tar.gz' | tar -xz -C /usr/local/bin && mv /usr/local/bin/shiver-1.3.5 /usr/local/bin/shiver
    
   # find /usr/local/bin/shiver -maxdepth 1 -executable -type f -exec cp {} /usr/local/bin \;

   # sed -e '/^ThisDir/ s/^#*/#/' -i /usr/local/bin/shiver_*.sh
   # sed -i '/^ToolsDir/i ThisDir="/usr/local/bin/shiver"' /usr/local/bin/shiver_*.sh

    rm -rf /tmp/seqtk /tmp/samtools* /tmp/smalt* /tmp/mafft*

%environment
    LC_ALL=C
    export LC_ALL
    PATH=$PATH:/usr/local/bin/shiver
    export PATH

%runscript
    exec shiver_init.sh "$@"

%labels
    Maintainer m-bull
    Version shiver-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

