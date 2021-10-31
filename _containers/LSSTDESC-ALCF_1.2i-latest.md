---
id: 3944
name: "LSSTDESC/ALCF_1.2i"
branch: "master"
tag: "latest"
commit: "5741843f9e5382e7d39fea2bde926f1355edfc62"
version: "7cb36262780b228dba92616f5229fc57"
build_date: "2018-12-03T17:26:30.234Z"
size_mb: 8037
size: 3892191263
sif: "https://datasets.datalad.org/shub/LSSTDESC/ALCF_1.2i/latest/2018-12-03-5741843f-7cb36262/7cb36262780b228dba92616f5229fc57.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/LSSTDESC/ALCF_1.2i/latest/2018-12-03-5741843f-7cb36262/
recipe: https://datasets.datalad.org/shub/LSSTDESC/ALCF_1.2i/latest/2018-12-03-5741843f-7cb36262/Singularity
collection: LSSTDESC/ALCF_1.2i
---

# LSSTDESC/ALCF_1.2i:latest

```bash
$ singularity pull shub://LSSTDESC/ALCF_1.2i:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: avillarreal/alcf_run2.0i:latest

%environment
   /DC2/ALCF_1.2i/docker_run.sh

%runscript
   exec python /DC2/ALCF_1.2i/scripts/run_imsim.py "$@"
```

## Collection

 - Name: [LSSTDESC/ALCF_1.2i](https://github.com/LSSTDESC/ALCF_1.2i)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

