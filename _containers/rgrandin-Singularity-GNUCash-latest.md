---
id: 4055
name: "rgrandin/Singularity-GNUCash"
branch: "master"
tag: "latest"
commit: "ae91a7920061e8a0d6a9a737672c3abb50606976"
version: "aa4f06f666f919aa59cc5941fa11a9fb"
build_date: "2019-12-30T03:29:38.419Z"
size_mb: 1014
size: 441098271
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/latest/2019-12-30-ae91a792-aa4f06f6/aa4f06f666f919aa59cc5941fa11a9fb.simg"
url: https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/latest/2019-12-30-ae91a792-aa4f06f6/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/latest/2019-12-30-ae91a792-aa4f06f6/Singularity
collection: rgrandin/Singularity-GNUCash
---

# rgrandin/Singularity-GNUCash:latest

```bash
$ singularity pull shub://rgrandin/Singularity-GNUCash:latest
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: fedora:latest


%runscript
    exec gnucash


%post
    dnf install -y gnucash
```

## Collection

 - Name: [rgrandin/Singularity-GNUCash](https://github.com/rgrandin/Singularity-GNUCash)
 - License: None

