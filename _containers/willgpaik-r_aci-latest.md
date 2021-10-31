---
id: 11343
name: "willgpaik/r_aci"
branch: "master"
tag: "latest"
commit: "c29c49b91e0fc0ed08909e123d121cd259b21c7b"
version: "90af47edac505c976e4c059b9abd2babbc1a83ac80b8f530ffc0d16184137bc5"
build_date: "2020-09-29T23:16:36.601Z"
size_mb: 3237.0
size: 999698432
sif: "https://datasets.datalad.org/shub/willgpaik/r_aci/latest/2020-09-29-c29c49b9-90af47ed/90af47edac505c976e4c059b9abd2babbc1a83ac80b8f530ffc0d16184137bc5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/r_aci/latest/2020-09-29-c29c49b9-90af47ed/
recipe: https://datasets.datalad.org/shub/willgpaik/r_aci/latest/2020-09-29-c29c49b9-90af47ed/Singularity
collection: willgpaik/r_aci
---

# willgpaik/r_aci:latest

```bash
$ singularity pull shub://willgpaik/r_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/centos7_aci

%setup

%files

%environment
  source /opt/rh/devtoolset-8/enable
  export PATH=$PATH:/opt/sw/r/bin

%runscript

%post
  yum -y install zlib-devel bzip2-devel xz-devel pcre-devel curl-devel readline-devel
  yum -y update
  
  source /opt/rh/devtoolset-8/enable
  mkdir -p /opt/sw/r
  cd /tmp
  wget http://lib.stat.cmu.edu/R/CRAN/src/base/R-4/R-4.0.2.tar.gz
  tar -xf R-4.0.2.tar.gz
  cd R-4.0.2
  ./configure --prefix=/opt/sw/r
  make && make install
  
  cd /tmp
  rm -rf R-4.0.2*
```

## Collection

 - Name: [willgpaik/r_aci](https://github.com/willgpaik/r_aci)
 - License: None

