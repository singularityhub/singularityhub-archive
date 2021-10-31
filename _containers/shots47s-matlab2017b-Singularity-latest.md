---
id: 1218
name: "shots47s/matlab2017b-Singularity"
branch: "master"
tag: "latest"
commit: "15b0148d32f378ae9ca0f445aa5ac8e0c1dfe93a"
version: "28fb4455cf881129020c6338ed24d20f"
build_date: "2018-01-08T17:06:55.190Z"
size_mb: 3762
size: 1489911839
sif: "https://datasets.datalad.org/shub/shots47s/matlab2017b-Singularity/latest/2018-01-08-15b0148d-28fb4455/28fb4455cf881129020c6338ed24d20f.simg"
url: https://datasets.datalad.org/shub/shots47s/matlab2017b-Singularity/latest/2018-01-08-15b0148d-28fb4455/
recipe: https://datasets.datalad.org/shub/shots47s/matlab2017b-Singularity/latest/2018-01-08-15b0148d-28fb4455/Singularity
collection: shots47s/matlab2017b-Singularity
---

# shots47s/matlab2017b-Singularity:latest

```bash
$ singularity pull shub://shots47s/matlab2017b-Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%labels
Maintainer ShawnTBrown
Version v0.9

%post
   echo "Installing Matlab Runtime 2017b"
   yum update -y
   yum install wget unzip libXext libXt-devel libXmu mesa-libGL -y
   mkdir mcr-install
   wget -P mcr-install -nv http://ssd.mathworks.com/supportfiles/downloads/R2017b/deployment_files/R2017b/installers/glnxa64/MCR_R2017b_glnxa64_installer.zip
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
```

## Collection

 - Name: [shots47s/matlab2017b-Singularity](https://github.com/shots47s/matlab2017b-Singularity)
 - License: None

