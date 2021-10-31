---
id: 2617
name: "DoaneAS/RNAseq"
branch: "master"
tag: "latest"
commit: "a0158d2bd54979fffa68ccff2d9bd3fc5d106be3"
version: "4fbcac52fce3bce36b76d716ab4cab10"
build_date: "2020-01-30T16:09:58.657Z"
size_mb: 3609
size: 1673334815
sif: "https://datasets.datalad.org/shub/DoaneAS/RNAseq/latest/2020-01-30-a0158d2b-4fbcac52/4fbcac52fce3bce36b76d716ab4cab10.simg"
url: https://datasets.datalad.org/shub/DoaneAS/RNAseq/latest/2020-01-30-a0158d2b-4fbcac52/
recipe: https://datasets.datalad.org/shub/DoaneAS/RNAseq/latest/2020-01-30-a0158d2b-4fbcac52/Singularity
collection: DoaneAS/RNAseq
---

# DoaneAS/RNAseq:latest

```bash
$ singularity pull shub://DoaneAS/RNAseq:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: scilifelab/ngi-rnaseq:1.4

%post
    mkdir /athena
    mkdir /scratchLocal
```

## Collection

 - Name: [DoaneAS/RNAseq](https://github.com/DoaneAS/RNAseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

