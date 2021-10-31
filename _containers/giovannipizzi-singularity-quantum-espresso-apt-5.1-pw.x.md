---
id: 7665
name: "giovannipizzi/singularity-quantum-espresso"
branch: "master"
tag: "apt-5.1-pw.x"
commit: "80e71c78b50806f99f61a56cd67378838f7ecfac"
version: "3b346a367c45271bf810fb5253f1ce1f"
build_date: "2019-03-08T13:41:28.037Z"
size_mb: 296
size: 132423711
sif: "https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1-pw.x/2019-03-08-80e71c78-3b346a36/3b346a367c45271bf810fb5253f1ce1f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1-pw.x/2019-03-08-80e71c78-3b346a36/
recipe: https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/apt-5.1-pw.x/2019-03-08-80e71c78-3b346a36/Singularity
collection: giovannipizzi/singularity-quantum-espresso
---

# giovannipizzi/singularity-quantum-espresso:apt-5.1-pw.x

```bash
$ singularity pull shub://giovannipizzi/singularity-quantum-espresso:apt-5.1-pw.x
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install quantum-espresso
    apt-get -y clean

%environment
    export LC_ALL=en_US.UTF-8

%runscript
    pw.x
```

## Collection

 - Name: [giovannipizzi/singularity-quantum-espresso](https://github.com/giovannipizzi/singularity-quantum-espresso)
 - License: None

