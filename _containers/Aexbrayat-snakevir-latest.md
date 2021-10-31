---
id: 11977
name: "Aexbrayat/snakevir"
branch: "master"
tag: "latest"
commit: "02b2df29aaf5173893ee8b3436a49ba8107b6334"
version: "2af0c52b4e3fae19d7074951d36a875b"
build_date: "2020-01-10T09:23:04.513Z"
size_mb: 4911.0
size: 2240897055
sif: "https://datasets.datalad.org/shub/Aexbrayat/snakevir/latest/2020-01-10-02b2df29-2af0c52b/2af0c52b4e3fae19d7074951d36a875b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Aexbrayat/snakevir/latest/2020-01-10-02b2df29-2af0c52b/
recipe: https://datasets.datalad.org/shub/Aexbrayat/snakevir/latest/2020-01-10-02b2df29-2af0c52b/Singularity
collection: Aexbrayat/snakevir
---

# Aexbrayat/snakevir:latest

```bash
$ singularity pull shub://Aexbrayat/snakevir:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# sudo singularity build snakemake Singularity

%files
    snakevir.scif
    Snakefile
    config.yaml

%environment
    PATH=/opt/conda/bin:$PATH
    export PATH

%post
    mkdir -p /samples /data /snakevirome
    apt-get update && apt-get -y install build-essential valgrind time python-numpy python-dev python-qt4 python-lxml python-six
    /opt/conda/bin/conda config --add channels defaults
    /opt/conda/bin/conda config --add channels conda-forge
    /opt/conda/bin/conda config --add channels bioconda

    # Install scif and scif-apps
    /opt/conda/bin/pip install scif
    /opt/conda/bin/scif install /snakevir.scif

    # Install snakemake
    /opt/conda/bin/pip install snakemake==4.4.0
    /opt/conda/bin/pip install docutils==0.14
    /opt/conda/bin/pip install biopython
    /opt/conda/bin/pip install pandas
    /opt/conda/bin/python - <<EOF
from ete3 import NCBITaxa
ncbi = NCBITaxa()
ncbi.update_taxonomy_database()

%runscript
    PATH=/opt/conda/bin:$PATH
    export PATH
    exec scif "$@"
```

## Collection

 - Name: [Aexbrayat/snakevir](https://github.com/Aexbrayat/snakevir)
 - License: None

