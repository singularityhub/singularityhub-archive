---
id: 1728
name: "endrebak/singularity_recipes"
branch: "master"
tag: "chipseeker_1_14_0"
commit: "4a97fa7dce918b66f717db00a5a4b5fdb9d1a9cb"
version: "0f8af44053927f7aa76d22e141a052d9"
build_date: "2018-02-16T17:20:20.108Z"
size_mb: 8813
size: 3153326111
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/chipseeker_1_14_0/2018-02-16-4a97fa7d-0f8af440/0f8af44053927f7aa76d22e141a052d9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/endrebak/singularity_recipes/chipseeker_1_14_0/2018-02-16-4a97fa7d-0f8af440/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/chipseeker_1_14_0/2018-02-16-4a97fa7d-0f8af440/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:chipseeker_1_14_0

```bash
$ singularity pull shub://endrebak/singularity_recipes:chipseeker_1_14_0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/anaconda3

%post
export PATH=/opt/conda/bin:${PATH}
echo 'export PATH=/opt/conda/bin:${PATH}' >> $SINGULARITY_ENVIRONMENT
conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge
conda install bioconductor-chipseeker bioconductor-txdb.celegans.ucsc.ce11.refgene bioconductor-txdb.celegans.ucsc.ce6.ensgene bioconductor-txdb.dmelanogaster.ucsc.dm3.ensgene bioconductor-txdb.dmelanogaster.ucsc.dm6.ensgene bioconductor-txdb.drerio.ucsc.danrer10.refgene bioconductor-txdb.hsapiens.ucsc.hg18.knowngene bioconductor-txdb.hsapiens.ucsc.hg19.knowngene bioconductor-txdb.hsapiens.ucsc.hg19.lincrnastranscripts bioconductor-txdb.hsapiens.ucsc.hg38.knowngene bioconductor-txdb.mmusculus.ucsc.mm10.ensgene bioconductor-txdb.mmusculus.ucsc.mm10.knowngene bioconductor-txdb.mmusculus.ucsc.mm9.knowngene bioconductor-txdb.rnorvegicus.ucsc.rn4.ensgene bioconductor-txdb.rnorvegicus.ucsc.rn5.refgene bioconductor-txdb.rnorvegicus.ucsc.rn6.refgene bioconductor-txdb.scerevisiae.ucsc.saccer2.sgdgene bioconductor-txdb.scerevisiae.ucsc.saccer3.sgdgene bioconductor-org.bt.eg.db bioconductor-org.ce.eg.db bioconductor-org.cf.eg.db bioconductor-org.dm.eg.db bioconductor-org.dr.eg.db bioconductor-org.gg.eg.db bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-org.rn.eg.db bioconductor-org.sc.sgd.db bioconductor-org.ss.eg.db bioconductor-dose bioconductor-reactomepa bioconductor-clusterprofiler
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

