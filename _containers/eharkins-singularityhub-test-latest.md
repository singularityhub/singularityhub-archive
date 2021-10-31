---
id: 6573
name: "eharkins/singularityhub-test"
branch: "master"
tag: "latest"
commit: "ef6f31fa80fe339a06e8f96f1dc8ce96c9b7e240"
version: "dd99e54d3acb90accf4fe52590b23c85"
build_date: "2019-01-25T08:49:38.047Z"
size_mb: 205
size: 81514527
sif: "https://datasets.datalad.org/shub/eharkins/singularityhub-test/latest/2019-01-25-ef6f31fa-dd99e54d/dd99e54d3acb90accf4fe52590b23c85.simg"
url: https://datasets.datalad.org/shub/eharkins/singularityhub-test/latest/2019-01-25-ef6f31fa-dd99e54d/
recipe: https://datasets.datalad.org/shub/eharkins/singularityhub-test/latest/2019-01-25-ef6f31fa-dd99e54d/Singularity
collection: eharkins/singularityhub-test
---

# eharkins/singularityhub-test:latest

```bash
$ singularity pull shub://eharkins/singularityhub-test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:16.04


%post

    apt-get -y update

    apt-get -y install fortune cowsay lolcat


%environment

    export LC_ALL=C

    export PATH=/usr/games:$PATH


%runscript

    fortune | cowsay | lolcat
```

## Collection

 - Name: [eharkins/singularityhub-test](https://github.com/eharkins/singularityhub-test)
 - License: None

