---
id: 10830
name: "motroy/singularity-amrfinder"
branch: "master"
tag: "latest"
commit: "8817b7c2150bc03ecd0da200a729f65b91be5042"
version: "30cd673ba3ab56f17c475b0bdda02a7f"
build_date: "2020-02-27T10:03:42.421Z"
size_mb: 686.0
size: 219996191
sif: "https://datasets.datalad.org/shub/motroy/singularity-amrfinder/latest/2020-02-27-8817b7c2-30cd673b/30cd673ba3ab56f17c475b0bdda02a7f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-amrfinder/latest/2020-02-27-8817b7c2-30cd673b/
recipe: https://datasets.datalad.org/shub/motroy/singularity-amrfinder/latest/2020-02-27-8817b7c2-30cd673b/Singularity
collection: motroy/singularity-amrfinder
---

# motroy/singularity-amrfinder:latest

```bash
$ singularity pull shub://motroy/singularity-amrfinder:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/amrfinderplus/amr/:/amrfinderplus/amr/data/:/usr/bin:$PATH"

%post
apt update && apt install -y git curl wget less locate build-essential openssh-server hmmer ncbi-blast+ libcurl4-openssl-dev
mkdir /amrfinderplus && cd /amrfinderplus
git clone --recursive https://github.com/ncbi/amr.git
cd amr && make
#download and index dbs to ./data/
./amrfinder -u
#test run
./amrfinder -o test_dna.RESULTS -d data/latest/ -n test_dna.fa -O Escherichia
export PATH="/amrfinderplus/amr/:/amrfinderplus/amr/data/:/usr/bin:$PATH"
```

## Collection

 - Name: [motroy/singularity-amrfinder](https://github.com/motroy/singularity-amrfinder)
 - License: [MIT License](https://api.github.com/licenses/mit)

