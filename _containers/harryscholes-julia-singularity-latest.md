---
id: 11204
name: "harryscholes/julia-singularity"
branch: "master"
tag: "latest"
commit: "17c85e8de551f215cc6ff5fd4b8272fe369a49f9"
version: "24facb85892e7655e2bc752fdc323356"
build_date: "2019-11-06T18:32:15.255Z"
size_mb: 427.0
size: 140996639
sif: "https://datasets.datalad.org/shub/harryscholes/julia-singularity/latest/2019-11-06-17c85e8d-24facb85/24facb85892e7655e2bc752fdc323356.sif"
url: https://datasets.datalad.org/shub/harryscholes/julia-singularity/latest/2019-11-06-17c85e8d-24facb85/
recipe: https://datasets.datalad.org/shub/harryscholes/julia-singularity/latest/2019-11-06-17c85e8d-24facb85/Singularity
collection: harryscholes/julia-singularity
---

# harryscholes/julia-singularity:latest

```bash
$ singularity pull shub://harryscholes/julia-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%runscript
julia --startup-file no --history-file no

%environment
export PATH=/julia-1.2.0/bin:$PATH
export LD_LIBRARY_PATH=/julia-1.2.0/lib:/julia-1.2.0/lib/julia:$LD_LIBRARY_PATH
export LC_ALL=C

%post
apt-get -y update
apt-get -y install curl
curl -L "https://julialang-s3.julialang.org/bin/linux/x64/1.2/julia-1.2.0-linux-x86_64.tar.gz" | tar xz
apt-get -y purge curl
apt-get clean
apt-get -y autoremove
```

## Collection

 - Name: [harryscholes/julia-singularity](https://github.com/harryscholes/julia-singularity)
 - License: None

