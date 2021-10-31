---
id: 12761
name: "DylanYang7225/Cellranger"
branch: "master"
tag: "latest"
commit: "21aba335314b9cf143140c2973b2c5e2a14cf8b0"
version: "28b38b1e2e5e72b258fcd6b8bb162d56"
build_date: "2021-01-27T15:36:53.297Z"
size_mb: 19938.0
size: 12548964383
sif: "https://datasets.datalad.org/shub/DylanYang7225/Cellranger/latest/2021-01-27-21aba335-28b38b1e/28b38b1e2e5e72b258fcd6b8bb162d56.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/DylanYang7225/Cellranger/latest/2021-01-27-21aba335-28b38b1e/
recipe: https://datasets.datalad.org/shub/DylanYang7225/Cellranger/latest/2021-01-27-21aba335-28b38b1e/Singularity
collection: DylanYang7225/Cellranger
---

# DylanYang7225/Cellranger:latest

```bash
$ singularity pull shub://DylanYang7225/Cellranger:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%labels
    Maintainer Hang(Dylan) Yang	
    Image_Name CellRanger
    Image_Version CellRanger_3.1.0
    
%environment
  export PATH=$PATH:/cellranger/cellranger-3.1.0

%post
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get install -y wget

  #--------------------------------------------------------------------------------
  # install cellranger and reference genome
  mkdir -p /cellranger
  cd /cellranger 
  wget -O cellranger-3.1.0.tar.gz "http://cf.10xgenomics.com/releases/cell-vdj/cellranger-3.1.0.tar.gz?Expires=1587461847&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9jZWxsLXZkai9jZWxscmFuZ2VyLTMuMS4wLnRhci5neiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU4NzQ2MTg0N319fV19&Signature=SOKsLLbobRGQ3zoALtK6xZzb6Fa-~PqJ~1iQ5xGTo-8mCyBfCZcTIZ6uPEJ6fh4y9IBLavpsENR9eUjKyGARBJe6lD43y20GbSqtQCDozDPMZnFJ58QNJuzbkIaS4q38c3jOjQNBlRzosTX4zcmU4XKL-M33Uq9obToEIQEpUhmA1u5FeqZgzn4LcfF-1NNOmX2i7yuLdcpULFxo1ChVD7YCSo09gCqyT9qs4sJWiAY~gFCJuaumPPuVaa8Q466Za3mbj0fdYeH-vCbxNIjdRiztzllWW-xF-z7inBolGfcScdVcz0V1ZuhthsXm2w7draBWRlesqsaS69DBNWRD3w__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"
  wget http://cf.10xgenomics.com/supp/cell-exp/refdata-cellranger-GRCh38-3.0.0.tar.gz
  wget http://cf.10xgenomics.com/supp/cell-vdj/refdata-cellranger-vdj-GRCh38-alts-ensembl-3.1.0.tar.gz
  tar -xvzf refdata-cellranger-GRCh38-3.0.0.tar.gz
  tar -xvzf cellranger-3.1.0.tar.gz
  tar -xvzf refdata-cellranger-vdj-GRCh38-alts-ensembl-3.1.0.tar.gz
  rm refdata-cellranger-GRCh38-3.0.0.tar.gz
  rm cellranger-3.1.0.tar.gz
  rm refdata-cellranger-vdj-GRCh38-alts-ensembl-3.1.0.tar.gz
   
# Create directories to bind-mount data and reference genome and to store output
  mkdir -p /output 
  mkdir -p /data 
  mkdir -p /work/scratch
```

## Collection

 - Name: [DylanYang7225/Cellranger](https://github.com/DylanYang7225/Cellranger)
 - License: None

