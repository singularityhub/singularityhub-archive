---
id: 9947
name: "jemunro/nf-wgs-raxml-ng"
branch: "master"
tag: "latest"
commit: "1a039846a31b31e5615601a69555b5c0db5ee324"
version: "d52be8c6f60213e5aa4799eac59c56cc"
build_date: "2019-08-19T03:15:12.092Z"
size_mb: 835
size: 313749535
sif: "https://datasets.datalad.org/shub/jemunro/nf-wgs-raxml-ng/latest/2019-08-19-1a039846-d52be8c6/d52be8c6f60213e5aa4799eac59c56cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jemunro/nf-wgs-raxml-ng/latest/2019-08-19-1a039846-d52be8c6/
recipe: https://datasets.datalad.org/shub/jemunro/nf-wgs-raxml-ng/latest/2019-08-19-1a039846-d52be8c6/Singularity
collection: jemunro/nf-wgs-raxml-ng
---

# jemunro/nf-wgs-raxml-ng:latest

```bash
$ singularity pull shub://jemunro/nf-wgs-raxml-ng:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    MAINTAINER Jacob Munro
    AUTHOR Bahlo Lab
    DESCRIPTION raxml-ng container
    VERSION 0.0.1

%files
    environment.yml /

%post
    apt-get update && apt-get install -y procps
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean --all -y

%environment
    export PATH="/opt/conda/envs/raxml-ng/bin:/opt/conda/bin:$PATH"
```

## Collection

 - Name: [jemunro/nf-wgs-raxml-ng](https://github.com/jemunro/nf-wgs-raxml-ng)
 - License: None

