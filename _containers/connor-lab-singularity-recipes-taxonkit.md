---
id: 7003
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "taxonkit"
commit: "59274c17feebde4d6f578522e21ef0f8db8bc800"
version: "ef3a87ee373ed05e56e1198ffbf64dd4"
build_date: "2019-02-07T19:57:01.361Z"
size_mb: 395
size: 69005343
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/taxonkit/2019-02-07-59274c17-ef3a87ee/ef3a87ee373ed05e56e1198ffbf64dd4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/taxonkit/2019-02-07-59274c17-ef3a87ee/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/taxonkit/2019-02-07-59274c17-ef3a87ee/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:taxonkit

```bash
$ singularity pull shub://connor-lab/singularity-recipes:taxonkit
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add bash bzip2-dev curl git ncurses-dev xz-dev zlib-dev
    apk add python3

    curl -fsSL ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz | tar -xz names.dmp nodes.dmp
   
    mkdir -p /opt/taxonkit

    mv *.dmp /opt/taxonkit  

    curl -fsSL 'https://github.com/shenwei356/taxonkit/releases/download/v0.3.0/taxonkit_linux_amd64.tar.gz' | tar -xz -C /usr/local/bin/

    git clone https://github.com/connor-lab/centrifuge-summary
    cd centrifuge-summary
    mv centrifuge-summary /usr/local/bin/

%environment
    export TAXONKIT_DB=/opt/taxonkit

%labels
    Maintainer m-bull
    Version taxonkit-0.3.0
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

