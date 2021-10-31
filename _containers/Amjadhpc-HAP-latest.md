---
id: 5797
name: "Amjadhpc/HAP"
branch: "master"
tag: "latest"
commit: "50bbb4dda196293ee57602e9e2d15abecaa3231f"
version: "adc87e4fb074c7908f916b86a01e81ab"
build_date: "2018-12-04T16:31:44.421Z"
size_mb: 1972
size: 760578079
sif: "https://datasets.datalad.org/shub/Amjadhpc/HAP/latest/2018-12-04-50bbb4dd-adc87e4f/adc87e4fb074c7908f916b86a01e81ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Amjadhpc/HAP/latest/2018-12-04-50bbb4dd-adc87e4f/
recipe: https://datasets.datalad.org/shub/Amjadhpc/HAP/latest/2018-12-04-50bbb4dd-adc87e4f/Singularity
collection: Amjadhpc/HAP
---

# Amjadhpc/HAP:latest

```bash
$ singularity pull shub://Amjadhpc/HAP:latest
```

## Singularity Recipe

```singularity
BootStrap: yum

OSVersion : 7

MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include : yum tar git 

%help
This is singularity 2.6.0  image for hap  build for centos 7 system.

%runscript

    exec echo "The runscript is the containers default runtime command!"


%setup 

%files



    
%environment

        

%labels
   AUTHOR  Amjad Syed
   
   Email  amjadcsu@gmail.com


%post
    yum -y install rpm  tar gzip autoconf  git cmake gcc  gcc-c++  boost make python wget python-setuptools python-devel zlib-devel zlib bzip2 bzip2-devel libstdc++ libstdc++-devel libstdc++-static
    mkdir -p /opt/sourcecode      
     echo $SINGULARITY_ROOTFS    
     echo $PWD
     ls -l
     cd /
   


     cd /root
   wget      https://files.pythonhosted.org/packages/e5/8f/3fc66461992dc9e9fcf5e005687d5f676729172dda640df2fd8b597a6da7/pip-9.0.2.tar.gz
     tar -zxvf pip-9.0.2.tar.gz
     cd pip-9.0.2
     python setup.py build
     python setup.py install
     cd /root
     pip install argparse
     pip install numpy
     pip install scipy
     pip install pandas
     pip install pysam
     pip install bx-python
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64:/usr/lib     
git clone https://github.com/sequencing/hap.py
#cd hap.py
 mkdir hap.py-build
 cd hap.py-build
cmake   ../hap.py
make
make install
```

## Collection

 - Name: [Amjadhpc/HAP](https://github.com/Amjadhpc/HAP)
 - License: None

