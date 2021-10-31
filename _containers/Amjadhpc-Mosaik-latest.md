---
id: 5478
name: "Amjadhpc/Mosaik"
branch: "master"
tag: "latest"
commit: "deaaef3c85563b1fd80aafe274742ec357c7c536"
version: "c2017304002fdfbb1dc728b56dcb8268"
build_date: "2018-11-05T14:28:49.881Z"
size_mb: 648
size: 224264223
sif: "https://datasets.datalad.org/shub/Amjadhpc/Mosaik/latest/2018-11-05-deaaef3c-c2017304/c2017304002fdfbb1dc728b56dcb8268.simg"
url: https://datasets.datalad.org/shub/Amjadhpc/Mosaik/latest/2018-11-05-deaaef3c-c2017304/
recipe: https://datasets.datalad.org/shub/Amjadhpc/Mosaik/latest/2018-11-05-deaaef3c-c2017304/Singularity
collection: Amjadhpc/Mosaik
---

# Amjadhpc/Mosaik:latest

```bash
$ singularity pull shub://Amjadhpc/Mosaik:latest
```

## Singularity Recipe

```singularity
BootStrap: yum

OSVersion : 7

MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include : yum tar

%help
This is singularity 2.6.0  image for Phenix pipeline build for centos 7 system.

%runscript

     /usr/bin/MosaikAligner --help


%setup 

 

%files
    
#    jdk-7u15-linux-x64.tar.gz   # phenix does not work with jdk 8 hence we have to use old version of 7u
 #   GenomeAnalysisTK.jar        # Again GATK we downloaded old version to work with phenix
 #   picard.jar                  #  picard .jar as pre requisite      
%environment

  #  VARIABLE=MEATBALLVALUE
 #   PATH=/usr/local/bin:/usr/jdk1.7.0_15/bin:$PATH
  #  export PATH
   # LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    #export LD_LIBRARY_PATH
    
    # GATK_JAR=/GenomeAnalysisTK.jar 
    # export GATK_JAR
    # JAVA_HOME=/usr/1.7.0_15
    # export JAVA_HOME
    #  JRE_HOME=/usr//1.7.0_15/jre/
    # export JRE_HOME
    #export  CLASSPATH=$(SINGULARITY_ROOTFS)/usr/local/bin/GenomeAnalysisTK.jar
    # PICARD_JAR=/picard.jar
    # export PICARD_JAR
        

%labels
   AUTHOR  Amjad Syed
   
   Email  amjadcsu@gmail.com


%post
    yum -y install git    autoconf  gcc make  gcc-devel  gcc-c++ gcc-c++-devel  hostname  zlib  zlib-devel libstdc++-devel libstdc++   glibc-devel  glibc-static
    mkdir -p /opt/sourcecode      
     echo $SINGULARITY_ROOTFS    
     echo $PWD
     ls -l
     cd /
     
    

     cd /root
     git clone https://github.com/wanpinglee/MOSAIK.git
     
     cd MOSAIK
     cd src
     echo "export PLATFORM_FLAGS = -D_FILE_OFFSET_BITS=64" > includes/linux.inc
     make
     pwd 
     cd /root/MOSAIK/bin
     cp MosaikAligner /usr/bin
     cp MosaikBuild  /usr/bin
     cp MosaikJump   /usr/bin
     cp MosaikText   /usr/bin

     ls /usr/bin     
    # cp /root/MOSAIK/src/bin/MosaikAligner /usr/bin
     rm -rf /root/MOSAIK
```

## Collection

 - Name: [Amjadhpc/Mosaik](https://github.com/Amjadhpc/Mosaik)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

