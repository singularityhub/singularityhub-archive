---
id: 7118
name: "motroy/singularity-kaiju-progen"
branch: "master"
tag: "latest"
commit: "faf8ac1de208db84f1f133ddd63fe42fcdefccf6"
version: "76a5ad90e532a65f888473ed26575efe"
build_date: "2020-07-10T21:12:41.711Z"
size_mb: 468
size: 164663327
sif: "https://datasets.datalad.org/shub/motroy/singularity-kaiju-progen/latest/2020-07-10-faf8ac1d-76a5ad90/76a5ad90e532a65f888473ed26575efe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-kaiju-progen/latest/2020-07-10-faf8ac1d-76a5ad90/
recipe: https://datasets.datalad.org/shub/motroy/singularity-kaiju-progen/latest/2020-07-10-faf8ac1d-76a5ad90/Singularity
collection: motroy/singularity-kaiju-progen
---

# motroy/singularity-kaiju-progen:latest

```bash
$ singularity pull shub://motroy/singularity-kaiju-progen:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/Software/kaiju/bin:/Software/kaiju/databases$PATH"


%post
mkdir /Software && cd /Software
apt update && apt install -y git curl wget less locate build-essential openssh-server g++ libz-dev

git clone https://github.com/bioinformatics-centre/kaiju.git
cd kaiju/src && make
mkdir /Software/kaiju/databases && cd /Software/kaiju/databases
#wget http://kaiju.binf.ku.dk/database/kaiju_db_progenomes_2019-02-05.tgz
#tar xvf http://kaiju.binf.ku.dk/database/kaiju_db_progenomes_2019-02-05.tgz
export PATH="/Software/kaiju/bin:/Software/kaiju/databases$PATH"
```

## Collection

 - Name: [motroy/singularity-kaiju-progen](https://github.com/motroy/singularity-kaiju-progen)
 - License: [MIT License](https://api.github.com/licenses/mit)

