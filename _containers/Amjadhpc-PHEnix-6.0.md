---
id: 5195
name: "Amjadhpc/PHEnix"
branch: "master"
tag: "6.0"
commit: "f5f6d05917f547d87127b5fbb7a2daa111ccaa0e"
version: "5a9d0d6634fff2e2757e58b61b01f8dc"
build_date: "2018-10-16T23:20:50.042Z"
size_mb: 1490
size: 522801183
sif: "https://datasets.datalad.org/shub/Amjadhpc/PHEnix/6.0/2018-10-16-f5f6d059-5a9d0d66/5a9d0d6634fff2e2757e58b61b01f8dc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Amjadhpc/PHEnix/6.0/2018-10-16-f5f6d059-5a9d0d66/
recipe: https://datasets.datalad.org/shub/Amjadhpc/PHEnix/6.0/2018-10-16-f5f6d059-5a9d0d66/Singularity
collection: Amjadhpc/PHEnix
---

# Amjadhpc/PHEnix:6.0

```bash
$ singularity pull shub://Amjadhpc/PHEnix:6.0
```

## Singularity Recipe

```singularity
BootStrap: yum

OSVersion : 7

MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include : yum tar

%help
This is singularity 2.6.0  image for Phenix pipeline build for centos 7 system. Checking again

%runscript

    #exec echo "The runscript is the containers default runtime command!"
     phenix.py --help


%setup 

 

%files
    
    jdk-7u15-linux-x64.tar.gz   # phenix does not work with jdk 8 hence we have to use old version of 7u
    GenomeAnalysisTK.jar        # Again GATK we downloaded old version to work with phenix
    picard.jar                  #  picard .jar as pre requisite      
%environment

  #  VARIABLE=MEATBALLVALUE
    PATH=/usr/local/bin:/usr/jdk1.7.0_15/bin:$PATH
    export PATH
    LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH
    
     GATK_JAR=/GenomeAnalysisTK.jar 
     export GATK_JAR
     JAVA_HOME=/usr/1.7.0_15
     export JAVA_HOME
      JRE_HOME=/usr//1.7.0_15/jre/
     export JRE_HOME
    #export  CLASSPATH=$(SINGULARITY_ROOTFS)/usr/local/bin/GenomeAnalysisTK.jar
     PICARD_JAR=/picard.jar
     export PICARD_JAR
        

%labels
   AUTHOR  Amjad Syed
   
   Email  amjadcsu@gmail.com


%post
    yum -y install tar gzip autoconf  gcc  make python python-libs python-setuptools python-devel unzip libyaml-devel wget ncurses-devel zlib-devel bzip2-devel xz-devel gcc-c++ tbb tbb-devel hostname chkconfig 
    mkdir -p /opt/sourcecode      
     echo $SINGULARITY_ROOTFS    
     echo $PWD
     ls -l
     cd /
     cp   GenomeAnalysisTK.jar /usr/local/bin
     cp   picard.jar          /usr/local/bin


     cd /root
   wget      https://files.pythonhosted.org/packages/e5/8f/3fc66461992dc9e9fcf5e005687d5f676729172dda640df2fd8b597a6da7/pip-9.0.2.tar.gz
     tar -zxvf pip-9.0.2.tar.gz
     cd pip-9.0.2
     python setup.py build
     python setup.py install
     cd /root
     pip install argparse #--proxy="http://sayedma2:no4%24security@10.0.9.20:8080"
     pip install numpy
     pip install PyVCF
     pip install biopython==1.65
    cd /root
    pip install bintrees==2.0.2
    pip install coverage==4.0.3
    pip install nose==1.3.7
    pip install Sphinx==1.3.5
    pip install sphinx-argparse==0.1.15
    pip install numpydoc==0.6.0
    

  wget https://github.com/samtools/htslib/archive/1.7.tar.gz
  tar -zxvf 1.7.tar.gz
  cd htslib-1.7
  autoheader
  autoconf
  ./configure
  make
  make install
  cd /root
  
  wget https://github.com/samtools/samtools/archive/1.7.tar.gz
  
   tar -zxvf 1.7.tar.gz.1
   cd samtools-1.7
   autoheader
   autoconf -Wno-syntax
   ./configure
   make 
   make install
   cd /root
   rm -rf /root/1.7.tar.*
   wget https://github.com/BenLangmead/bowtie2/archive/v2.3.4.1.tar.gz 

   tar -zxvf v2.3.4.1.tar.gz
   cd bowtie2-2.3.4.1
   make 
   cd /root
   rm -rf /root/bowtie2-2.3.4.1
   wget https://github.com/lh3/bwa/archive/v0.7.17.tar.gz  
   tar -zxvf v0.7.17.tar.gz
   cd bwa-0.7.17
   make
   cp bwa /usr/local/bin
   cp qualfa2fq.pl /usr/local/bin
   cp xa2multi.pl  /usr/local/bin     
   cd /root
   rm -rf /root/bwa-0.7.17
   pip2 install PHenix
cd /
tar -zxvf jdk-7u15-linux-x64.tar.gz
cp -r  jdk1.7.*/ /usr

alternatives --install /usr/bin/java java /usr/1.7.0_15/bin/java 2
 
  
   export CLASSPATH=/usr/local/bin/GenomeAnalysisTK.jar:$CLASSPATH   
    echo 'export GATK_JAR=/usr/local/bin/GenomeAnalysisTK.jar' >>$SINGULARITY_ENVIRONMENT  
    echo 'export PICARD_JAR=/usr/local/bin/Picard.jar' >>$SINGULARITY_ENVIRONMENT
    echo 'export JAVA_HOME=/usr/jdk1.7.0_15' >>$SINGULARITY_ENVIRONMENT
    echo  'export JRE_HOME=/usr/jdk1.7.0_15/jre' >>$SINGULARITY_ENVIRONMENT
    export PATH=/usr/jdk1.7.0_15/bin:$PATH
```

## Collection

 - Name: [Amjadhpc/PHEnix](https://github.com/Amjadhpc/PHEnix)
 - License: None

