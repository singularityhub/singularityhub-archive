---
id: 8038
name: "rgrandin/Singularity-GNUCash"
branch: "master"
tag: "fedora29"
commit: "77975cca220579c60d319f5e2c4d6c75c8ba3945"
version: "20f5397f0f64da521f8ab32a936b51bf"
build_date: "2019-03-31T19:21:50.066Z"
size_mb: 1014
size: 441098271
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/fedora29/2019-03-31-77975cca-20f5397f/20f5397f0f64da521f8ab32a936b51bf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rgrandin/Singularity-GNUCash/fedora29/2019-03-31-77975cca-20f5397f/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/fedora29/2019-03-31-77975cca-20f5397f/Singularity
collection: rgrandin/Singularity-GNUCash
---

# rgrandin/Singularity-GNUCash:fedora29

```bash
$ singularity pull shub://rgrandin/Singularity-GNUCash:fedora29
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: fedora:29 


%runscript
    exec gnucash


%post
    dnf install -y gnucash
```

## Collection

 - Name: [rgrandin/Singularity-GNUCash](https://github.com/rgrandin/Singularity-GNUCash)
 - License: None

