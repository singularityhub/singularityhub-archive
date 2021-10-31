---
id: 10499
name: "peterk87/viral-ampliseq-assembly"
branch: "master"
tag: "latest"
commit: "60e7cdb0b43ffcf9a90bb535577e26152febff11"
version: "f45ccb63cd12e7f674490464dabc435f"
build_date: "2020-09-28T15:29:58.718Z"
size_mb: 3909.0
size: 1307729951
sif: "https://datasets.datalad.org/shub/peterk87/viral-ampliseq-assembly/latest/2020-09-28-60e7cdb0-f45ccb63/f45ccb63cd12e7f674490464dabc435f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/peterk87/viral-ampliseq-assembly/latest/2020-09-28-60e7cdb0-f45ccb63/
recipe: https://datasets.datalad.org/shub/peterk87/viral-ampliseq-assembly/latest/2020-09-28-60e7cdb0-f45ccb63/Singularity
collection: peterk87/viral-ampliseq-assembly
---

# peterk87/viral-ampliseq-assembly:latest

```bash
$ singularity pull shub://peterk87/viral-ampliseq-assembly:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:4.6.14

%labels
    MAINTAINER Peter Kruczkiewicz
    DESCRIPTION Singularity image containing all requirements for the peterk87/viral-ampliseq-assembly
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/viral-ampliseq-assembly-1.0.0/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    export PATH=/opt/conda/bin:$PATH
    apt-get update && apt-get install -y procps curl && apt-get clean -y
    conda install conda=4.7.10
    conda env create -f /environment.yml
    conda clean -a
```

## Collection

 - Name: [peterk87/viral-ampliseq-assembly](https://github.com/peterk87/viral-ampliseq-assembly)
 - License: [MIT License](https://api.github.com/licenses/mit)

