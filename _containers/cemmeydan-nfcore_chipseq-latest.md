---
id: 9630
name: "cemmeydan/nfcore_chipseq"
branch: "master"
tag: "latest"
commit: "e22b4071197443232f771f82aaddab815f62b2b3"
version: "fd5bcbc9972fa9040e73bcf8c0607475"
build_date: "2019-06-07T11:19:42.491Z"
size_mb: 4103
size: 1343303711
sif: "https://datasets.datalad.org/shub/cemmeydan/nfcore_chipseq/latest/2019-06-07-e22b4071-fd5bcbc9/fd5bcbc9972fa9040e73bcf8c0607475.simg"
url: https://datasets.datalad.org/shub/cemmeydan/nfcore_chipseq/latest/2019-06-07-e22b4071-fd5bcbc9/
recipe: https://datasets.datalad.org/shub/cemmeydan/nfcore_chipseq/latest/2019-06-07-e22b4071-fd5bcbc9/Singularity
collection: cemmeydan/nfcore_chipseq
---

# cemmeydan/nfcore_chipseq:latest

```bash
$ singularity pull shub://cemmeydan/nfcore_chipseq:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: nfcore/chipseq:1.0.0

%setup

%environment

%files

%post
  mkdir -p /athena
  mkdir -p /scratchLocal
  mkdir /scratch
```

## Collection

 - Name: [cemmeydan/nfcore_chipseq](https://github.com/cemmeydan/nfcore_chipseq)
 - License: None

