---
id: 14973
name: "GuillaumeStuder/essai_hackathon_container"
branch: "main"
tag: "latest"
commit: "b42a20a898bb66e879d2692ab708c5555d815fbd"
version: "85e11aec142eaa1d968c0580deaf8e20"
build_date: "2020-11-27T00:39:55.757Z"
size_mb: 1860.0
size: 693100575
sif: "https://datasets.datalad.org/shub/GuillaumeStuder/essai_hackathon_container/latest/2020-11-27-b42a20a8-85e11aec/85e11aec142eaa1d968c0580deaf8e20.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/GuillaumeStuder/essai_hackathon_container/latest/2020-11-27-b42a20a8-85e11aec/
recipe: https://datasets.datalad.org/shub/GuillaumeStuder/essai_hackathon_container/latest/2020-11-27-b42a20a8-85e11aec/Singularity
collection: GuillaumeStuder/essai_hackathon_container
---

# GuillaumeStuder/essai_hackathon_container:latest

```bash
$ singularity pull shub://GuillaumeStuder/essai_hackathon_container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: r-base:4.0.2

%labels
  Maintainer Guillaume Studer
  base.image="r-base:4.0.2"
  version="1"
  software="EnhencedVolcano+DESeq2+FactoMineR+factoextra"
%help
  Please faites que ca fonctionne
%post
  apt-get update
  apt-get install -y procps libssl-dev libcurl4-gnutls-dev curl git libopenmpi-dev openmpi-bin openmpi-doc libxml2-dev
  
  R --slave -e 'install.packages("ggplot2")'
  R --slave -e 'install.packages("ggrepel")'
  R --slave -e 'install.packages("FactoMineR")'
  R --slave -e 'install.packages("factoextra")'
  R --slave -e 'install.packages("matrixStats")'
  R --slave -e 'install.packages("ggalt")'
  R --slave -e 'install.packages("ggrastr")'
  R --slave -e 'install.packages("knitr")'
  R --slave -e 'install.packages("gridExtra")'
  R --slave -e 'install.packages("RUnit")'
  
  
  R --slave -e 'install.packages("BiocManager")'
  R --slave -e 'BiocManager::install("airway")'
  R --slave -e 'BiocManager::install("org.Hs.eg.db")'
  R --slave -e 'BiocManager::install("pasilla")'
  R --slave -e 'BiocManager::install("magrittr")'
  R --slave -e 'BiocManager::install("BiocGenerics")'
  R --slave -e 'BiocManager::install("GenomeInfoDb")'
  R --slave -e 'BiocManager::install("MatrixGenerics")'
  R --slave -e 'BiocManager::install("Biobase")'
  R --slave -e 'BiocManager::install("IRanges")'
  R --slave -e 'BiocManager::install("S4Vectors")'
  R --slave -e 'BiocManager::install("GenomicRanges")'
  R --slave -e 'BiocManager::install("SummarizedExperiment")'
  R --slave -e 'BiocManager::install("DESeq2")'
  R --slave -e 'BiocManager::install("EnhancedVolcano")'
```

## Collection

 - Name: [GuillaumeStuder/essai_hackathon_container](https://github.com/GuillaumeStuder/essai_hackathon_container)
 - License: None

