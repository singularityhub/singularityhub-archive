---
id: 7925
name: "willgpaik/allpaths_aci"
branch: "master"
tag: "latest"
commit: "0db8345caaec30826924552b84701129f283380e"
version: "d1bb036f795278935de52afe2109a4ed"
build_date: "2020-12-12T07:21:36.824Z"
size_mb: 6641
size: 2023858207
sif: "https://datasets.datalad.org/shub/willgpaik/allpaths_aci/latest/2020-12-12-0db8345c-d1bb036f/d1bb036f795278935de52afe2109a4ed.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/allpaths_aci/latest/2020-12-12-0db8345c-d1bb036f/
recipe: https://datasets.datalad.org/shub/willgpaik/allpaths_aci/latest/2020-12-12-0db8345c-d1bb036f/Singularity
collection: willgpaik/allpaths_aci
---

# willgpaik/allpaths_aci:latest

```bash
$ singularity pull shub://willgpaik/allpaths_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://willgpaik/centos7_aci:latest

%setup

%files

%environment 
  export PATH=$PATH:/opt/sw/allpaths/bin

%runscript


%post
  yum -y update

  mkdir -p /opt/sw/allpaths
  cd /opt/sw
  wget ftp://ftp.broadinstitute.org/pub/crd/ALLPATHS/Release-LG/latest_source_code/LATEST_VERSION.tar.gz
  tar -xf LATEST_VERSION.tar.gz
  cd allpathslg-52488
  ./configure --prefix=/opt/sw/allpaths
  make
  make install
  
  cd /opt/sw
  rm -rf allpathslg-52488
  rm LATEST_VERSION.tar.gz
```

## Collection

 - Name: [willgpaik/allpaths_aci](https://github.com/willgpaik/allpaths_aci)
 - License: None

