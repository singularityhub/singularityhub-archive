---
id: 3203
name: "UMMS-Biocore/piPipes_singularity"
branch: "master"
tag: "latest"
commit: "78b2e9d5bdf61ee891dbb261caa717673d310dd6"
version: "9d8f798867c4a2f2c89ce7ed99fdb7f0"
build_date: "2020-01-31T20:22:58.480Z"
size_mb: 7142
size: 3676844063
sif: "https://datasets.datalad.org/shub/UMMS-Biocore/piPipes_singularity/latest/2020-01-31-78b2e9d5-9d8f7988/9d8f798867c4a2f2c89ce7ed99fdb7f0.simg"
url: https://datasets.datalad.org/shub/UMMS-Biocore/piPipes_singularity/latest/2020-01-31-78b2e9d5-9d8f7988/
recipe: https://datasets.datalad.org/shub/UMMS-Biocore/piPipes_singularity/latest/2020-01-31-78b2e9d5-9d8f7988/Singularity
collection: UMMS-Biocore/piPipes_singularity
---

# UMMS-Biocore/piPipes_singularity:latest

```bash
$ singularity pull shub://UMMS-Biocore/piPipes_singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://onuryukselen/singularity

%labels

    AUTHOR Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/Software/piPipes/bin:/Software/brew/bin:/Software/sratoolkit.2.9.0-ubuntu64/bin
    export PATH

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"  
  
%post

############
### piPipes
############
    mkdir -p /Software 
    cd /Software
    chmod 777 /Software
    ## clone piPipes_singularity
    git clone https://github.com/onuryukselen/piPipes_singularity 
    ## copy forked piPipes
    git clone https://github.com/onuryukselen/piPipes.git /Software/piPipes
    cd /Software/piPipes
    ln -s $PWD/piPipes /usr/local/bin/piPipes
    ln -s $PWD/piPipes_debug /usr/local/bin/piPipes_debug
    
#################
###  Genome data
#################
    mkdir -p /Software/piPipes/common/hg19/rmsk
    cd /Software/piPipes_singularity/genome_data
    cat rmsk.txt.gz* > rmsk.txt.gz
    rsync -vazu  /Software/piPipes_singularity/genome_data/rmsk.txt.gz  /Software/piPipes/common/hg19/rmsk/.
#    wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/rmsk.txt.gz' -O rmsk.txt.gz
    ## commented out related download scripts from the piPipes/bin/piPipes_install_genomes.sh
    sed -i 's/rsync -a -P/#rsync -a -P/g' /Software/piPipes/bin/piPipes_install_genomes.sh
    mkdir -p /Software/piPipes/common/dm3
    rsync -vazu  /Software/piPipes_singularity/genome_data/chrU.fa.gz /Software/piPipes/common/dm3/. 
#    wget  ftp://hgdownload.cse.ucsc.edu/goldenPath/dm3/chromosomes/chrU.fa.gz
     
#### 1. R
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
  cd /tmp 
  wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.8_amd64.deb
  dpkg -i libicu52_52.1-3ubuntu0.8_amd64.deb
  wget https://cran.rstudio.com/src/base/R-3/R-3.4.3.tar.gz
  tar xvf R-3.4.3.tar.gz
  cd /tmp/R-3.4.3
  apt-get update
  apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 ghostscript  libicu52
  apt-get install -y libgmp10 libgmp-dev
  apt-get install -y fort77 aptitude
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  apt install -y   libpcre3-dev liblzma-dev  
  apt-get update
  apt-get install -y bioperl
  apt-get update 
  
  ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes 
  echo "Will use make with $NPROCS cores."
  make -j${NPROCS}
  make install

  pip install fastcluster
  echo install.packages\(\"fastcluster\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"stringi\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"RColorBrewer\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"grid\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggthemes\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"gplots\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"parallel\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"scales\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"reshape\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"gridExtra\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"gdata\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"labeling\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"RCircos\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"reshape2\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  yes | apt-get install libmariadb-client-lgpl-dev
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite()"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('cummeRbund')"
  
# 2. HTSeq-count
pip install HTSeq
which htseq-count

# 3. MACS2
pip install macs2
which macs2

# 4. Perl Module Statistics::Descriptive;
yes | cpan Statistics::Descriptive
perl -MStatistics::Descriptive -e "print \"Installed.\\n\";"

# 5. Install Gawk with Linuxbrew  
locale-gen "en_US.UTF-8"
dpkg-reconfigure locales
export LANGUAGE="en_US.UTF-8"
echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
cd /Software
chmod 777 /tmp
chmod +t /tmp
apt-get install -y apt-transport-https build-essential libsm6 libxrender1 libfontconfig1 ruby
useradd -m singularity
su -c 'cd /Software && git clone https://github.com/Linuxbrew/brew.git /Software/brew' singularity
su -c '/Software/brew/bin/brew install gawk' singularity
ln -s /Software/brew/bin/gawk /Software/piPipes/bin/awk
    
##6. NCBI SRA and cutadapt 
cd /Software
#curl -O https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.0/sratoolkit.2.9.0-ubuntu64.tar.gz
#tar xvf sratoolkit.2.9.0-ubuntu64.tar.gz
pip install cutadapt

##7. RSeQC
pip install RSeQC
```

## Collection

 - Name: [UMMS-Biocore/piPipes_singularity](https://github.com/UMMS-Biocore/piPipes_singularity)
 - License: None

