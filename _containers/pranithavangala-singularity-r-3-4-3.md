---
id: 2405
name: "pranithavangala/singularity"
branch: "master"
tag: "r-3-4-3"
commit: "3ee83027aea3156b06cc94430fd665228a04954e"
version: "3f17a3b5df0cc9a02c8fc59adfa339e1"
build_date: "2020-12-30T14:38:31.932Z"
size_mb: 3910
size: 1459433503
sif: "https://datasets.datalad.org/shub/pranithavangala/singularity/r-3-4-3/2020-12-30-3ee83027-3f17a3b5/3f17a3b5df0cc9a02c8fc59adfa339e1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pranithavangala/singularity/r-3-4-3/2020-12-30-3ee83027-3f17a3b5/
recipe: https://datasets.datalad.org/shub/pranithavangala/singularity/r-3-4-3/2020-12-30-3ee83027-3f17a3b5/Singularity
collection: pranithavangala/singularity
---

# pranithavangala/singularity:r-3-4-3

```bash
$ singularity pull shub://pranithavangala/singularity:r-3-4-3
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://pranithavangala/singularity:0_part1

%labels

    AUTHOR Pranitha Vangala <pranitha.vangala@gmail.com>
    Version v1.0

# 2. This is how to copy files for >= 2.3, each line is a pair of <source> < destination>
#%files
#    avocados.txt # added to the root of the image
#    avocados.txt /opt # added to the directory opt

%environment
    export SRC=/usr/local/src
    export BIN=/usr/local/bin
    export R_VERSION=R-3.4.1

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"    

%post
######
## vim
#####

apt-get install -y vim

######
## R
#####
export SRC=/usr/local/src
export BIN=/usr/local/bin
export R_VERSION=R-3.4.1


%post
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
  wget https://cran.rstudio.com/src/base/R-3/R-3.4.3.tar.gz
  tar xvf R-3.4.3.tar.gz
  cd R-3.4.3

  apt-get update
  apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 curl 
  apt-get install -y libgmp10 libgmp-dev
  apt-get install -y gcc fort77 aptitude
  aptitude install -y g++
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  aptitude install -y gfortran
  gfortran --version
  apt install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev

  apt-get update

  ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes
  echo "Will use make with $NPROCS cores."
  make -j${NPROCS}
  make install

  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ade4\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ape\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"FD\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  R --slave "devtools::install_github('igraph/rigraph')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite()"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('dada2')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('tidyverse')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('edgeR')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('DESeq2')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('ape')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('ctc')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('gplots')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('Biobase', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('qvalue', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('goseq', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('Glimma', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('ROTS', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('GOplot', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('argparse', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('sm', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('zinbwave', dep = TRUE)"

######
## Python 2.7.5
#####

apt-get install -y cpp gcc g++
apt install python2.7 python-pip

#wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz 
#tar xvf Python-2.7.5.tgz
#cd Python-2.7.5
#./configure
#make
export HTSLIB_CONFIGURE_OPTIONS=--enable-plugins
pip install --upgrade pip
pip install pysam
pip install numpy scipy matplotlib ipython jupyter pandas sympy nose

##########
## Bowtie2
#########
cd $SRC
wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-linux-x86_64.zip/download -O bowtie2-2.3.3.1-linux-x86_64.zip && \
    unzip bowtie2-2.3.3.1-linux-x86_64.zip && \
    mv bowtie2-2.3.3.1-linux-x86_64/bowtie2* $BIN && \
    rm *.zip && \
    rm -r bowtie2-2.3.3.1-linux-x86_64

##########
## samtools
#########
cd $SRC
wget https://sourceforge.net/projects/samtools/files/samtools/1.7/samtools-1.7.tar.bz2/download -O samtools-1.7.tar.bz2 && tar xf samtools-1.7.tar.bz2
cd samtools-1.7*
./configure
make
cp samtools* $BIN
cd ..
rm -r samtools-1.7*

##########
## bedtools
#########
cd $SRC
apt-get install -y bedtools

##########
## Java
#########
cd $SRC

echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
add-apt-repository -y ppa:webupd8team/java && \
apt-get update && \
apt-get install -y oracle-java8-installer && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /var/cache/oracle-jdk8-installer

apt-get -y autoremove
export JAVA_HOME=/usr/lib/jvm/java-8-oracle

##########
## SPRITE
##########


##########
## NextFlow
##########

mkdir /data && cd /data
curl -s https://get.nextflow.io | bash
mv /data/nextflow /usr/bin/.
chmod 755 /usr/bin/nextflow

mkdir /project /nl /share /.nextflow /amazon
mkdir -p /mnt/efs
```

## Collection

 - Name: [pranithavangala/singularity](https://github.com/pranithavangala/singularity)
 - License: None

