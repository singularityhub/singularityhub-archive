---
id: 11962
name: "Aexbrayat/snakescif"
branch: "master"
tag: "latest"
commit: "7c2349ae5306744417cb6464008f29f804156588"
version: "05ffe76063511d067feea53a1cffb154"
build_date: "2020-10-24T18:16:22.555Z"
size_mb: 6304.0
size: 2833498143
sif: "https://datasets.datalad.org/shub/Aexbrayat/snakescif/latest/2020-10-24-7c2349ae-05ffe760/05ffe76063511d067feea53a1cffb154.sif"
url: https://datasets.datalad.org/shub/Aexbrayat/snakescif/latest/2020-10-24-7c2349ae-05ffe760/
recipe: https://datasets.datalad.org/shub/Aexbrayat/snakescif/latest/2020-10-24-7c2349ae-05ffe760/Singularity
collection: Aexbrayat/snakescif
---

# Aexbrayat/snakescif:latest

```bash
$ singularity pull shub://Aexbrayat/snakescif:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.3.27

# sudo singularity build snakemake Singularity

%files
    snakevir.scif
    Snakefile
    config.yaml
    cluster.json
    

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
    /opt/conda/bin/pip install snakemake==5.7.4
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

 - Name: [Aexbrayat/snakescif](https://github.com/Aexbrayat/snakescif)
 - License: None

