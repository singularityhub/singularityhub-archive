---
id: 9774
name: "nrachman/reproducibility"
branch: "master"
tag: "latest"
commit: "6bf29a4259ecbb3ff3e75413f6f680810bf4ceb3"
version: "c8c83a5357bbd5f2ddfba2366ba14823"
build_date: "2019-06-13T14:46:44.406Z"
size_mb: 3094
size: 1032818719
sif: "https://datasets.datalad.org/shub/nrachman/reproducibility/latest/2019-06-13-6bf29a42-c8c83a53/c8c83a5357bbd5f2ddfba2366ba14823.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nrachman/reproducibility/latest/2019-06-13-6bf29a42-c8c83a53/
recipe: https://datasets.datalad.org/shub/nrachman/reproducibility/latest/2019-06-13-6bf29a42-c8c83a53/Singularity
collection: nrachman/reproducibility
---

# nrachman/reproducibility:latest

```bash
$ singularity pull shub://nrachman/reproducibility:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularity-hub.org/ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463:latest 
##the shub:// tag should not be included
##see https://github.com/sylabs/singularity/issues/2847


%post
  sudo apt-get update
  sudo apt-get -y install libcairo2-dev #for arrayQualityMetrics
  sudo apt-get -y install libxt-dev #for arrayQualityMetrics
  sudo apt-get -y install libudunits2-dev #for ggraph

  R -e "install.packages('gridSVG')" #required by arrayQualityMetrics

  R -e "BiocManager::install('limma')"
  R -e "BiocManager::install('variancePartition')"
  R -e "BiocManager::install('oligo')"
  R -e "BiocManager::install('preprocessCore')" #needed for metaintegrator
  R -e "BiocManager::install('arrayQualityMetrics')"
  R -e "BiocManager::install('GEOquery')"
  R -e "BiocManager::install('sva')"
  R -e "BiocManager::install('impute')"
  R -e "BiocManager::install('GO.db')" #needed for WGCNA
  R -e "BiocManager::install('multtest')" #needed for metaintegrator
  R -e "BiocManager::install('GEOmetadb')"  #needed for metaintegrator
  
  R -e "install.packages('knitr')"
  R -e "install.packages('tidyverse')"
  R -e "install.packages('plyr')" #used in pick probeset code
  R -e "install.packages('r.jive')"
  R -e "install.packages('ComplexHeatmap')"
  R -e "install.packages('pheatmap')"
  R -e "install.packages('tidygraph')"
  R -e "install.packages('units')"
  R -e "install.packages('ggraph')"
  R -e "install.packages('igraph')"
  R -e "install.packages('randomForest')"
  R -e "install.packages('reshape2')"
  R -e "install.packages('fpc')"
  R -e "install.packages('glmnet')"
  R -e "install.packages('WGCNA')"
 
  R -e "install.packages('ggpubr')"
  R -e "install.packages('ggrepel')"
  R -e "install.packages('cowplot')"
  R -e "install.packages('gridExtra')"
  R -e "install.packages('MetaIntegrator')"
  R -e "install.packages('ROCR')"
  R -e "install.packages('pROC')"
```

## Collection

 - Name: [nrachman/reproducibility](https://github.com/nrachman/reproducibility)
 - License: None

