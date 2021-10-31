---
id: 15558
name: "timo-singularity/pytorch"
branch: "master"
tag: "latest"
commit: "862ac2816f9ac5772a8357eb520630f83b1ef196"
version: "131e565de1cfcaa9c03b682d4683ec31"
build_date: "2021-04-06T07:13:24.526Z"
size_mb: 6865.0
size: 1957732383
sif: "https://datasets.datalad.org/shub/timo-singularity/pytorch/latest/2021-04-06-862ac281-131e565d/131e565de1cfcaa9c03b682d4683ec31.sif"
url: https://datasets.datalad.org/shub/timo-singularity/pytorch/latest/2021-04-06-862ac281-131e565d/
recipe: https://datasets.datalad.org/shub/timo-singularity/pytorch/latest/2021-04-06-862ac281-131e565d/Singularity
collection: timo-singularity/pytorch
---

# timo-singularity/pytorch:latest

```bash
$ singularity pull shub://timo-singularity/pytorch:latest
```

## Singularity Recipe

```singularity
#Bootstrap: localimage
#From: ./sherpa.sif
Bootstrap: shub
From: timo-singularity/sherpa

%help

  Container with Rivet, Sherpa, Pytorch

%post

  yum -y install git
  
  pip3 --no-cache-dir install cython numpy scipy
  pip3 --no-cache-dir install torch torchvision
  pip3 --no-cache-dir install matplotlib pandas seaborn
  pip3 --no-cache-dir install ipykernel jupyterlab
  
  pip3 --no-cache-dir install numdifftools nflows
  pip3 --no-cache-dir install gvar
  git clone https://gitlab.com/tjansse/vegas.git
  pip3 install ./vegas

   # we need to downgrade jedi, as there is a problem with auto-completion
  # in the current jupyter
  pip3 --no-cache-dir install --force-reinstall jedi==0.17.2

  ldconfig
  yum clean all
```

## Collection

 - Name: [timo-singularity/pytorch](https://github.com/timo-singularity/pytorch)
 - License: None

