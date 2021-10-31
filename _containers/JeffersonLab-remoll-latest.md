---
id: 899
name: "JeffersonLab/remoll"
branch: "develop"
tag: "latest"
commit: "9bc14746cf80abbc064537981f250fd86d906206"
version: "f31a1dfbcd07a1057e93bbfa0e23d9a3"
build_date: "2020-05-28T20:33:16.356Z"
size_mb: 4568
size: 2139840543
sif: "https://datasets.datalad.org/shub/JeffersonLab/remoll/latest/2020-05-28-9bc14746-f31a1dfb/f31a1dfbcd07a1057e93bbfa0e23d9a3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JeffersonLab/remoll/latest/2020-05-28-9bc14746-f31a1dfb/
recipe: https://datasets.datalad.org/shub/JeffersonLab/remoll/latest/2020-05-28-9bc14746-f31a1dfb/Singularity
collection: JeffersonLab/remoll
---

# JeffersonLab/remoll:latest

```bash
$ singularity pull shub://JeffersonLab/remoll:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:jeffersonlab/remoll:develop

%files

%labels
MAINTAINER Erik Stevenson

%environment

%runscript
exec /entrypoint.sh "$@"

%post
```

## Collection

 - Name: [JeffersonLab/remoll](https://github.com/JeffersonLab/remoll)
 - License: None

