---
id: 7155
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "mc"
commit: "c1f35eb8a2f97fb932f14f7dfc5cf420af5ce925"
version: "05d8a444d6b263121096a827928a8545"
build_date: "2019-02-12T14:29:42.674Z"
size_mb: 48
size: 14151711
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/mc/2019-02-12-c1f35eb8-05d8a444/05d8a444d6b263121096a827928a8545.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/mc/2019-02-12-c1f35eb8-05d8a444/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/mc/2019-02-12-c1f35eb8-05d8a444/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:mc

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:mc
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: alpine

%runscript
  /usr/bin/mc

%setup

%files

%environment

%labels

%post
  apk add --no-cache mc vim
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

