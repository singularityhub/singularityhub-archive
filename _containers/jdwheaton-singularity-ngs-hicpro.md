---
id: 8063
name: "jdwheaton/singularity-ngs"
branch: "master"
tag: "hicpro"
commit: "3857750b13c01c1074d5f5a389879a5d996daed0"
version: "e596ba1f2144f73477f0baeb6a05c60b"
build_date: "2019-04-02T03:27:08.789Z"
size_mb: 2097
size: 650784799
sif: "https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/hicpro/2019-04-02-3857750b-e596ba1f/e596ba1f2144f73477f0baeb6a05c60b.simg"
url: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/hicpro/2019-04-02-3857750b-e596ba1f/
recipe: https://datasets.datalad.org/shub/jdwheaton/singularity-ngs/hicpro/2019-04-02-3857750b-e596ba1f/Singularity
collection: jdwheaton/singularity-ngs
---

# jdwheaton/singularity-ngs:hicpro

```bash
$ singularity pull shub://jdwheaton/singularity-ngs:hicpro
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%labels
    AUTHOR Nicolas Servant

%post
    apt-get update
    apt-get install -y wget
    apt-get install -y gzip
    apt-get install -y bzip2
    apt-get install -y curl
    apt-get install -y unzip

    ## g++
    apt-get install -y build-essential
    
    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
       wget https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh \
       	    -O ~/anaconda.sh && \
	    bash ~/anaconda.sh -b -p /usr/local/anaconda && \
	    rm ~/anaconda.sh
    fi

    # set anaconda path
    export PATH=$PATH:/usr/local/anaconda/bin
    conda update conda

    conda config --add channels r
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    
    # Let us save some space
    conda clean --packages -y

    # external tools
    echo "Installing dependancies ... "
    conda install -y bowtie2
    conda install -y samtools

    # Python (>2.7) with *pysam (>=0.8.3)*, *bx(>=0.5.0)*, *numpy(>=1.8.2)*, and *scipy(>=0.15.1)* libraries
    conda install -y python=2.7.11
    conda install -y -c anaconda scipy 
    conda install -y -c anaconda numpy 
    conda install -y -c bcbio bx-python 
    conda install -y -c bioconda pysam 

    # Install R
    conda update readline	
    #conda install -c conda-forge readline=6.2
    conda install -c r r-base 
    conda install -c r r-ggplot2=2.2.1
    conda install -c r r-rcolorbrewer
    conda install -c r r-gridbase	

    # Install HiC-pro
    echo "Installing latest HiC-Pro release ..."
    VERSION=$(curl -s https://github.com/nservant/HiC-Pro/releases/latest | egrep -o '2.[0-9]*.[0-9]*')
    echo "v"$VERSION".zip" | wget --base=http://github.com/nservant/HiC-Pro/archive/ -i - -O hicpro_latest.zip && unzip hicpro_latest.zip
    #VERSION="devel"
    #echo $VERSION".zip" | wget --base=http://github.com/nservant/HiC-Pro/archive/ -i - -O hicpro_latest.zip && unzip hicpro_latest.zip
    
    cd $(echo HiC-Pro-$VERSION)

    # Edit the config-install.txt file to specify a SLURM cluster (this is the easiest solution short of forking the repo)
    sed -i 's/CLUSTER_SYS.*/CLUSTER_SYS = SLURM/g' config-install.txt

    make configure
    make install
    
    # Let us save some space
    conda clean --packages -y
    conda clean --all -y
    rm -rf /usr/local/anaconda/pkgs

%test
    INSTALLED_HICPRO_VERSION=$(find /usr/local/bin -name HiC-Pro | xargs dirname)
    $INSTALLED_HICPRO_VERSION/HiC-Pro -h

%environment
    export PATH=$PATH:/usr/local/anaconda/bin
    INSTALLED_VERSION=$(find /usr/local/bin -name HiC-Pro | xargs dirname)
    export PATH=$PATH:$INSTALLED_VERSION 
    export LANG=C
```

## Collection

 - Name: [jdwheaton/singularity-ngs](https://github.com/jdwheaton/singularity-ngs)
 - License: None

