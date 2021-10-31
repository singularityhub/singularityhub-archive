---
id: 10166
name: "dominik-handler/AP_singu"
branch: "master"
tag: "hic-pro"
commit: "a6c0056d8e8c4d4c71873356dd530b94bebf5f5a"
version: "65b1eb652902ccd2b1d5f0900f30bb5f"
build_date: "2019-07-03T15:00:58.377Z"
size_mb: 2559
size: 851484703
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/hic-pro/2019-07-03-a6c0056d-65b1eb65/65b1eb652902ccd2b1d5f0900f30bb5f.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/hic-pro/2019-07-03-a6c0056d-65b1eb65/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/hic-pro/2019-07-03-a6c0056d-65b1eb65/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:hic-pro

```bash
$ singularity pull shub://dominik-handler/AP_singu:hic-pro
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda2

%labels
    AUTHOR Nicolas Servant

%pre


%post
    apt-get update

    apt-get install -y wget
    apt-get install -y gzip
    apt-get install -y bzip2
    apt-get install -y curl
    apt-get install -y unzip

    ## g++
    apt-get install -y build-essential
    
    #conda update conda

    conda config --add channels r
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    
    # Let us save some space
    conda clean --packages -y

    #conda install -y python=2.7
    # external tools
    echo "Installing dependancies ... "
    conda install -y bowtie2
    conda install -y samtools

    # Python (>2.7) with *pysam (>=0.8.3)*, *bx(>=0.5.0)*, *numpy(>=1.8.2)*, and *scipy(>=0.15.1)* libraries

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

%runscript
  HiC-Pro "$@"
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

