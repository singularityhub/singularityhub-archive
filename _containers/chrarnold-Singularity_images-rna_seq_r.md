---
id: 5737
name: "chrarnold/Singularity_images"
branch: "master"
tag: "rna_seq_r"
commit: "d9183c9ae296b4111481f33fd776bacfe798cd0d"
version: "cad9eb8abcf063525e4256c1c7d0e8e4"
build_date: "2019-11-14T17:15:23.997Z"
size_mb: 1934
size: 680722463
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/rna_seq_r/2019-11-14-d9183c9a-cad9eb8a/cad9eb8abcf063525e4256c1c7d0e8e4.simg"
url: https://datasets.datalad.org/shub/chrarnold/Singularity_images/rna_seq_r/2019-11-14-d9183c9a-cad9eb8a/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/rna_seq_r/2019-11-14-d9183c9a-cad9eb8a/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:rna_seq_r

```bash
$ singularity pull shub://chrarnold/Singularity_images:rna_seq_r
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: bioconductor/release_core2

%labels
  Version v1.0

%help
  Singularity image for the RNA-Seq pipeline (R 3.5.1 + all packages)



%post

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('GenomicRanges')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('rtracklayer')"

  R --slave -e "install.packages('checkmate')"
  R --slave -e "install.packages('futile.logger')"
  R --slave -e "install.packages('tidyverse')"
  R --slave -e "install.packages('reshape2')"
  R --slave -e "install.packages('RColorBrewer')"
  R --slave -e "install.packages('grDevices')"
  R --slave -e "install.packages('matrixStats')"
  R --slave -e "install.packages('rlist')"
  R --slave -e "install.packages('gridExtra')"
  R --slave -e "install.packages('stringr')"
  R --slave -e "install.packages('scales')"
  R --slave -e "install.packages('stats')"

%environment

%test
  R --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

