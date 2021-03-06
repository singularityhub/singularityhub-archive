---
id: 847
name: "glass-consortium/glasstools"
branch: "master"
tag: "beta"
commit: "402ecb7cf84072d58d5a98c340ef0c96661099a7"
version: "e3fcd575b10b6869cbf9faa5d98acdb4"
build_date: "2019-11-10T23:21:28.210Z"
size_mb: 3629
size: 1390419999
sif: "https://datasets.datalad.org/shub/glass-consortium/glasstools/beta/2019-11-10-402ecb7c-e3fcd575/e3fcd575b10b6869cbf9faa5d98acdb4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/glass-consortium/glasstools/beta/2019-11-10-402ecb7c-e3fcd575/
recipe: https://datasets.datalad.org/shub/glass-consortium/glasstools/beta/2019-11-10-402ecb7c-e3fcd575/Singularity
collection: glass-consortium/glasstools
---

# glass-consortium/glasstools:beta

```bash
$ singularity pull shub://glass-consortium/glasstools:beta
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: no

%help
  Visit https://docker.glass-consortium.org on getting started with GLASS workflows.

%setup
  umask 0022
  rm -rf ${SINGULARITY_ROOTFS}/setup
  mkdir -p ${SINGULARITY_ROOTFS}/setup
  chmod 755 ${SINGULARITY_ROOTFS}/setup
  cp -r setup ${SINGULARITY_ROOTFS}/

%labels
  Name glasstools:beta
  Version v1.1.2s2
  Maintainer Samir B. Amin, tweet: sbamin, web: https://sbamin.com
  Description Singularity image to run GLASS consortium workflows
  Website https://docker.glass-consortium.org
  Sourcecode https://github.com/glass-consortium/glasstools
  Issues https://github.com/glass-consortium/glassdocs/issues
  License https://github.com/glass-consortium/glasstools/blob/master/LICENSE
  Contact Roel Verhaak, tweet: roelverhaak, web: https://www.jax.org/verhaak-lab

%environment

  PATH=/opt/miniconda/bin:/opt/bin:/home/glass/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/prada/pyPRADA_1.2:/opt/freebayes/default/bin:/usr/lib/jvm/java/bin:/usr/lib/jvm/java/db/bin:/usr/lib/jvm/java/jre/bin"${PATH:+:$PATH}"
  JAVA_HOME=/usr/lib/jvm/java
  J2SDKDIR=/usr/lib/jvm/java
  J2REDIR=/usr/lib/jvm/java/jre
  JAVA_LD_LIBRARY_PATH=/usr/lib/jvm/java/jre/lib/amd64/server
  JDK7=/opt/java/jdk7
  JDK8=/opt/java/jdk8
  TZ=Etc/UTC
  LD_LIBRARY_PATH=/usr/lib/jvm/java/jre/lib/amd64/server"${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

  export PATH JAVA_HOME J2SDKDIR J2REDIR JAVA_LD_LIBRARY_PATH JDK7 JDK8 TZ LD_LIBRARY_PATH

%post
  echo -e "\n#####\nSet Env\n#####\n"
  chmod 755 /etc/profile
  . /etc/profile
  umask 0022

  echo -e "\n#####\nUpdate startup script by adding mypathmunge function and user defined profile.d directory\n#####\n"
  cat /setup/config/profile >>$SINGULARITY_ENVIRONMENT

  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export R_VERSION="R-3.4.2"
  export TZ=Etc/UTC
  echo $TZ >| /etc/timezone

  export DEBIAN_FRONTEND=noninteractive
  export DEBCONF_NONINTERACTIVE_SEEN=true

  echo -e "\n#####\nInstall devtools\n#####\n"
  apt-get update && apt-get install --yes --no-install-recommends apt-utils \
  build-essential python-software-properties \
  python-setuptools sudo locales ca-certificates tzdata \
  software-properties-common cmake libcurl4-openssl-dev wget curl \
  gdebi tar zip unzip rsync screen nano vim dos2unix bc \
  libxml2-dev libssl-dev dpkg-dev libx11-dev libxpm-dev libxft-dev \
  libxext-dev libpng-dev libjpeg-dev binutils libncurses-dev zlib1g-dev libbz2-dev \
  liblzma-dev ruby libarchive-zip-perl libdbd-mysql-perl libjson-perl gfortran libpcre3-dev

  echo -e "\n#####\nInstall devtools\n#####\n"
  add-apt-repository --yes ppa:git-core/ppa
  apt-get update && apt-get install --yes --no-install-recommends git

  echo -e "\n#####\nSetup locale\n#####\n"
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8

  echo -e "\n#####\nSetup Timezone\n#####\n"
  echo "TZ is $TZ"
  rm -f /etc/localtime && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
  dpkg-reconfigure -f noninteractive tzdata

  echo -e "\n#####\nSetup glassuser\n#####\n"
  groupadd -g 712119 glass && \
  useradd -m -d /home/glass -s /bin/bash -c "GLASS Default User" -u 2119518 -g glass -G staff,sudo glassuser && \
  echo "%sudo  ALL=(ALL) NOPASSWD:ALL" | (EDITOR="tee -a" visudo)

  echo -e "\n#####\nInstall Conda\n#####\n"
  mkdir -p /opt/bin && \
  wget --no-check-certificate https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O /opt/miniconda.sh && \
  bash /opt/miniconda.sh -b -p /opt/miniconda -f && \
  rm -f /opt/miniconda.sh

  echo -e "\n#####\nOverride system python with conda python\n#####\n"
  PATH=/opt/miniconda/bin:/opt/bin:/home/glass/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  export PATH

  ## bugfix: https://stackoverflow.com/a/46498173/1243763 
  conda update --yes conda && conda update --yes python

  conda config --add channels conda-forge && \
  conda config --add channels defaults && \
  conda config --add channels r && \
  conda config --add channels bioconda && \
  cp /root/.condarc /opt/miniconda/.condarc && \
  mkdir -p /etc/profile.d
  chmod 755 /etc/profile.d

  echo -e "\n#####\nCopy startup and git config\n#####\n"
  chown -R root:glass /setup
  rsync -avhP /setup/config/profile /etc/profile
  chmod 755 /etc/profile
  rsync -avhP /setup/config/.gitconfig /root/.gitconfig
  rsync -avhP /setup/config/.gitconfig_glass /home/glass/.gitconfig
  chown glassuser:glass /home/glass/.gitconfig

  echo -e "\n#####\nSetup JDK8\n#####\n"
  mkdir -p /opt/java
  cd /opt/java
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/jdk-8u151-linux-x64.tar.gz
  tar xvzf jdk-8u151-linux-x64.tar.gz
  ln -s jdk1.8.0_151 jdk8
  rm -f jdk-8u151-linux-x64.tar.gz
  cd /opt/java/jdk1.8.0_151/lib/amd64
  ln -s ../../jre/lib/amd64/server ./server
  mkdir -p /usr/lib/jvm
  cd /usr/lib/jvm
  ln -s /opt/java/jdk8 java

  echo -e "\n#####\nSetup JDK7\n#####\n"
  cd /opt/java
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/jdk1.7.0_79.tar.gz
  tar xvzf jdk1.7.0_79.tar.gz
  ln -s jdk1.7.0_79 jdk7
  rm -f jdk1.7.0_79.tar.gz

  echo -e "\n#####\nPush jar files\n#####\n"
  mkdir -p /opt/jars
  cd /opt/jars
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/picard.jar
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/GenomeAnalysisTK.jar
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/VarScan2.jar
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/mutect-1.1.7.jar
  chown -R root:glass /opt/jars
  chmod 644 /opt/jars/*.jar

  echo -e "\n#####\nSetup PRADA\n#####\n"
  mkdir -p /opt/prada
  cd /opt/prada
  wget --no-check-certificate ftp://ftp.jax.org/verhaak/deps/pyPRADA_1.2.tar.gz
  tar xvzf pyPRADA_1.2.tar.gz
  chown -R root:glass pyPRADA_1.2
  rm -f pyPRADA_1.2.tar.gz
  cd /

  echo -e "\n#####\nUpdate Env\n#####\n"
  PATH=/opt/miniconda/bin:/opt/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm/java/bin:/usr/lib/jvm/java/db/bin:/usr/lib/jvm/java/jre/bin"${PATH:+:$PATH}"

  JAVA_HOME=/usr/lib/jvm/java
  J2SDKDIR=/usr/lib/jvm/java
  J2REDIR=/usr/lib/jvm/java/jre
  JAVA_LD_LIBRARY_PATH=/usr/lib/jvm/java/jre/lib/amd64/server
  JDK7=/opt/java/jdk7
  JDK8=/opt/java/jdk8
  
  LD_LIBRARY_PATH=/usr/lib/jvm/java/jre/lib/amd64/server"${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

  export PATH JAVA_HOME J2SDKDIR J2REDIR JAVA_LD_LIBRARY_PATH JDK7 JDK8 TZ LD_LIBRARY_PATH

  echo -e "\n#####\nInstall R and other tools from conda\n#####\n"
  conda install --yes r-base htslib samtools bcftools bwa bedtools bamtools htseq pysam biopython

  echo -e "\n#####\nInstall R packages\n#####\n"
  Rscript -e 'install.packages(c("tidyverse", "git2r", "stringr", "devtools", "params", "flowr", "funr"), repos = c(CRAN="http://cran.rstudio.com"))'
  
  Rscript -e 'devtools::install_github("glass-consortium/ultraseq", subdir = "ultraseq", ref="master")'
  
  echo -e "\n#####\nInstall sequenza\n#####\n"  
  Rscript -e "source('http://bioconductor.org/biocLite.R');biocLite('copynumber', suppressUpdates=TRUE)"

  Rscript -e 'install.packages("sequenza", repos = c(CRAN="http://cran.rstudio.com"))'

  wget --no-check-certificate -O /opt/bin/sequenza-utils.py ftp://ftp.jax.org/verhaak/deps/sequenza-utils.py
  chmod 755 /opt/bin/sequenza-utils.py

  echo -e "\n#####\nSetup flowr\n#####\n"
  mkdir -p /root/bin
  Rscript -e 'library(flowr);setup()'

  echo -e "\n#####\nTest flowr\n#####\n"
  ln -s /opt/miniconda/lib/R/library/flowr/scripts/flowr /opt/bin/flowr
  chmod 755 /opt/miniconda/lib/R/library/flowr/scripts/flowr
  echo "Where is flowr command located?"
  which flowr
  flowr run x=sleep_pipe platform=local execute=TRUE
  rm -f /root/Rplots.pdf /opt/Rplots.pdf

  echo -e "\n#####\nInstall rjava package\n#####\n"
  ln -s /opt/java/jdk8/jre/lib/amd64/server/libjvm.so /opt/miniconda/lib/
  R CMD javareconf
  conda install --yes r-rjava
  cd /

  echo -e "\n#####\nInstall STAR\n#####\n"
  mkdir -p /opt/star
  cd /opt/star
  git clone https://github.com/alexdobin/STAR
  cd STAR
  git checkout 2.5.3a
  rsync -avhP /opt/star/STAR/bin/Linux_x86_64_static/ /opt/bin/
  cd /
  rm -rf /opt/star

  echo -e "\n#####\nInstall bamutil\n#####\n"
  mkdir -p /opt/bamutil
  cd /opt/bamutil
  wget --no-check-certificate https://github.com/statgen/bamUtil/archive/v1.0.14.tar.gz && \
  tar xvzf v1.0.14.tar.gz
  cd bamUtil-1.0.14
  make cloneLib
  make
  rsync -avhP /opt/bamutil/bamUtil-1.0.14/bin/bam /opt/bin
  cd /
  rm -rf /opt/bamutil

  echo -e "\n#####\nInstall freebayes\n#####\n"
  mkdir -p /opt/freebayes
  cd /opt/freebayes
  mkdir -p fb_seqlib
  mkdir -p fb_bamtools
  git clone --recursive https://github.com/ekg/freebayes.git source
  cd /opt/freebayes/source
  make
  cd /opt/freebayes
  rm -rf source/vcflib/samples
  rm -rf source/src
  rm -rf source/bamtools
  rm -rf source/.git
  rm -rf source/vcflib/googletest
  rm -rf source/vcflib/paper
  rm -rf source/SeqLib/src
  rm -rf source/SeqLib/htslib/test
  rm -rf source/vcflib/tabixpp/htslib/test
  rsync -avhP source/ fb_seqlib/
  ln -s fb_seqlib default
  rm -rf source
  cd fb_seqlib
  chmod 755 scripts/sam_add_rg.pl
  rsync -avhP scripts/ bin/
  cd /

  echo -e "\n#####\nSetup Disk Mounts\n#####\n"
  mkdir -p /mnt/scratch/refdata && \
  mkdir -p /mnt/scratch/logs && \
  mkdir -p /mnt/glasscore && \
  mkdir -p /mnt/glasscore/configs/bin && \
  mkdir -p /mnt/glasscore/configs/profile.d && \
  mkdir -p /mnt/glasscore/configs/extapps && \
  mkdir -p /mnt/glasscore/configs/extapps/Rpkgs && \
  mkdir -p /mnt/glasscore/workflows && \
  mkdir -p /mnt/glassdata/tmp && \
  mkdir -p /mnt/glassdata/flowr && \
  chown -R glassuser:glass /mnt/scratch && \
  chown -R glassuser:glass /mnt/glasscore && \
  chown -R glassuser:glass /mnt/glassdata && \
  chmod -R 775 /mnt/scratch && \
  chmod -R 775 /mnt/glasscore && \
  chmod -R 775 /mnt/glassdata

  echo -e "\n#####\nSetup bashrc\n#####\n"
  rsync -avhP /setup/config/root.bashrc /root/.bashrc && \
  rsync -avhP /setup/config/glassuser.bashrc /home/glass/.bashrc && \
  chown root:root /root/.bashrc && \
  chown glassuser:glass /home/glass/.bashrc && \
  chmod 644 /root/.bashrc && \
  chmod 644 /home/glass/.bashrc

  echo -e "\n#####\nCleanup\n#####\n"
  rm -rf /setup
  apt-get clean
  rm -rf /var/lib/apt/lists/*
  conda clean --yes --all

##############################
# R
##############################

%apprun R
  exec R "$@"

%apphelp R
  Get to R prompt, e.g.,

  singularity run --app R image_name.simg

  Visit https://docker.glass-consortium.org on getting started with GLASS workflows.

%apprun Rscript
  exec Rscript "$@"

%apphelp Rscript
  Run R scripts from shell using Rscript, e.g.,

  singularity run --app Rscript image_name.simg mycommands.R

  Visit https://docker.glass-consortium.org on getting started with GLASS workflows.

##############################
# goglass
##############################

%apprun goglass
  exec goglass "$@"

%apphelp goglass
  Run GLASS workflows from shell,e.g.,

  export GLASSMOUNTS=/mnt/scratch/lab/sandbox/singularity_glasstools/recipes/build/glass_mounts

  singularity run --app goglass \
  -B "${GLASSMOUNTS}"/disk1/glasscore:/mnt/glasscore \
  -B "${GLASSMOUNTS}"/disk1/scratch:/mnt/scratch \
  -B "${GLASSMOUNTS}"/disk2/glassdata:/mnt/glassdata \
  image_name.simg -m dna -t align -i fqs -s sample_barcode -f sample_mapping_table.tsv -d WES -n GO

  PS: For current and valid command format for GLASS workflows,
  visit https://docker.glass-consortium.org

##############################
# default command
##############################

%runscript
  exec echo "Visit https://docker.glass-consortium.org on getting started with GLASS workflows"

## END ##
```

## Collection

 - Name: [glass-consortium/glasstools](https://github.com/glass-consortium/glasstools)
 - License: None

