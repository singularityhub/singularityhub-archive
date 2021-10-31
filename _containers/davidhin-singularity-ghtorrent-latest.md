---
id: 15666
name: "davidhin/singularity-ghtorrent"
branch: "master"
tag: "latest"
commit: "2c4633992c564e232f86cbe6715397e5ca9d2667"
version: "e0ef15831d16dce142b7a04ca339a89e"
build_date: "2021-03-12T00:27:49.875Z"
size_mb: 837.0
size: 324821023
sif: "https://datasets.datalad.org/shub/davidhin/singularity-ghtorrent/latest/2021-03-12-2c463399-e0ef1583/e0ef15831d16dce142b7a04ca339a89e.sif"
url: https://datasets.datalad.org/shub/davidhin/singularity-ghtorrent/latest/2021-03-12-2c463399-e0ef1583/
recipe: https://datasets.datalad.org/shub/davidhin/singularity-ghtorrent/latest/2021-03-12-2c463399-e0ef1583/Singularity
collection: davidhin/singularity-ghtorrent
---

# davidhin/singularity-ghtorrent:latest

```bash
$ singularity pull shub://davidhin/singularity-ghtorrent:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:python:3.8-slim

%labels
    MAINTAINER admin
    WHATAMI admin

%files
    cli.sh /cli.sh
    requirements.txt /requirements.txt

%runscript
    exec /bin/bash /cli.sh "$@"

%post
    chmod u+x /cli.sh

    # Install dependencies here
    apt update
    apt install -y build-essential
    pip install -r /requirements.txt
```

## Collection

 - Name: [davidhin/singularity-ghtorrent](https://github.com/davidhin/singularity-ghtorrent)
 - License: None

