---
id: 1611
name: "StanfordCosyne/pancakes"
branch: "master"
tag: "matlab"
commit: "b1fc092e444792712dc16a9a1ccf400bf324335e"
version: "17c4176a685ec7e18c2b691c6a79ef8c"
build_date: "2018-02-13T08:25:31.506Z"
size_mb: 3596
size: 1443188767
sif: "https://datasets.datalad.org/shub/StanfordCosyne/pancakes/matlab/2018-02-13-b1fc092e-17c4176a/17c4176a685ec7e18c2b691c6a79ef8c.simg"
url: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/matlab/2018-02-13-b1fc092e-17c4176a/
recipe: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/matlab/2018-02-13-b1fc092e-17c4176a/Singularity
collection: StanfordCosyne/pancakes
---

# StanfordCosyne/pancakes:matlab

```bash
$ singularity pull shub://StanfordCosyne/pancakes:matlab
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: centos:7

%labels
    Maintainer Vanessa Sochat
    Version v0.1
    MatlabVersion R2017b

%post
   echo "Installing Matlab Runtime 2017b"
   yum update -y
   yum install wget unzip libXext libXt-devel libXmu mesa-libGL -y
   mkdir mcr-install
   wget -P mcr-install http://ssd.mathworks.com/supportfiles/downloads/R2017b/deployment_files/R2017b/installers/glnxa64/MCR_R2017b_glnxa64_installer.zip
   cd mcr-install
   unzip MCR_R2017b_glnxa64_installer.zip
   ./install -mode silent -agreeToLicense yes
   cd ..
   rm -rf mcr-install
   yum clean all

%environment
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/MATLAB/MATLAB_Runtime/v93/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/java/jre/glnxa64/jre/lib/amd64/server:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/java/jre/glnxa64/jre/lib/amd64
    XAPPLRESDIR=/usr/local/MATLAB/MATLAB_Runtime/v93/X11/app-defaults
    MCR_CACHE_VERBOSE=true
    MCR_CACHE_ROOT=/tmp
    PATH=/usr/local/MATLAB/MATLAB_Runtime/v93/bin/glnxa64:$PATH
    export LD_LIBRARY_PATH XAPPLRESDIR MCR_CACHE_VERBOSE MCR_CACHE_ROOT PATH
```

## Collection

 - Name: [StanfordCosyne/pancakes](https://github.com/StanfordCosyne/pancakes)
 - License: None

