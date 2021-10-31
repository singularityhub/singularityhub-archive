---
id: 14234
name: "tothuhien/synteny_pipeline_singularity"
branch: "master"
tag: "latest"
commit: "1d27981d87b67217fa8ebebdabf81fb0423cb890"
version: "9ef3ae477f93ec0f5dbe3df8c8792493"
build_date: "2021-04-06T21:26:57.771Z"
size_mb: 4622.0
size: 2413703199
sif: "https://datasets.datalad.org/shub/tothuhien/synteny_pipeline_singularity/latest/2021-04-06-1d27981d-9ef3ae47/9ef3ae477f93ec0f5dbe3df8c8792493.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tothuhien/synteny_pipeline_singularity/latest/2021-04-06-1d27981d-9ef3ae47/
recipe: https://datasets.datalad.org/shub/tothuhien/synteny_pipeline_singularity/latest/2021-04-06-1d27981d-9ef3ae47/Singularity
collection: tothuhien/synteny_pipeline_singularity
---

# tothuhien/synteny_pipeline_singularity:latest

```bash
$ singularity pull shub://tothuhien/synteny_pipeline_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

This image contains required softwares to run the pipeline https://gitlab.com/sandve-lab/salmonid_synteny
First pull the image from shub: singularity pull shub://tothuhien/synteny_pipeline_singularity
Then cd to the folder of the pipeline and use the dowload image to run the snakefile of the pipeline: singularity exec synteny_pipeline_singularity.simg snakemake -s Snakefile.py --configfile config.yaml --cores 10

%post
apt-get update
apt-get install software-properties-common -y


add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
apt-get install wget zlib1g-dev libbz2-dev liblzma-dev libpcre3-dev libcurl4-gnutls-dev gfortran g++ gcc make libcurl3-gnutls mcl bzip2 libxml2-dev libssl-dev libmariadbclient-dev libpq-dev ssh apt-utils gnupg locales slurm-client -y

echo "LC_ALL=en_US.UTF-8" >> /etc/environment
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
locale-gen en_US.UTF-8

mkdir -p /usr/share/man/man1

#Install java
apt install default-jre -y

wget https://github.com/davidemms/OrthoFinder/releases/download/2.3.14/OrthoFinder.tar.gz
tar -xzvf OrthoFinder.tar.gz
mv OrthoFinder /usr/local/bin
rm OrthoFinder.tar.gz
  
wget https://bioweb.supagro.inra.fr/macse/releases/macse_v2.03.jar
mv macse_v2.03.jar /usr/local/bin
 
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda
export PATH=$PATH:/usr/local/miniconda/bin
rm Miniconda3-latest-Linux-x86_64.sh

conda init bash
conda install -c conda-forge -y mamba
mamba create -c conda-forge -c bioconda -n snakemake -y snakemake
conda install -c biocore -n snakemake -y mafft 
conda install -c bioconda -n snakemake  -y fasttree
mv /usr/local/miniconda/envs/snakemake/bin/fasttree /usr/local/miniconda/envs/snakemake/bin/FastTree #name required by orthofinder
conda install -c bioconda -n snakemake -y treebest
conda install -c conda-forge -n snakemake -y openmpi

mv /usr/local/lib/libmpi_cxx.so /usr/local/miniconda/envs/snakemake/lib
mv /usr/local/lib/libmpi_cxx.so.1 /usr/local/miniconda/envs/snakemake/lib
mv /usr/local/miniconda/envs/snakemake/lib/libmpi.so.40 /usr/local/miniconda/envs/snakemake/lib/libmpi.so.1

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/miniconda/lib:/usr/local/miniconda/envs/snakemake/lib' >>$SINGULARITY_ENVIRONMENT
echo 'export PATH=$PATH:/usr/local/miniconda/bin:/usr/local/miniconda/envs/snakemake/bin:/usr/local/bin/OrthoFinder:/usr/local/bin/OrthoFinder/bin' >>$SINGULARITY_ENVIRONMENT
echo 'export R_LIBS_USER=/usr/local/lib/R/library' >>$SINGULARITY_ENVIRONMENT

#Install R/3.5.0
wget https://cran.r-project.org/src/base/R-3/R-3.5.0.tar.gz
tar -xf R-3.5.0.tar.gz
cd R-3.5.0
./configure --with-readline=no --with-x=no
make
make install
cd ../
rm R-3.5.0.tar.gz

#Install required R packages
R --slave -e 'install.packages("BiocManager",repos="https://cloud.r-project.org/")'
R --slave -e 'BiocManager::install(c("dplyr","tidyverse","magrittr","treeio","Biostrings","ape","yaml","seqinr"),dependencies=TRUE)'

%files 
i-adhore /usr/local/bin
libpng15.so.15.13.0 /usr/local/lib
libmpi_cxx.so /usr/local/lib
libmpi_cxx.so.1 /usr/local/lib

%runscript
exec "$@"`
```

## Collection

 - Name: [tothuhien/synteny_pipeline_singularity](https://github.com/tothuhien/synteny_pipeline_singularity)
 - License: None

