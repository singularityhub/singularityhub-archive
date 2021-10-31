---
id: 8778
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "limma-voom"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "98b2d97f318e15c4cb98a2e84a3787f2"
build_date: "2019-05-08T15:11:14.332Z"
size_mb: 2600
size: 993087519
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/limma-voom/2019-05-08-5f15386e-98b2d97f/98b2d97f318e15c4cb98a2e84a3787f2.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/limma-voom/2019-05-08-5f15386e-98b2d97f/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/limma-voom/2019-05-08-5f15386e-98b2d97f/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:limma-voom

```bash
$ singularity pull shub://jlboat/BioinfoContainers:limma-voom
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.1

%post
    R -e "install.packages('BiocManager', repos='http://cran.us.r-project.org');"
    R -e "BiocManager::install(c('limma','edgeR','Glimma','tximport','ComplexHeatmap','alpine','alpineData','GenomicAlignments','rtracklayer','ensembldb','GenomicRanges'))"
    R -e "install.packages(c('ggplot2','readr','tidyr','RColorBrewer','DT','knitr','rmarkdown'), repos='https://cloud.r-project.org/')"

%runscript
    exec Rscript "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

