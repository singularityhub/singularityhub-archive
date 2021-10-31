---
id: 7429
name: "cflerin/pySCENIC"
branch: "master"
tag: "0.9.5"
commit: "c465da50ee600b766177ab5a2b23f227659f08da"
version: "b9340a04b32d635bb11001c75dbe8b6c"
build_date: "2019-02-25T16:42:16.383Z"
size_mb: 1299
size: 453275679
sif: "https://datasets.datalad.org/shub/cflerin/pySCENIC/0.9.5/2019-02-25-c465da50-b9340a04/b9340a04b32d635bb11001c75dbe8b6c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cflerin/pySCENIC/0.9.5/2019-02-25-c465da50-b9340a04/
recipe: https://datasets.datalad.org/shub/cflerin/pySCENIC/0.9.5/2019-02-25-c465da50-b9340a04/Singularity
collection: cflerin/pySCENIC
---

# cflerin/pySCENIC:0.9.5

```bash
$ singularity pull shub://cflerin/pySCENIC:0.9.5
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%post
    . /opt/conda/etc/profile.d/conda.sh
    apt-get update && apt-get install -y build-essential
    conda install python=3.6
    conda activate
    pip install --no-cache-dir --upgrade pyscenic==0.9.5 dask==1.0.0 pandas==0.23.4
```

## Collection

 - Name: [cflerin/pySCENIC](https://github.com/cflerin/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

