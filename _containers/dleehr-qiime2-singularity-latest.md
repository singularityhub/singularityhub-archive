---
id: 1196
name: "dleehr/qiime2-singularity"
branch: "master"
tag: "latest"
commit: "51146bc68e89452b15e5e9762af90d403e20d083"
version: "e97319db8c62aad5b2262690b05adfdc"
build_date: "2020-04-29T00:48:48.820Z"
size_mb: 5972
size: 2638270495
sif: "https://datasets.datalad.org/shub/dleehr/qiime2-singularity/latest/2020-04-29-51146bc6-e97319db/e97319db8c62aad5b2262690b05adfdc.simg"
url: https://datasets.datalad.org/shub/dleehr/qiime2-singularity/latest/2020-04-29-51146bc6-e97319db/
recipe: https://datasets.datalad.org/shub/dleehr/qiime2-singularity/latest/2020-04-29-51146bc6-e97319db/Singularity
collection: dleehr/qiime2-singularity
---

# dleehr/qiime2-singularity:latest

```bash
$ singularity pull shub://dleehr/qiime2-singularity:latest
```

## Singularity Recipe

```singularity
# Adapted from https://github.com/qiime2/vm-playbooks/blob/master/docker/Dockerfile

BootStrap: docker
From: continuumio/miniconda3:4.3.27p0

%runscript
/opt/conda/bin/qiime "$@"

%post
export QIIME2_RELEASE=2017.12
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export MPLBACKEND=agg
export PATH=/opt/conda/bin:${PATH}

# Required by qt
apt update && apt install -y libgl1-mesa-swx11
# conda update -q -y conda
conda install --file https://data.qiime2.org/distro/core/qiime2-${QIIME2_RELEASE}-conda-linux-64.txt
qiime dev refresh-cache
```

## Collection

 - Name: [dleehr/qiime2-singularity](https://github.com/dleehr/qiime2-singularity)
 - License: None

