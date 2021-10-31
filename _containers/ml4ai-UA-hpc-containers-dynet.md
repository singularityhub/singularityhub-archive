---
id: 6654
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "dynet"
commit: "c0e569627dde1422aabf9c09fcc8d2bd9b4dbd61"
version: "2757b160ab03f3d8b251d180299eb1f4"
build_date: "2019-01-28T22:35:35.921Z"
size_mb: 3644
size: 1771855903
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/dynet/2019-01-28-c0e56962-2757b160/2757b160ab03f3d8b251d180299eb1f4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/dynet/2019-01-28-c0e56962-2757b160/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/dynet/2019-01-28-c0e56962-2757b160/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:dynet

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:dynet
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: spellrun/dynet

%post
   # in-container bind points for shared filesystems
   mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
   pip install tqdm
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

