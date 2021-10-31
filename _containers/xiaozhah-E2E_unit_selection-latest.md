---
id: 10297
name: "xiaozhah/E2E_unit_selection"
branch: "master"
tag: "latest"
commit: "99385d958e33c914935849466c2dba5534c63d48"
version: "bda9aaea8c46bd9c272457789af800e4"
build_date: "2020-04-30T05:42:17.845Z"
size_mb: 3995.0
size: 1920696351
sif: "https://datasets.datalad.org/shub/xiaozhah/E2E_unit_selection/latest/2020-04-30-99385d95-bda9aaea/bda9aaea8c46bd9c272457789af800e4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/xiaozhah/E2E_unit_selection/latest/2020-04-30-99385d95-bda9aaea/
recipe: https://datasets.datalad.org/shub/xiaozhah/E2E_unit_selection/latest/2020-04-30-99385d95-bda9aaea/Singularity
collection: xiaozhah/E2E_unit_selection
---

# xiaozhah/E2E_unit_selection:latest

```bash
$ singularity pull shub://xiaozhah/E2E_unit_selection:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:latest
 
%labels
  Author Zhou Xiao
  Version v1.0.2
  build_date 2019 July 22

%post
  apt-get update
  apt-get upgrade -y
  apt-get install -y tmux htop ranger tree ncdu wget zip unzip nano
  apt-get autoclean
  
  /opt/conda/bin/pip install tensorflow==1.13.1 tensorboardX==1.1 numpy inflect librosa==0.6.3 pillow scipy matplotlib tqdm
```

## Collection

 - Name: [xiaozhah/E2E_unit_selection](https://github.com/xiaozhah/E2E_unit_selection)
 - License: None

