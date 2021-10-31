---
id: 7179
name: "motroy/singularity-opal"
branch: "master"
tag: "latest"
commit: "88ecfe9d3da2a5fbd72d95b38f7ef9e6175151fd"
version: "53bf84309ee17056c4838d8404d6fc95"
build_date: "2019-02-13T20:23:58.148Z"
size_mb: 4189
size: 1373454367
sif: "https://datasets.datalad.org/shub/motroy/singularity-opal/latest/2019-02-13-88ecfe9d-53bf8430/53bf84309ee17056c4838d8404d6fc95.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-opal/latest/2019-02-13-88ecfe9d-53bf8430/
recipe: https://datasets.datalad.org/shub/motroy/singularity-opal/latest/2019-02-13-88ecfe9d-53bf8430/Singularity
collection: motroy/singularity-opal
---

# motroy/singularity-opal:latest

```bash
$ singularity pull shub://motroy/singularity-opal:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/Software/opal:$PATH"


%post
apt update && apt install -y git curl wget less locate unzip build-essential python2.7 python2.7-dev python-pip vowpal-wabbit
pip install pandas sklearn
mkdir -p /Software/ && cd /Software/
git clone https://github.com/yunwilliamyu/opal.git
export PATH="/Software/opal:$PATH"
cd opal
bash SETUP.sh
```

## Collection

 - Name: [motroy/singularity-opal](https://github.com/motroy/singularity-opal)
 - License: [MIT License](https://api.github.com/licenses/mit)

