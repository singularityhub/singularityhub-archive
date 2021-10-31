---
id: 15545
name: "savvas-paragkamian/deco"
branch: "master"
tag: "latest"
commit: "6f2e49b8b8ccd3647cd079ff4616c5f345098f17"
version: "67c8cf2913eb9b4389ce31ce3542bf38"
build_date: "2021-04-02T22:12:28.216Z"
size_mb: 3046.0
size: 1005510687
sif: "https://datasets.datalad.org/shub/savvas-paragkamian/deco/latest/2021-04-02-6f2e49b8-67c8cf29/67c8cf2913eb9b4389ce31ce3542bf38.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/savvas-paragkamian/deco/latest/2021-04-02-6f2e49b8-67c8cf29/
recipe: https://datasets.datalad.org/shub/savvas-paragkamian/deco/latest/2021-04-02-6f2e49b8-67c8cf29/Singularity
collection: savvas-paragkamian/deco
---

# savvas-paragkamian/deco:latest

```bash
$ singularity pull shub://savvas-paragkamian/deco:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:savvasparagkamian/deco:latest

%labels
    Maintainer Savvas Paragkamian
%post
    export WORKDIR="/home/deco"
    echo "export WORKDIR=$WORKDIR" >> $SINGULARITY_ENVIRONMENT
    chmod -R 777 /home/deco

%runscript
    echo "Arguments received: $*"
    exec ./home/deco/scripts/cli-workflow.sh "$@"
```

## Collection

 - Name: [savvas-paragkamian/deco](https://github.com/savvas-paragkamian/deco)
 - License: [Other](None)

