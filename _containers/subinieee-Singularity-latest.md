---
id: 11595
name: "subinieee/Singularity"
branch: "master"
tag: "latest"
commit: "71c3bdaf8c0470132aac81d70c08258ad2ed31f7"
version: "bbff5d8d9341eb9c16e6be88c2258e06"
build_date: "2019-11-14T13:45:13.667Z"
size_mb: 1929.0
size: 542871583
sif: "https://datasets.datalad.org/shub/subinieee/Singularity/latest/2019-11-14-71c3bdaf-bbff5d8d/bbff5d8d9341eb9c16e6be88c2258e06.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/subinieee/Singularity/latest/2019-11-14-71c3bdaf-bbff5d8d/
recipe: https://datasets.datalad.org/shub/subinieee/Singularity/latest/2019-11-14-71c3bdaf-bbff5d8d/Singularity
collection: subinieee/Singularity
---

# subinieee/Singularity:latest

```bash
$ singularity pull shub://subinieee/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:sachet/polysolver:v4

%post

     mkdir /data/
     mv /home/polysolver /usr/local/libexec/polysolver
     mv /home/samtools /usr/local/libexec/samtools
     export PSHOME=/usr/local/libexec/polysolver
     export SAMTOOLS_DIR=/usr/local/libexec/samtools
     export JAVA_DIR=/usr/bin
     export NOVOALIGN_DIR=$PSHOME/binaries
```

## Collection

 - Name: [subinieee/Singularity](https://github.com/subinieee/Singularity)
 - License: None

