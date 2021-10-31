---
id: 2937
name: "JeffersonLab/remoll"
branch: "master"
tag: "develop"
commit: "5006e7752fab3800f0b372ec690078973507b5d1"
version: "467452ad78dd4a1057d9c80292efa768"
build_date: "2018-11-17T04:47:28.899Z"
size_mb: 9196
size: 6808403999
sif: "https://datasets.datalad.org/shub/JeffersonLab/remoll/develop/2018-11-17-5006e775-467452ad/467452ad78dd4a1057d9c80292efa768.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JeffersonLab/remoll/develop/2018-11-17-5006e775-467452ad/
recipe: https://datasets.datalad.org/shub/JeffersonLab/remoll/develop/2018-11-17-5006e775-467452ad/Singularity
collection: JeffersonLab/remoll
---

# JeffersonLab/remoll:develop

```bash
$ singularity pull shub://JeffersonLab/remoll:develop
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

