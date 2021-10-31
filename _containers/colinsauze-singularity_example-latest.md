---
id: 3599
name: "colinsauze/singularity_example"
branch: "master"
tag: "latest"
commit: "28eb7d989c54c8cde3aa2f37a1e5055190d08b05"
version: "4a924675592da94ba87cdb930e682cee"
build_date: "2018-07-19T11:53:19.042Z"
size_mb: 158
size: 67805215
sif: "https://datasets.datalad.org/shub/colinsauze/singularity_example/latest/2018-07-19-28eb7d98-4a924675/4a924675592da94ba87cdb930e682cee.simg"
url: https://datasets.datalad.org/shub/colinsauze/singularity_example/latest/2018-07-19-28eb7d98-4a924675/
recipe: https://datasets.datalad.org/shub/colinsauze/singularity_example/latest/2018-07-19-28eb7d98-4a924675/Singularity
collection: colinsauze/singularity_example
---

# colinsauze/singularity_example:latest

```bash
$ singularity pull shub://colinsauze/singularity_example:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:ubuntu:18.04

%help
    Example container for Cowsay

%labels
    MAINTAINER Colin Sauze

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH
    
%post  
    apt-get update
    apt-get -y install cowsay

%runscript
    cowsay $@
```

## Collection

 - Name: [colinsauze/singularity_example](https://github.com/colinsauze/singularity_example)
 - License: None

