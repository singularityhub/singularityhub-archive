---
id: 9755
name: "ethancaballero/singularity-containers"
branch: "master"
tag: "myia_benchmarks"
commit: "6189c921b40cd788fcaef04e9074d0b8fd5003c1"
version: "74042648f161029eb4a5c6589db8f985"
build_date: "2019-06-12T11:53:04.553Z"
size_mb: 3890
size: 2401136671
sif: "https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks/2019-06-12-6189c921-74042648/74042648f161029eb4a5c6589db8f985.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ethancaballero/singularity-containers/myia_benchmarks/2019-06-12-6189c921-74042648/
recipe: https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks/2019-06-12-6189c921-74042648/Singularity
collection: ethancaballero/singularity-containers
---

# ethancaballero/singularity-containers:myia_benchmarks

```bash
$ singularity pull shub://ethancaballero/singularity-containers:myia_benchmarks
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%environment
    PATH=$PATH:/opt/conda/bin

%post
    PATH=$PATH:/opt/conda/bin
    git clone https://github.com/mila-iqia/myia.git
    cd myia
    conda install -c abergeron -c pytorch --file=requirements.conda
    pip install -r requirements.txt
    pip install -e . --no-deps
```

## Collection

 - Name: [ethancaballero/singularity-containers](https://github.com/ethancaballero/singularity-containers)
 - License: None

