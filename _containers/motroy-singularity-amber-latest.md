---
id: 7170
name: "motroy/singularity-amber"
branch: "master"
tag: "latest"
commit: "f556b2b91acf3e7233ee5414a15f2860b24c52ca"
version: "0c1629363bfd44376c498ed13a9d9f73"
build_date: "2019-09-11T01:28:23.371Z"
size_mb: 965
size: 405594143
sif: "https://datasets.datalad.org/shub/motroy/singularity-amber/latest/2019-09-11-f556b2b9-0c162936/0c1629363bfd44376c498ed13a9d9f73.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-amber/latest/2019-09-11-f556b2b9-0c162936/
recipe: https://datasets.datalad.org/shub/motroy/singularity-amber/latest/2019-09-11-f556b2b9-0c162936/Singularity
collection: motroy/singularity-amber
---

# motroy/singularity-amber:latest

```bash
$ singularity pull shub://motroy/singularity-amber:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:17.10

%environment
export PATH="${HOME}/.local/bin:$PATH"


%post
apt update && apt install -y git curl wget less locate unzip build-essential python3-pip
pip3 install cami-amber
export PATH="${HOME}/.local/bin:$PATH"
```

## Collection

 - Name: [motroy/singularity-amber](https://github.com/motroy/singularity-amber)
 - License: [MIT License](https://api.github.com/licenses/mit)

