---
id: 8017
name: "vahidmech/container_workshop"
branch: "master"
tag: "latest"
commit: "33dffde133a6561c2e418afa1ee250156423bfd1"
version: "57508d20e76f36ae3de8fef1d2266ee9"
build_date: "2019-03-29T01:29:26.338Z"
size_mb: 867
size: 334467103
sif: "https://datasets.datalad.org/shub/vahidmech/container_workshop/latest/2019-03-29-33dffde1-57508d20/57508d20e76f36ae3de8fef1d2266ee9.simg"
url: https://datasets.datalad.org/shub/vahidmech/container_workshop/latest/2019-03-29-33dffde1-57508d20/
recipe: https://datasets.datalad.org/shub/vahidmech/container_workshop/latest/2019-03-29-33dffde1-57508d20/Singularity
collection: vahidmech/container_workshop
---

# vahidmech/container_workshop:latest

```bash
$ singularity pull shub://vahidmech/container_workshop:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: makaho/hisat2-zstd

%labels
MAINTAINER rgrandin@iastate.edu
APPLICATION hisat2

%help
This container provides hisat2

%runscript
exec hisat2 "$@"
```

## Collection

 - Name: [vahidmech/container_workshop](https://github.com/vahidmech/container_workshop)
 - License: None

