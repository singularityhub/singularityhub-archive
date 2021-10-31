---
id: 6009
name: "ISU-HPC/cDNA_cupcake"
branch: "master"
tag: "5.8.0"
commit: "d6d4314cedcfb835b24c4c39103723b4f9aa3bfa"
version: "17fb3cf214e5e57d1d654b28a7253dde"
build_date: "2018-12-18T23:11:37.990Z"
size_mb: 2137
size: 1050931231
sif: "https://datasets.datalad.org/shub/ISU-HPC/cDNA_cupcake/5.8.0/2018-12-18-d6d4314c-17fb3cf2/17fb3cf214e5e57d1d654b28a7253dde.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/cDNA_cupcake/5.8.0/2018-12-18-d6d4314c-17fb3cf2/
recipe: https://datasets.datalad.org/shub/ISU-HPC/cDNA_cupcake/5.8.0/2018-12-18-d6d4314c-17fb3cf2/Singularity
collection: ISU-HPC/cDNA_cupcake
---

# ISU-HPC/cDNA_cupcake:5.8.0

```bash
$ singularity pull shub://ISU-HPC/cDNA_cupcake:5.8.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda


%labels
MAINTAINER ynanyam@iastate.edu

%post

#install CDNA_cupcake
apt update -y
apt install -y gcc zlib1g-dev
. /opt/conda/bin/activate base
cd /opt
git clone https://github.com/Magdoll/cDNA_Cupcake.git
cd cDNA_Cupcake
conda install -y setuptools numpy
python setup.py build
python setup.py install
```

## Collection

 - Name: [ISU-HPC/cDNA_cupcake](https://github.com/ISU-HPC/cDNA_cupcake)
 - License: None

