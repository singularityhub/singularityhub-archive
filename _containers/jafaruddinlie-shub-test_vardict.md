---
id: 13270
name: "jafaruddinlie/shub"
branch: "master"
tag: "test_vardict"
commit: "b597695e88b3d24fac8263983592933277c20900"
version: "1e742d89f624619a04891f24494c0360e0580cc1729b3740a22044b092c60b02"
build_date: "2020-08-29T01:52:13.856Z"
size_mb: 10107.0
size: 3919822848
sif: "https://datasets.datalad.org/shub/jafaruddinlie/shub/test_vardict/2020-08-29-b597695e-1e742d89/1e742d89f624619a04891f24494c0360e0580cc1729b3740a22044b092c60b02.sif"
url: https://datasets.datalad.org/shub/jafaruddinlie/shub/test_vardict/2020-08-29-b597695e-1e742d89/
recipe: https://datasets.datalad.org/shub/jafaruddinlie/shub/test_vardict/2020-08-29-b597695e-1e742d89/Singularity
collection: jafaruddinlie/shub
---

# jafaruddinlie/shub:test_vardict

```bash
$ singularity pull shub://jafaruddinlie/shub:test_vardict
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

