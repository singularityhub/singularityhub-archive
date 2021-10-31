---
id: 7681
name: "MacIver-Lab/Ergodic-Information-Harvesting"
branch: "master"
tag: "latest"
commit: "d2715e68bf4d9f0373e9684fae8b46c70d08d8df"
version: "a3c2018b57492682d0b082075dcd8a5c"
build_date: "2019-03-10T21:28:11.068Z"
size_mb: 915
size: 323682335
sif: "https://datasets.datalad.org/shub/MacIver-Lab/Ergodic-Information-Harvesting/latest/2019-03-10-d2715e68-a3c2018b/a3c2018b57492682d0b082075dcd8a5c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MacIver-Lab/Ergodic-Information-Harvesting/latest/2019-03-10-d2715e68-a3c2018b/
recipe: https://datasets.datalad.org/shub/MacIver-Lab/Ergodic-Information-Harvesting/latest/2019-03-10-d2715e68-a3c2018b/Singularity
collection: MacIver-Lab/Ergodic-Information-Harvesting
---

# MacIver-Lab/Ergodic-Information-Harvesting:latest

```bash
$ singularity pull shub://MacIver-Lab/Ergodic-Information-Harvesting:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%help
    This is a Singularity container for EIH simulations.
    It builds a minimal Python 3 environment running on Linux with all the libraries required for EIH simulations.

%labels
    Maintainer Chen Chen (chenchen.bme@gmail.com)
    Version v0.2
   
%environment
     export conda=/opt/conda/bin/conda
     export pip=/opt/conda/bin/pip
     export python3=/opt/conda/bin/python
     export python=python3

%post 
     # update system and install gcc
     apt-get update
     apt-get install gcc g++ -y
     # update conda
     /opt/conda/bin/conda update --all -y --quiet
     # Update pip
     /opt/conda/bin/pip install -U pip -q
     # Install dependencies
     /opt/conda/bin/conda install -c conda-forge -y -q tqdm cython numba scipy=1.0.1 numpy=1.16.1 
     # Clean up
     /opt/conda/bin/conda clean --all -y --quiet
     apt-get autoremove -y
     apt-get clean
     # create bind points for HPCC environment
     mkdir -p /EIH

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [MacIver-Lab/Ergodic-Information-Harvesting](https://github.com/MacIver-Lab/Ergodic-Information-Harvesting)
 - License: [MIT License](https://api.github.com/licenses/mit)

