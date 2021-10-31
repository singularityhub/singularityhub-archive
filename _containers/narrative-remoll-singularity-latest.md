---
id: 517
name: "narrative/remoll-singularity"
branch: "master"
tag: "latest"
commit: "582992a34d9b67acf744daee24fc5ce04dfa3319"
version: "98c5b28069fc9873705954da8eef2212"
build_date: "2017-10-27T19:22:10.310Z"
size_mb: 4431
size: 2015674399
sif: "https://datasets.datalad.org/shub/narrative/remoll-singularity/latest/2017-10-27-582992a3-98c5b280/98c5b28069fc9873705954da8eef2212.simg"
url: https://datasets.datalad.org/shub/narrative/remoll-singularity/latest/2017-10-27-582992a3-98c5b280/
recipe: https://datasets.datalad.org/shub/narrative/remoll-singularity/latest/2017-10-27-582992a3-98c5b280/Singularity
collection: narrative/remoll-singularity
---

# narrative/remoll-singularity:latest

```bash
$ singularity pull shub://narrative/remoll-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:jeffersonlab/remoll:latest 

%files

%labels
MAINTAINER Erik Stevenson

%environment

%runscript
exec /entrypoint.sh "$@"

%post
```

## Collection

 - Name: [narrative/remoll-singularity](https://github.com/narrative/remoll-singularity)
 - License: None

