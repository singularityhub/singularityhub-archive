---
id: 7154
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "vim"
commit: "c1f35eb8a2f97fb932f14f7dfc5cf420af5ce925"
version: "465fa292ebf92f651064f4b5f70278d0"
build_date: "2019-02-12T14:29:42.680Z"
size_mb: 415
size: 118980639
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/vim/2019-02-12-c1f35eb8-465fa292/465fa292ebf92f651064f4b5f70278d0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/vim/2019-02-12-c1f35eb8-465fa292/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/vim/2019-02-12-c1f35eb8-465fa292/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:vim

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:vim
```

## Singularity Recipe

```singularity
/home/pmitev/Singularity/vim/Singularity                                                                                                        149/149               100%
Bootstrap:  docker
From: thinca/vim:latest-full

%runscript
  vim $*

%setup

%files

%environment

%post
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

