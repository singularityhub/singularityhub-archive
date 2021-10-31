---
id: 1061
name: "TormodLandet/singularity-fenics-dev-env"
branch: "master"
tag: "latest"
commit: "c18681b96483f4a0e6d16048d6688e3e3ba08eac"
version: "74cf75aece58e781602b47d8c7c85a34"
build_date: "2020-03-13T18:26:14.911Z"
size_mb: 2107
size: 678461471
sif: "https://datasets.datalad.org/shub/TormodLandet/singularity-fenics-dev-env/latest/2020-03-13-c18681b9-74cf75ae/74cf75aece58e781602b47d8c7c85a34.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TormodLandet/singularity-fenics-dev-env/latest/2020-03-13-c18681b9-74cf75ae/
recipe: https://datasets.datalad.org/shub/TormodLandet/singularity-fenics-dev-env/latest/2020-03-13-c18681b9-74cf75ae/Singularity
collection: TormodLandet/singularity-fenics-dev-env
---

# TormodLandet/singularity-fenics-dev-env:latest

```bash
$ singularity pull shub://TormodLandet/singularity-fenics-dev-env:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: trlandet/fenics-dev:latest

%post
    cp /home/fenics/bin/fenics-* /usr/local/bin

%runscript
    echo "Welcome to the Singularity FEniCS dev-env container"
    exec /bin/bash -i "$@"
```

## Collection

 - Name: [TormodLandet/singularity-fenics-dev-env](https://github.com/TormodLandet/singularity-fenics-dev-env)
 - License: None

