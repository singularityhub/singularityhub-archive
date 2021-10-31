---
id: 15225
name: "klarman-cell-observatory/pegasus"
branch: "master"
tag: "latest"
commit: "ca5ef20996b9a6b0b623965e9c0f8da497573abc"
version: "d4aa0917f81ebed851a1250a56534232016596fc2f35467b2885a39a46ef7d40"
build_date: "2021-03-10T16:13:58.303Z"
size_mb: 2424.0703125
size: 2541821952
sif: "https://datasets.datalad.org/shub/klarman-cell-observatory/pegasus/latest/2021-03-10-ca5ef209-d4aa0917/d4aa0917f81ebed851a1250a56534232016596fc2f35467b2885a39a46ef7d40.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/klarman-cell-observatory/pegasus/latest/2021-03-10-ca5ef209-d4aa0917/
recipe: https://datasets.datalad.org/shub/klarman-cell-observatory/pegasus/latest/2021-03-10-ca5ef209-d4aa0917/Singularity
collection: klarman-cell-observatory/pegasus
---

# klarman-cell-observatory/pegasus:latest

```bash
$ singularity pull shub://klarman-cell-observatory/pegasus:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%post
    apt update
    apt install -y --no-install-recommends build-essential libfftw3-dev default-jdk python3 python3-pip python3-dev
    ln -s /usr/bin/python3 /usr/bin/python
    python -m pip install --upgrade pip
    python -m pip install pegasuspy
    python -m pip install fitsne leidenalg
```

## Collection

 - Name: [klarman-cell-observatory/pegasus](https://github.com/klarman-cell-observatory/pegasus)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

