---
id: 5548
name: "chrarnold/Singularity_images"
branch: "master"
tag: "atac_seq_r"
commit: "e8680e0828142d6350e90c51bb10c116862eb6f4"
version: "bfb85e7e2ad594ec5e234175adaff44e"
build_date: "2021-03-16T15:52:46.662Z"
size_mb: 2092
size: 746782751
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_r/2021-03-16-e8680e08-bfb85e7e/bfb85e7e2ad594ec5e234175adaff44e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chrarnold/Singularity_images/atac_seq_r/2021-03-16-e8680e08-bfb85e7e/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_r/2021-03-16-e8680e08-bfb85e7e/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:atac_seq_r

```bash
$ singularity pull shub://chrarnold/Singularity_images:atac_seq_r
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: bioconductor/release_core2

%labels
  Version v1.0

%help
  Singularity image for the ATAC-Seq pipeline (R 3.5.1 + all packages)



%post

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('DESeq2')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('GenomicRanges')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('Rsamtools')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
          biocLite('DiffBind')"


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

