---
id: 11596
name: "subinieee/polysolver"
branch: "master"
tag: "latest"
commit: "430f46102184e47b6c9b4ca71bf6af3d424951cb"
version: "6de75d5c22ec54bda83876a03ca0cb24"
build_date: "2019-11-14T16:22:07.119Z"
size_mb: 1929.0
size: 542871583
sif: "https://datasets.datalad.org/shub/subinieee/polysolver/latest/2019-11-14-430f4610-6de75d5c/6de75d5c22ec54bda83876a03ca0cb24.sif"
url: https://datasets.datalad.org/shub/subinieee/polysolver/latest/2019-11-14-430f4610-6de75d5c/
recipe: https://datasets.datalad.org/shub/subinieee/polysolver/latest/2019-11-14-430f4610-6de75d5c/Singularity
collection: subinieee/polysolver
---

# subinieee/polysolver:latest

```bash
$ singularity pull shub://subinieee/polysolver:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From: sachet/polysolver:v3

%post

     mkdir /data/
     mv /home/polysolver /usr/local/libexec/polysolver
     mv /home/samtools /usr/local/libexec/samtools
     export PSHOME=/usr/local/libexec/polysolver
     export SAMTOOLS_DIR=/usr/local/libexec/samtools
     export JAVA_DIR=/usr/bin
     export NOVOALIGN_DIR=$PSHOME/binaries

     # IMPORTANT: the below aren't set, I'm not sure where they are inside image
     export GATK_DIR=$PSHOME
     export MUTECT_DIR=$PSHOME
     export STRELKA_DIR=$PSHOME
     chmod 777 -R /usr/local/libexec
```

## Collection

 - Name: [subinieee/polysolver](https://github.com/subinieee/polysolver)
 - License: [MIT License](https://api.github.com/licenses/mit)

