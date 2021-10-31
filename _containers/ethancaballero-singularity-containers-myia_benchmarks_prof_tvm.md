---
id: 9854
name: "ethancaballero/singularity-containers"
branch: "master"
tag: "myia_benchmarks_prof_tvm"
commit: "fb9f824179f74a0d220a975a6fd50188d08920fd"
version: "e78abfd3f3d8f963b30879df71595d54"
build_date: "2019-06-18T02:03:56.918Z"
size_mb: 6993
size: 4369104927
sif: "https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks_prof_tvm/2019-06-18-fb9f8241-e78abfd3/e78abfd3f3d8f963b30879df71595d54.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ethancaballero/singularity-containers/myia_benchmarks_prof_tvm/2019-06-18-fb9f8241-e78abfd3/
recipe: https://datasets.datalad.org/shub/ethancaballero/singularity-containers/myia_benchmarks_prof_tvm/2019-06-18-fb9f8241-e78abfd3/Singularity
collection: ethancaballero/singularity-containers
---

# ethancaballero/singularity-containers:myia_benchmarks_prof_tvm

```bash
$ singularity pull shub://ethancaballero/singularity-containers:myia_benchmarks_prof_tvm
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
 conda remove nnvm topi
 conda upgrade -c abergeron tvm
 conda install -c abergeron/label/cuda tvm-libs cudatoolkit=10.0
 pip install -r requirements.txt
 pip install -e . --no-deps
 pip install pyinstrument
```

## Collection

 - Name: [ethancaballero/singularity-containers](https://github.com/ethancaballero/singularity-containers)
 - License: None

