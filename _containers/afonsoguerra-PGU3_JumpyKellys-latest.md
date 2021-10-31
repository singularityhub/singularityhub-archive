---
id: 11646
name: "afonsoguerra/PGU3_JumpyKellys"
branch: "master"
tag: "latest"
commit: "20a884863d46359a1e1f35fb4f50cc75169c044a"
version: "a30c28914455176b7c1632a77b1474c2"
build_date: "2020-04-22T17:52:36.577Z"
size_mb: 2074.0
size: 1033101343
sif: "https://datasets.datalad.org/shub/afonsoguerra/PGU3_JumpyKellys/latest/2020-04-22-20a88486-a30c2891/a30c28914455176b7c1632a77b1474c2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/afonsoguerra/PGU3_JumpyKellys/latest/2020-04-22-20a88486-a30c2891/
recipe: https://datasets.datalad.org/shub/afonsoguerra/PGU3_JumpyKellys/latest/2020-04-22-20a88486-a30c2891/Singularity
collection: afonsoguerra/PGU3_JumpyKellys
---

# afonsoguerra/PGU3_JumpyKellys:latest

```bash
$ singularity pull shub://afonsoguerra/PGU3_JumpyKellys:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
echo "Starting the Jumpy Genes Research container [19-316]..."
echo ""
echo "Available entrypoints for run are --app jumpy and --app testjumpy"


%post

# Install latest version of R (https://linuxize.com/post/how-to-install-r-on-ubuntu-18-04/)
#  (do it this way otherwise by default will install 3.2)

apt-get -y update

apt-get install -y apt-transport-https software-properties-common apt-utils wget curl
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'

apt-get -y update
#apt-get -y upgrade

# Installing extra software
apt-get -y install libssl-dev libcurl4-openssl-dev git git-lfs automake autoconf libxml2 libxml2-dev libcurl4-openssl-dev libfontconfig1-dev libcairo2-dev

apt-get -y install r-base-core

apt-get -y install tk-dev mesa-common-dev libglu1-mesa-dev #Satisfying dependencies for rgl that seems to be required below for RColorBrewer

apt-get -y install python3-pip python-pip

## Install required R packages

R --slave -e 'install.packages(c("devtools","BiocManager"), dependencies=TRUE, repos = "http://cran.us.r-project.org")'
#R --slave -e 'install.packages("BiocManager", dependencies=TRUE, repos = "http://cran.us.r-project.org")'
#R --slave -e 'BiocManager::install("DESeq2", version = "3.8")'
R --slave -e 'BiocManager::install("DESeq2")'
#R --slave -e 'BiocManager::install("tidyverse")' # this is actually cran it seems

R --slave -e 'devtools::install_github("tidyverse/tidyverse")'

R --slave -e 'install.packages(c("scales", "WriteXLS"), dependencies=TRUE, repos = "http://cran.us.r-project.org")'


# Installing some python stuff
pip3 install snakemake docopt pandas

cd /usr/bin

git clone https://github.com/hyunhwaj/SalmonTE






git clone https://github.com/mhammell-laboratory/TEtranscripts

cd TEtranscripts/

#This was giving 'forbidden' error... commenting out three lines below to avoid that. Sort it out later. 

###Will likely need to get the reference databases, more dependencies and all. But maybe play with the other one first. 
#wget 'http://labshare.cshl.edu/shares/mhammelllab/www-data/TEtranscripts/TE_GTF/hg38_rmsk_TE.gtf.gz'
#wget 'http://labshare.cshl.edu/shares/mhammelllab/www-data/TEtranscripts/TE_GTF/makeTEgtf.pl.gz'
#gzip -d makeTEgtf.pl.gz hg38_rmsk_TE.gtf.gz



#wget -r --mirror http://labshare.cshl.edu/shares/mhammelllab/www-data/TEtranscripts/test_data/

cd /


%environment
export LC_ALL=C
export PATH=$PATH:$PWD
export PATH="$PATH:/usr/bin/SalmonTE"
export PATH="$PATH:/usr/bin/TEtranscripts"
export R_LIBS_SITE=${R_LIBS_SITE}':/usr/local/lib/R/site-library:/usr/lib/R/site-library:/usr/lib/R/library'


%apprun jumpy
    SalmonTE.py "$@"

%apprun testjumpy
    SalmonTE.py quant --reference=hs /usr/bin/SalmonTE/example/CTRL_1_R1.fastq /usr/bin/SalmonTE/example/CTRL_2_R1.fastq         

%apprun jumpyquant
    SalmonTE.py quant --reference=hs "$@"        

%apprun jumpydge
    SalmonTE.py test --inpath=SalmonTE_output --outpath=SalmonTE_statistical_test --tabletype=csv --figtype=png --analysis_type=DE "$@"

%apprun jumpydge1
    SalmonTE.py test --inpath=SalmonTE_output --outpath=SalmonTE_statistical_test --tabletype=csv --figtype=png --analysis_type=DE --conditions=control,treatment
```

## Collection

 - Name: [afonsoguerra/PGU3_JumpyKellys](https://github.com/afonsoguerra/PGU3_JumpyKellys)
 - License: None

