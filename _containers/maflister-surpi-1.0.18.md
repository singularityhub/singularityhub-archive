---
id: 2383
name: "maflister/surpi"
branch: "master"
tag: "1.0.18"
commit: "9cb8e657d1c40339ae5b1a1c418ebcbeafca9e21"
version: "b350c93379dce4a6d67d299a368b8a18"
build_date: "2018-04-03T19:57:11.411Z"
size_mb: 3033
size: 786472991
sif: "https://datasets.datalad.org/shub/maflister/surpi/1.0.18/2018-04-03-9cb8e657-b350c933/b350c93379dce4a6d67d299a368b8a18.simg"
url: https://datasets.datalad.org/shub/maflister/surpi/1.0.18/2018-04-03-9cb8e657-b350c933/
recipe: https://datasets.datalad.org/shub/maflister/surpi/1.0.18/2018-04-03-9cb8e657-b350c933/Singularity
collection: maflister/surpi
---

# maflister/surpi:1.0.18

```bash
$ singularity pull shub://maflister/surpi:1.0.18
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:12.04

%labels
Maintainer Matthew Flister
Version v1.0

%help
This container runs SURPI.

%environment
    export PATH=$PATH:/usr/local/bin/surpi

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    export DEBIAN_FRONTEND=noninteractive
    apt-get update && apt-get install -y --no-install-recommends \
        curl \
        wget \
        vim \
        build-essential \
        gcc-multilib \
        git \
        make \
        python \
        python-dev \
        gcc \
        unzip \
        g++ \
        g++-4.6 \
        cpanminus \
        ghostscript \
        blast2 
    apt-get clean

    #Change below folders as desired in order to change installation location.
    install_folder="/usr/local"
    bin_folder="$install_folder/bin"
   
    if [ ! -d $bin_folder ]
    then
        mkdir $bin_folder
    fi
   
    CWD=$(pwd)
   
    #
    ##
    ### install Perl Modules
    ##
    #
   
    # for taxonomy
    cpanm DBI
    cpanm DBD::SQLite
   
    #
    ##
    ### install SURPI scripts
    ##
    #
   
    #Install via git clone
    # cd $bin_folder
    # git clone https://github.com/chiulab/surpi.git
    # cd $CWD
   
    #Install specific version
    version="surpi-1.0.18"
    wget "https://github.com/chiulab/surpi/releases/download/v1.0.18/$version.tar.gz"
    tar xvfz $version.tar.gz
    mv $version "$bin_folder/"
    ln -s "$bin_folder/$version" "$bin_folder/surpi"
   
    echo "PATH=\$PATH:$bin_folder" >> ~/.bashrc
    echo "PATH=\$PATH:$bin_folder/surpi" >> ~/.bashrc
   
    #
    ##
    ### install gt (genometools)
    ##
    #
    #Works in Ubuntu 14.10
    curl -O "http://genometools.org/pub/genometools-1.5.4.tar.gz"
    tar xvfz genometools-1.5.4.tar.gz
    cd genometools-1.5.4
    make 64bit=yes curses=no cairo=no
    make "prefix=$install_folder" 64bit=yes curses=no cairo=no install
    cd "$CWD"
   
    #
    ##
    ### install seqtk
    ##
    #
    # 6/4/14 - discovered that current version of seqtk (1.0-r57) is buggy. We should install 1.0-r31
    curl "https://codeload.github.com/lh3/seqtk/zip/1.0" > seqtk.zip
    unzip seqtk.zip
    cd seqtk-1.0
    make
    mv seqtk "$bin_folder/"
    cd $CWD
   
    #
    ##
    ### install fastq
    ##
    #
    mkdir fastq
    cd fastq
    wget "https://raw.github.com/brentp/bio-playground/master/reads-utils/fastq.cpp"
    g++ -O2 -o fastq fastq.cpp
    mv fastq "$bin_folder/"
    chmod +x "$bin_folder/fastq"
    cd $CWD
   
    #
    ##
    ### install fqextract
    ##
    #
    mkdir fqextract
    cd fqextract
    wget https://raw.github.com/attractivechaos/klib/master/khash.h
    wget http://chiulab.ucsf.edu/SURPI/software/fqextract.c
    gcc fqextract.c -o fqextract
    mv fqextract "$bin_folder/"
    chmod +x "$bin_folder/fqextract"
    cd $CWD
   
    #
    ##
    ### install cutadapt
    ##
    #
    #curl -O "https://cutadapt.googlecode.com/files/cutadapt-1.2.1.tar.gz"
    wget https://pypi.python.org/packages/44/16/cf42365624044fd4c2491015fb7292e8cf67a8832d77be103d55103ebf6d/cutadapt-1.2.1.tar.gz
    tar xvfz cutadapt-1.2.1.tar.gz
    cd cutadapt-1.2.1
    python setup.py build
    python setup.py install
    cd $CWD
    
    #
    ##
    ### install prinseq-lite.pl
    ##
    #
    
    curl -O "http://iweb.dl.sourceforge.net/project/prinseq/standalone/prinseq-lite-0.20.3.tar.gz"
    tar xvfz prinseq-lite-0.20.3.tar.gz
    cp prinseq-lite-0.20.3/prinseq-lite.pl "$bin_folder/"
    chmod +x "$bin_folder/prinseq-lite.pl"
    
    #
    ##
    ### compile and install dropcache (must be after SURPI scripts)
    ##
    #
    
    gcc $bin_folder/surpi/source/dropcache.c -o dropcache
    mv dropcache "$bin_folder/"
    chown root "$bin_folder/dropcache"
    chmod u+s "$bin_folder/dropcache"
    
    #
    ##
    ### install SNAP
    ##
    #
    
    curl -O "http://snap.cs.berkeley.edu/downloads/snap-0.15.4-linux.tar.gz"
    tar xvfz snap-0.15.4-linux.tar.gz
    cp snap-0.15.4-linux/snap "$bin_folder/"
    
    #
    ##
    ### install RAPSearch
    ##
    #
    
    git clone https://github.com/zhaoyanswill/RAPSearch2.git
    cd RAPSearch2
    ./install
    cp bin/* "$bin_folder/"
    cd $CWD
   
    #
    ##
    ### install fastQValidator from sourcecode
    ##
    #
    # http://genome.sph.umich.edu/wiki/FastQValidator
   
    curl -O "https://genome.sph.umich.edu/w/images/2/20/FastQValidatorLibStatGen.0.1.1a.tgz"
    tar xvf FastQValidatorLibStatGen.0.1.1a.tgz
    cd fastQValidator_0.1.1a
    make all
    cp fastQValidator/bin/fastQValidator "$bin_folder/"
    cd $CWD
   
   
    #
    ##
    ### install AbySS 1.5.2
    ##
    #
    # http://www.bcgsc.ca/platform/bioinfo/software/abyss
   
    #Download ABySS
    wget "https://github.com/bcgsc/abyss/releases/download/1.5.2/abyss-1.5.2.tar.gz"
    tar xvfz abyss-1.5.2.tar.gz
   
    #Set up Boost Dependency
    cd abyss-1.5.2
    wget http://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.gz
    tar xvfz boost_1_57_0.tar.gz
    ln -s boost_1_57_0/boost boost
   
    #Install packaged dependencies
    apt-get install -y openmpi-bin sparsehash libopenmpi-dev # Ubuntu 12.04
    #apt-get install -y openmpi-bin libsparsehash-dev libopenmpi-dev # Ubuntu 14.10
   
    # Configure ABySS
    ./configure --with-mpi=/usr/lib/openmpi CPPFLAGS=-I/usr/include/google
    make AM_CXXFLAGS=-Wall
    make install
    cd $CWD
   
    #
    ##
    ### install Minimo
    ##
    #
   
    apt-get -y install mummer
    cpanm DBI
    cpanm Statistics::Descriptive
    cpanm XML::Parser
   
    curl -O "http://iweb.dl.sourceforge.net/project/amos/amos/3.1.0/amos-3.1.0.tar.gz"
    tar xvfz amos-3.1.0.tar.gz
    cd amos-3.1.0
    ./configure --prefix=$install_folder CXX='g++-4.6'
    make
    make install
    cd $CWD
   
    #
    ##
    ### install fastq-dump
    ##
    #

    wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
    tar -xvf sratoolkit.current-ubuntu64.tar.gz
    cd sratoolkit.2.9.0-ubuntu64/bin
    cp -R * /usr/local/bin
    cd $CWD
```

## Collection

 - Name: [maflister/surpi](https://github.com/maflister/surpi)
 - License: [MIT License](https://api.github.com/licenses/mit)

