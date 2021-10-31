---
id: 4908
name: "s-andrews/singularitytest"
branch: "master"
tag: "latest"
commit: "5fb8b8c53a65fd7f337742216d57a8f5dfdddec5"
version: "f5c2fb351488d23ce0f34a3f3cd5ba70"
build_date: "2018-09-19T22:54:40.439Z"
size_mb: 1956
size: 747114527
sif: "https://datasets.datalad.org/shub/s-andrews/singularitytest/latest/2018-09-19-5fb8b8c5-f5c2fb35/f5c2fb351488d23ce0f34a3f3cd5ba70.simg"
url: https://datasets.datalad.org/shub/s-andrews/singularitytest/latest/2018-09-19-5fb8b8c5-f5c2fb35/
recipe: https://datasets.datalad.org/shub/s-andrews/singularitytest/latest/2018-09-19-5fb8b8c5-f5c2fb35/Singularity
collection: s-andrews/singularitytest
---

# s-andrews/singularitytest:latest

```bash
$ singularity pull shub://s-andrews/singularitytest:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
  This is a test image we're building just to make sure we know how

%setup
  touch ${SINGULARITY_ROOTFS}/i_made_a_file.txt
  
%post
  yum -y install wget
  yum -y install epel-release
  yum -y update
  yum -y install R
  yum -y install xkeyboard-config
  wget https://download1.rstudio.org/rstudio-1.1.456-x86_64.rpm
  yum -y localinstall rstudio-1.1.456-x86_64.rpm
  
%runscript
```

## Collection

 - Name: [s-andrews/singularitytest](https://github.com/s-andrews/singularitytest)
 - License: None

