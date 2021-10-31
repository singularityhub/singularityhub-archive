---
id: 9787
name: "ethancaballero/singularity-containers"
branch: "master"
tag: "myia_benchmarks_prof"
commit: "fb39b40631d6283c2d244b7a4a3db1f8eacd171a"
version: "200747a591fbd50109da94b75491f97a"
build_date: "2019-06-13T19:52:02.109Z"
size_mb: 6188
size: 3792031775
sif: "https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks_prof/2019-06-13-fb39b406-200747a5/200747a591fbd50109da94b75491f97a.simg"
url: https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks_prof/2019-06-13-fb39b406-200747a5/
recipe: https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks_prof/2019-06-13-fb39b406-200747a5/Singularity
collection: ethancaballero/singularity-containers
---

# ethancaballero/singularity-containers:myia_benchmarks_prof

```bash
$ singularity pull shub://ethancaballero/singularity-containers:myia_benchmarks_prof
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-devel

%environment
 PATH=$PATH:/opt/conda/bin

%post
 apt-get -y update
 apt-get -y install wget vim git zip unzip tar
 wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
 bash miniconda.sh -b -p /opt/conda
 PATH=$PATH:/opt/conda/bin
 git clone https://github.com/mila-iqia/myia.git
 cd myia
 conda install -c abergeron -c pytorch --file=requirements.conda
 pip install -r requirements.txt
 pip install -e . --no-deps
 pip install pyinstrument
```

## Collection

 - Name: [ethancaballero/singularity-containers](https://github.com/ethancaballero/singularity-containers)
 - License: None

