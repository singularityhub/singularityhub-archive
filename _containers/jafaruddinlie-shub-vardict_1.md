---
id: 13271
name: "jafaruddinlie/shub"
branch: "master"
tag: "vardict_1"
commit: "b597695e88b3d24fac8263983592933277c20900"
version: "fe829a1567f8854b321597216c456bdae6a621bf3162ac90744a6efab4a56229"
build_date: "2020-08-29T02:16:03.673Z"
size_mb: 10107.0
size: 3919822848
sif: "https://datasets.datalad.org/shub/jafaruddinlie/shub/vardict_1/2020-08-29-b597695e-fe829a15/fe829a1567f8854b321597216c456bdae6a621bf3162ac90744a6efab4a56229.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jafaruddinlie?dir=/shub/vardict_1/2020-08-29-b597695e-fe829a15/
recipe: https://datasets.datalad.org/shub/jafaruddinlie/shub/vardict_1/2020-08-29-b597695e-fe829a15/Singularity
collection: jafaruddinlie/shub
---

# jafaruddinlie/shub:vardict_1

```bash
$ singularity pull shub://jafaruddinlie/shub:vardict_1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804-cuda10.1

%labels
 MAINTAINER_NAME  Jason Steen
 MAINTAINER_EMAIL jason.steen@monash.edu

 APPLICATION_NAME HIPLEX
 APPLICATION_VERSION 2

%environment

%post -c /bin/bash
 apt update
 apt -y install curl bedtools r-base-core default-jdk default-jre autoconf libbz2-dev liblzma-dev libssl-dev libcurl4-openssl-dev libncurses-dev zlib1g-dev
 which ls
 echo "Test"

%runscript 
 $*
```

## Collection

 - Name: [jafaruddinlie/shub](https://github.com/jafaruddinlie/shub)
 - License: None

