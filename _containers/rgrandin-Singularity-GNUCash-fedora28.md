---
id: 4056
name: "rgrandin/Singularity-GNUCash"
branch: "master"
tag: "fedora28"
commit: "2712b0b93f7884ced9a57f48d9f7cb132d910d9f"
version: "f890b78753f287cb703a9f7a662c34df"
build_date: "2018-08-19T16:01:34.815Z"
size_mb: 969
size: 420634655
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/fedora28/2018-08-19-2712b0b9-f890b787/f890b78753f287cb703a9f7a662c34df.simg"
url: https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/fedora28/2018-08-19-2712b0b9-f890b787/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-GNUCash/fedora28/2018-08-19-2712b0b9-f890b787/Singularity
collection: rgrandin/Singularity-GNUCash
---

# rgrandin/Singularity-GNUCash:fedora28

```bash
$ singularity pull shub://rgrandin/Singularity-GNUCash:fedora28
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: fedora:28 


%runscript
    exec gnucash


%post
    dnf install -y gnucash
```

## Collection

 - Name: [rgrandin/Singularity-GNUCash](https://github.com/rgrandin/Singularity-GNUCash)
 - License: None

