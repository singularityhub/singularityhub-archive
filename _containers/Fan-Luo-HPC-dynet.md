---
id: 5824
name: "Fan-Luo/HPC"
branch: "master"
tag: "dynet"
commit: "488bf153cba48f36b101c54170bf37a8f088bf80"
version: "3197a6992b1a8315db21d20dc1a3ef1b"
build_date: "2018-12-09T13:14:44.264Z"
size_mb: 3643
size: 1770967071
sif: "https://datasets.datalad.org/shub/Fan-Luo/HPC/dynet/2018-12-09-488bf153-3197a699/3197a6992b1a8315db21d20dc1a3ef1b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Fan-Luo/HPC/dynet/2018-12-09-488bf153-3197a699/
recipe: https://datasets.datalad.org/shub/Fan-Luo/HPC/dynet/2018-12-09-488bf153-3197a699/Singularity
collection: Fan-Luo/HPC
---

# Fan-Luo/HPC:dynet

```bash
$ singularity pull shub://Fan-Luo/HPC:dynet
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

 - Name: [Fan-Luo/HPC](https://github.com/Fan-Luo/HPC)
 - License: None

