---
id: 2799
name: "CHRUdeLille/vep_containers"
branch: "master"
tag: "75"
commit: "1348d218a02857c9ee298a64291d0af2b5471bd4"
version: "b39cb6aae353860ab5418397bd22c986"
build_date: "2018-08-23T18:25:58.967Z"
size_mb: 596
size: 204726303
sif: "https://datasets.datalad.org/shub/CHRUdeLille/vep_containers/75/2018-08-23-1348d218-b39cb6aa/b39cb6aae353860ab5418397bd22c986.simg"
url: https://datasets.datalad.org/shub/CHRUdeLille/vep_containers/75/2018-08-23-1348d218-b39cb6aa/
recipe: https://datasets.datalad.org/shub/CHRUdeLille/vep_containers/75/2018-08-23-1348d218-b39cb6aa/Singularity
collection: CHRUdeLille/vep_containers
---

# CHRUdeLille/vep_containers:75

```bash
$ singularity pull shub://CHRUdeLille/vep_containers:75
```

## Singularity Recipe

```singularity
#!/bin/bash
#
# Christophe Demay <christophe.demay@chru-lille.fr>
# 2018/05/11: initial version
BootStrap: docker
From: phusion/baseimage:0.10.1
%labels
  MAINTAINER christophe.demay@chru-lille.fr
  VERSION 75

%environment
  PATH=/opt/vep/src/ensembl-tools-release-75/scripts/variant_effect_predictor/:$PATH
  LC_ALL=en_US.UTF-8
  LANGUAGE=en_US.UTF-8

%help
  __     _______ ____    _____ ____  
  \ \   / / ____|  _ \  |___  | ___| 
   \ \ / /|  _| | |_) |    / /|___ \ 
    \ V / | |___|  __/    / /  ___) |
     \_/  |_____|_|      /_/  |____/ 

     Singularity container for VEP 75 <https://github.com/Ensembl/ensembl-tools/archive/release/75.zip> application. Documentation available at http://grch37.ensembl.org/info/docs/tools/vep/index.html
     Cache folder is not included in the container. You have to bind folder containing the cache and add it with the '--cache' option.

%post
       apt-get update
       apt-get -y install \
         build-essential \
         cpanminus \
         curl \
         wget \
         unzip \
         perl \
         perl-base \
         tabix \
         locales
         
       locale-gen en_US.UTF-8
       export LANGUAGE=en_US.UTF-8
       export LANG=en_US.UTF-8
       export LC_ALL=en_US.UTF-8
       locale-gen en_US.UTF-8
       dpkg-reconfigure locales
       # 
       # cpanm DBI DBD::mysql
       # 
       mkdir -p /opt/vep/src
       
       
       
       cpanm Archive::Extract Archive::Zip CGI Bio::PrimarySeqI DBI
       #LWP::Simple Bio::Perl LWP::Protocol::https
       
       cd /opt/vep/src
       wget https://github.com/Ensembl/ensembl-tools/archive/release/75.zip
       unzip 75.zip
       
       cd /opt/vep/src/ensembl-tools-release-75/scripts/variant_effect_predictor/
       ln -s variant_effect_predictor.pl vep
       chmod u+x *.pl
       ./INSTALL.pl -a a -b 'https://github.com/bioperl/bioperl-live/archive/bioperl-release-1-6-1.tar.gz'
       
       rm /opt/vep/src/75.zip
```

## Collection

 - Name: [CHRUdeLille/vep_containers](https://github.com/CHRUdeLille/vep_containers)
 - License: None

