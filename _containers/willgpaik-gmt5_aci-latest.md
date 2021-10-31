---
id: 8789
name: "willgpaik/gmt5_aci"
branch: "master"
tag: "latest"
commit: "695883b06d3f686d02e2517cc036cfd02d94abbd"
version: "9bd9adecf2a7204fb61da56e16e70fbb"
build_date: "2019-07-19T15:27:39.042Z"
size_mb: 3899.0
size: 1681870879
sif: "https://datasets.datalad.org/shub/willgpaik/gmt5_aci/latest/2019-07-19-695883b0-9bd9adec/9bd9adecf2a7204fb61da56e16e70fbb.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/gmt5_aci/latest/2019-07-19-695883b0-9bd9adec/
recipe: https://datasets.datalad.org/shub/willgpaik/gmt5_aci/latest/2019-07-19-695883b0-9bd9adec/Singularity
collection: willgpaik/gmt5_aci
---

# willgpaik/gmt5_aci:latest

```bash
$ singularity pull shub://willgpaik/gmt5_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://willgpaik/centos7_aci:latest

%setup

%files

%environment

%runscript

%post
  yum -y install cmake \
    subversion \
    libcurl-devel \
    netcdf-devel \
    gdal-devel \
    pcre-devel \
    fftw3-devel \
    lapack-devel \
    openblas-devel

  mkdir -p /opt/sw/
  cd /opt/sw
  git clone https://github.com/GenericMappingTools/gmt.git
  wget -nc ftp://ftp.star.nesdis.noaa.gov/pub/sod/lsa/gmt/gshhg-gmt-2.3.7.tar.gz
  wget -nc ftp://ftp.star.nesdis.noaa.gov/pub/sod/lsa/gmt/dcw-gmt-1.1.4.tar.gz
  tar -xf gshhg-gmt-2.3.7.tar.gz
  tar -xf dcw-gmt-1.1.4.tar.gz
  
  cd gmt
  mkdir build
  cd build
  cmake .. -DGSHHG_ROOT=../../gshhg-gmt-2.3.7 \
    -DDCW_ROOT=../../dcw-gmt-1.1.4
    
  make && make install
  
  cd /opt/sw
  rm *.tar.gz
```

## Collection

 - Name: [willgpaik/gmt5_aci](https://github.com/willgpaik/gmt5_aci)
 - License: None

