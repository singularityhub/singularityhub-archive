---
id: 7177
name: "motroy/singularity-CAT"
branch: "master"
tag: "latest"
commit: "d37b5cfbe43267a916c1edd4824f19d019ec2e34"
version: "d711115e769a9842d216f293683b0fb9"
build_date: "2019-02-13T20:23:58.138Z"
size_mb: 649
size: 247033887
sif: "https://datasets.datalad.org/shub/motroy/singularity-CAT/latest/2019-02-13-d37b5cfb-d711115e/d711115e769a9842d216f293683b0fb9.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-CAT/latest/2019-02-13-d37b5cfb-d711115e/
recipe: https://datasets.datalad.org/shub/motroy/singularity-CAT/latest/2019-02-13-d37b5cfb-d711115e/Singularity
collection: motroy/singularity-CAT
---

# motroy/singularity-CAT:latest

```bash
$ singularity pull shub://motroy/singularity-CAT:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/Software/CAT/CAT_pack:/Software/Prodigal:/Software/diamond/bin:$PATH"


%post
apt update && apt install -y git curl wget less locate unzip build-essential python3 python3-dev python3-pip gcc cmake libpthread-stubs0-dev zlib1g-dev
mkdir -p /Software/ && cd /Software/
git clone --recursive https://github.com/dutilh/CAT.git
export PATH="/Software/CAT/CAT_pack:$PATH"

cd /Software/
git clone --recursive https://github.com/hyattpd/Prodigal.git
cd Prodigal
make install
export PATH="/Software/Prodigal:$PATH"

cd /Software/
git clone --recursive https://github.com/bbuchfink/diamond.git
cd diamond
mkdir bin && cd bin
cmake ..
make install
export PATH="/Software/diamond/bin:$PATH"
```

## Collection

 - Name: [motroy/singularity-CAT](https://github.com/motroy/singularity-CAT)
 - License: [MIT License](https://api.github.com/licenses/mit)

