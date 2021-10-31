---
id: 9336
name: "elisadonnard/singularity"
branch: "master"
tag: "pypackages"
commit: "6b5ae5a17a33e9648474ec3a7a7daa7531d040d9"
version: "4d78d9fa40eb5dbe61aee336765d6c3c"
build_date: "2020-06-14T13:58:37.497Z"
size_mb: 3606
size: 1330061343
sif: "https://datasets.datalad.org/shub/elisadonnard/singularity/pypackages/2020-06-14-6b5ae5a1-4d78d9fa/4d78d9fa40eb5dbe61aee336765d6c3c.simg"
url: https://datasets.datalad.org/shub/elisadonnard/singularity/pypackages/2020-06-14-6b5ae5a1-4d78d9fa/
recipe: https://datasets.datalad.org/shub/elisadonnard/singularity/pypackages/2020-06-14-6b5ae5a1-4d78d9fa/Singularity
collection: elisadonnard/singularity
---

# elisadonnard/singularity:pypackages

```bash
$ singularity pull shub://elisadonnard/singularity:pypackages
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://elisadonnard/singularity:r3.5

%labels

    AUTHOR Elisa Donnard
    Version v4.0

%post
apt-get update && apt-get -y upgrade && apt-get -y install python3 && apt-get -y install python3-pip
pip3 install biopython numpy pandas PyBrain regex scipy
```

## Collection

 - Name: [elisadonnard/singularity](https://github.com/elisadonnard/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

