---
id: 6492
name: "s-andrews/singtest3"
branch: "master"
tag: "latest"
commit: "994e0fce58a867bfb0a1dbb524d5dbcc0916fde1"
version: "cde853980bf15f3e22fefb4957c8b33d"
build_date: "2019-01-23T18:33:57.849Z"
size_mb: 106
size: 48848927
sif: "https://datasets.datalad.org/shub/s-andrews/singtest3/latest/2019-01-23-994e0fce-cde85398/cde853980bf15f3e22fefb4957c8b33d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/s-andrews/singtest3/latest/2019-01-23-994e0fce-cde85398/
recipe: https://datasets.datalad.org/shub/s-andrews/singtest3/latest/2019-01-23-994e0fce-cde85398/Singularity
collection: s-andrews/singtest3
---

# s-andrews/singtest3:latest

```bash
$ singularity pull shub://s-andrews/singtest3:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER Simon Andrews

%environment
MYVAR = 3
export MYVAR

%runscript



%post  
apt -y update
apt -y install wget
touch /this_is_a_file_I_made
```

## Collection

 - Name: [s-andrews/singtest3](https://github.com/s-andrews/singtest3)
 - License: None

