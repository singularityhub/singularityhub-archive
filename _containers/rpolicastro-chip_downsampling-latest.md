---
id: 9848
name: "rpolicastro/chip_downsampling"
branch: "dev"
tag: "latest"
commit: "96ba7a5e2c589c727fef5109a1fe3cebd5f4cf1f"
version: "9f0202cd088299b924e3c8dd8f4bc036"
build_date: "2020-03-06T14:32:37.862Z"
size_mb: 1507
size: 518557727
sif: "https://datasets.datalad.org/shub/rpolicastro/chip_downsampling/latest/2020-03-06-96ba7a5e-9f0202cd/9f0202cd088299b924e3c8dd8f4bc036.simg"
url: https://datasets.datalad.org/shub/rpolicastro/chip_downsampling/latest/2020-03-06-96ba7a5e-9f0202cd/
recipe: https://datasets.datalad.org/shub/rpolicastro/chip_downsampling/latest/2020-03-06-96ba7a5e-9f0202cd/Singularity
collection: rpolicastro/chip_downsampling
---

# rpolicastro/chip_downsampling:latest

```bash
$ singularity pull shub://rpolicastro/chip_downsampling:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%post

## Add conda to path
export PATH=$PATH:/opt/conda/bin

## Update conda
conda update -n base -y -c defaults conda

## Install chipseq-automation software
conda create -n chip-downsampling -y -c conda-forge -c bioconda \
r-getopt samtools bioconductor-rsubread macs2

## Update chipseq-automation environment
conda update -n chip-downsampling -y -c conda-forge -c bioconda --all

## Clean up extra files
conda clean --all
```

## Collection

 - Name: [rpolicastro/chip_downsampling](https://github.com/rpolicastro/chip_downsampling)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

