---
id: 12460
name: "matmu/nanopore"
branch: "master"
tag: "latest"
commit: "d96dfbc9ceab9cae031e38854c4f01961e68dd98"
version: "42faae0bfd74f2380a6a84f185bbf622"
build_date: "2020-04-21T01:55:11.237Z"
size_mb: 9806.0
size: 5180944415
sif: "https://datasets.datalad.org/shub/matmu/nanopore/latest/2020-04-21-d96dfbc9-42faae0b/42faae0bfd74f2380a6a84f185bbf622.sif"
url: https://datasets.datalad.org/shub/matmu/nanopore/latest/2020-04-21-d96dfbc9-42faae0b/
recipe: https://datasets.datalad.org/shub/matmu/nanopore/latest/2020-04-21-d96dfbc9-42faae0b/Singularity
collection: matmu/nanopore
---

# matmu/nanopore:latest

```bash
$ singularity pull shub://matmu/nanopore:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: matmu/nanopore:latest

%labels
Maintainer Matthias Munz <m.munz@uni-luebeck.de>

%help
Software for analysing Nanopore sequencing data.
Available programs: 
  samtools
  minimap2
  nanopolish
  medaka
  guppy_basecaller (CPU version)
  guppy_aligner (CPU version)
  guppy_barcoder (CPU version)

A minimap2 index for reference genome Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz is available at /opt/Homo_sapiens.GRCh38.dna.primary_assembly.mmi

%environment
    export PATH=/opt/nanopolish:/opt/ont-guppy-cpu/bin:/opt/nanopolish/minimap2:${PATH}
```

## Collection

 - Name: [matmu/nanopore](https://github.com/matmu/nanopore)
 - License: None

