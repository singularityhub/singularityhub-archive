---
id: 15600
name: "davidhin/singularity-example"
branch: "main"
tag: "latest"
commit: "93457c891707952e396a817d214722a142fb53d1"
version: "fa23b6d6979b3d66fbb216f13cb330a3"
build_date: "2021-03-15T01:16:10.326Z"
size_mb: 7981.0
size: 4532129823
sif: "https://datasets.datalad.org/shub/davidhin/singularity-example/latest/2021-03-15-93457c89-fa23b6d6/fa23b6d6979b3d66fbb216f13cb330a3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/davidhin/singularity-example/latest/2021-03-15-93457c89-fa23b6d6/
recipe: https://datasets.datalad.org/shub/davidhin/singularity-example/latest/2021-03-15-93457c89-fa23b6d6/Singularity
collection: davidhin/singularity-example
---

# davidhin/singularity-example:latest

```bash
$ singularity pull shub://davidhin/singularity-example:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ufoym/deepo:pytorch-cu102

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

 - Name: [davidhin/singularity-example](https://github.com/davidhin/singularity-example)
 - License: None

