---
id: 8723
name: "IARCbioinfo/polysolver-singularity"
branch: "master"
tag: "v4"
commit: "6526dbf308a47cf99d5a266403668c03b176847c"
version: "8c7ef4db6c2011a18f27a558d81d5d59"
build_date: "2021-04-14T22:24:06.577Z"
size_mb: 1929
size: 542879775
sif: "https://datasets.datalad.org/shub/IARCbioinfo/polysolver-singularity/v4/2021-04-14-6526dbf3-8c7ef4db/8c7ef4db6c2011a18f27a558d81d5d59.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/IARCbioinfo/polysolver-singularity/v4/2021-04-14-6526dbf3-8c7ef4db/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/polysolver-singularity/v4/2021-04-14-6526dbf3-8c7ef4db/Singularity
collection: IARCbioinfo/polysolver-singularity
---

# IARCbioinfo/polysolver-singularity:v4

```bash
$ singularity pull shub://IARCbioinfo/polysolver-singularity:v4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sachet/polysolver:v4
%post
    mkdir /data
    sed -i 's.#!/bin/sh.#!/bin/bash.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.TMP_DIR=\$outDir.TMP_DIR=/tmp.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.TMP_DIR=/home/polysolver.TMP_DIR=/tmp.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.\$SAMTOOLS_DIR./home/polysolver/binaries.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.6:29941260-29945884.chr6:29941260-29945884.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.6:31353872-31357187.chr6:31353872-31357187.g' /home/polysolver/scripts/shell_call_hla_type
    sed -i 's.6:31268749-31272105.chr6:31268749-31272105.g' /home/polysolver/scripts/shell_call_hla_type
```

## Collection

 - Name: [IARCbioinfo/polysolver-singularity](https://github.com/IARCbioinfo/polysolver-singularity)
 - License: [BSD 2-Clause "Simplified" License](https://api.github.com/licenses/bsd-2-clause)

