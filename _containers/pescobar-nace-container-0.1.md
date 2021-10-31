---
id: 5083
name: "pescobar/nace-container"
branch: "master"
tag: "0.1"
commit: "1ac60257704fa3f0524b09d4857008114a38c547"
version: "1885d03c13ef039d25baaab3e86a98b8"
build_date: "2018-10-03T09:11:43.240Z"
size_mb: 3582
size: 1881423903
sif: "https://datasets.datalad.org/shub/pescobar/nace-container/0.1/2018-10-03-1ac60257-1885d03c/1885d03c13ef039d25baaab3e86a98b8.simg"
url: https://datasets.datalad.org/shub/pescobar/nace-container/0.1/2018-10-03-1ac60257-1885d03c/
recipe: https://datasets.datalad.org/shub/pescobar/nace-container/0.1/2018-10-03-1ac60257-1885d03c/Singularity
collection: pescobar/nace-container
---

# pescobar/nace-container:0.1

```bash
$ singularity pull shub://pescobar/nace-container:0.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%post

    export PATH=/opt/conda/bin:$PATH

    # make sure to have the latest conda version
    conda update -n base conda

    # add some extra channels
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install some bioinfo tools from Bioconda
    conda install --yes -c bioconda picard==2.14
    conda install --yes -c bioconda fastqc==0.11.7
    conda install --yes -c bioconda samtools==1.9
    conda install --yes -c bioconda bwa==0.7.17
    conda install --yes -c bioconda bedtools==2.27.1
    
    # install some dependencies to build R packages
    apt-get update
    apt-get -y install build-essential gfortran file
    
    # install R and some extra packages
    conda install --yes -c conda-forge eigen
    conda install --yes -c conda-forge pandoc
    conda install --yes -c conda-forge r-base==3.5.1 

    # Install bioconductor and some extra R packages
    Rscript -e "source ('https://bioconductor.org/biocLite.R'); \
    biocLite(); \
    biocLite(c(\
    'acepack',\
    'AnnotationDbi',\
    'AnnotationFilter',\
    'AnnotationHub',\
    'assertthat',\
    'backports',\
    'base',\
    'base64enc',\
    'bindr',\
    'bindrcpp',\
    'Biobase',\
    'BiocGenerics',\
    'BiocInstaller',\
    'BiocParallel',\
    'biomaRt',\
    'Biostrings',\
    'biovizBase',\
    'bit64',\
    'bit',\
    'bitops',\
    'blob',\
    'BSgenome.Hsapiens.UCSC.hg19',\
    'BSgenome',\
    'checkmate',\
    'cluster',\
    'colorspace',\
    'compiler',\
    'curl',\
    'data.table',\
    'datasets',\
    'DBI',\
    'DelayedArray',\
    'dichromat',\
    'digest',\
    'dplyr',\
    'dplyr',\
    'ensembldb',\
    'evaluate',\
    'factoextra',\
    'foreign',\
    'Formula',\
    'GenomeInfoDb',\
    'GenomeInfoDbData',\
    'GenomicAlignments',\
    'GenomicFeatures',\
    'GenomicRanges',\
    'getopt',\
    'GGally',\
    'ggbio',\
    'ggplot2',\
    'ggrepel',\
    'glue',\
    'glue',\
    'graph',\
    'graphics',\
    'grDevices',\
    'grid',\
    'gridExtra',\
    'gtable',\
    'highr',\
    'Hmisc',\
    'htmlTable',\
    'htmltools',\
    'htmlwidgets',\
    'httpuv',\
    'httr',\
    'interactiveDisplayBase',\
    'IRanges',\
    'knitr',\
    'knitr',\
    'knitrBootstrap',\
    'labeling',\
    'lattice',\
    'latticeExtra',\
    'lazyeval',\
    'magrittr',\
    'markdown',\
    'Matrix',\
    'matrixStats',\
    'memoise',\
    'methods',\
    'methods',\
    'mime',\
    'munsell',\
    'nnet',\
    'OrganismDbi',\
    'parallel',\
    'parallel',\
    'pkgconfig',\
    'plyr',\
    'PropCIs',\
    'ProtGenerics',\
    'purrr',\
    'R6',\
    'RAPIDR',\
    'RBGL',\
    'RColorBrewer',\
    'Rcpp',\
    'Rcpp',\
    'RCurl',\
    'reshape2',\
    'reshape',\
    'rlang',\
    'rlang',\
    'rmarkdown',\
    'rpart',\
    'rprojroot',\
    'Rsamtools',\
    'RSQLite',\
    'rtracklayer',\
    'S4Vectors',\
    'scales',\
    'shiny',\
    'splines',\
    'stats',\
    'stats4',\
    'stats4',\
    'stringi',\
    'stringr',\
    'SummarizedExperiment',\
    'survival',\
    'tibble',\
    'tidyselect',\
    'tools',\
    'utils',\
    'VariantAnnotation',\
    'viridis',\
    'viridisLite',\
    'XML',\
    'xtable',\
    'XVector',\
    'yaml',\
    'zlibbioc'))"


%environment
    export PATH=/opt/conda/bin:$PATH
    export XDG_RUNTIME_DIR=""


%apprun samtools
    samtools "$@"

%apprun bwa
    bwa "$@"
```

## Collection

 - Name: [pescobar/nace-container](https://github.com/pescobar/nace-container)
 - License: None

