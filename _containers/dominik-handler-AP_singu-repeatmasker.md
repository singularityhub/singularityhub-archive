---
id: 13132
name: "dominik-handler/AP_singu"
branch: "master"
tag: "repeatmasker"
commit: "52a3852b6763db6116f061d084ecbeab4aae0934"
version: "eaa41017c1c811cc1b76dab52f99b59a5136426217282dbe4828957ae727b524"
build_date: "2020-05-26T11:19:38.333Z"
size_mb: 2072.60546875
size: 2173284352
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/repeatmasker/2020-05-26-52a3852b-eaa41017/eaa41017c1c811cc1b76dab52f99b59a5136426217282dbe4828957ae727b524.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/repeatmasker/2020-05-26-52a3852b-eaa41017/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/repeatmasker/2020-05-26-52a3852b-eaa41017/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:repeatmasker

```bash
$ singularity pull shub://dominik-handler/AP_singu:repeatmasker
```

## Singularity Recipe

```singularity
Bootstrap: library
From: ubuntu:18.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  repeatmasker v4.1.0  

%runscript
    "$@"

%post
  # Software versions
    export RM_VERSION=4.1.0
    export RMB_VERSION=2.10.0
    export TRF_VERSION=409
    export DFAM_VERSION=3.1
 
  #install base-dependencies
    apt-get update
    apt-get -y install software-properties-common
    add-apt-repository universe
    apt-get update    
    apt-get install -y --no-install-recommends wget tar libgomp1 unzip build-essential openssh-client locales parallel rsync

  mkdir /install-dir

  locale-gen en_US.UTF-8
    export LANG=en_US.UTF-8  
    export LANGUAGE=en_US:en  
    export LC_ALL=en_US.UTF-8  

  # Configure term
    export TERM=xterm

  # Install cpanm
    wget -O - http://cpanmin.us | perl - --self-upgrade
  
  # Install the Text::Soundex module via cpan:
    cpanm Text::Soundex

  #install rmblast
    cd /install-dir
    wget -nv http://www.repeatmasker.org/rmblast-${RMB_VERSION}+-x64-linux.tar.gz
    tar zxf /install-dir/rmblast-${RMB_VERSION}+-x64-linux.tar.gz
    cp /install-dir/rmblast-${RMB_VERSION}/bin/* /usr/local/bin/
    rm -rf /install-dir/rmblast-${RMB_VERSION}+-x64-linux.tar.gz
    rm -rf /install-dir/rmblast-${RMB_VERSION}
  
  #install trf
    cd /install-dir
    wget -nv http://tandem.bu.edu/trf/downloads/trf${TRF_VERSION}.linux64 
    mv trf${TRF_VERSION}.linux64 /usr/bin/trf
    chmod +x /usr/bin/trf

  #install hmmer
    cd /install-dir
    wget -nv http://eddylab.org/software/hmmer/hmmer-3.2.1.tar.gz
    tar zxf hmmer-3.2.1.tar.gz
    cd hmmer-3.2.1
    ./configure --prefix /usr/local/
    make
    make check
    make install
  
  # install easel
    cd easel
    make install


  #install repeatmasker
    cd /usr/local
    wget -nv http://www.repeatmasker.org/RepeatMasker-${RM_VERSION}.tar.gz
    tar xvf RepeatMasker-${RM_VERSION}.tar.gz
    rm -rf RepeatMasker-${RM_VERSION}.tar.gz
    ln -s /usr/local/RepeatMasker/RepeatMasker /usr/bin/RepeatMasker
    chmod a+x /usr/bin/RepeatMasker

    #add repbase library
    cd /usr/local/RepeatMasker/
    wget https://brenneckelab.imba.oeaw.ac.at/tmp/RepBaseRepeatMaskerEdition-20181026.tar    
    tar xvf RepBaseRepeatMaskerEdition-20181026.tar
    rm RepBaseRepeatMaskerEdition-20181026.tar

    #add Dfam library
    #cd /usr/local/RepeatMasker/Libraries
    #wget -nv --no-check-certificate https://www.dfam.org/releases/Dfam_${DFAM_VERSION}/families/Dfam.hmm.gz
    #gunzip -f Dfam.hmm.gz

    #configure RepeatMasker
    cd /usr/local/RepeatMasker
    perl ./configure -trf_prgm /usr/bin/trf -hmmer_dir /usr/local/bin/ -rmblast_dir /usr/local/bin/ -default_search_engine=hmmer -libdir=/usr/local/RepeatMasker/Libraries/

    #initiate RepeatMasker by running it quickly
    cd /install-dir/
    wget -nv --no-check-certificate https://github.com/tpall/repeatmasker-singularity/raw//master/test/seqs/small-1.fa
    RepeatMasker //small-1.fa

  #install kent-utils
    apt-get --assume-yes install mysql-client libssl-dev openssl libmysqlclient-dev  build-essential zlib1g libpng-dev cmake git-core wget zlib1g-dev uuid-dev
  
    mkdir -p /Software
    cd /Software
    #git clone git://github.com/ENCODE-DCC/kentUtils.git
    wget http://hgdownload.soe.ucsc.edu/admin/exe/userApps.src.tgz 
    tar zxvf userApps.src.tgz  

    mv userApps kentUtils
    cd kentUtils
    make
  
  #clean up
    apt-get autoremove
    apt-get clean

%environment
  export  PATH="/Software/kentUtils/bin:$PATH"
  export HOME="/Software/kentUtils/"


%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

