---
id: 4192
name: "khanlab/template-circleci"
branch: "master"
tag: "latest"
commit: "0503649c77a1d667ff5b94c2a196b3ca7a7c92fb"
version: "4a332ac3f179e3b3681c9e46f0a6cd4e"
build_date: "2019-01-11T15:17:03.912Z"
size_mb: 5
size: 2043935
sif: "https://datasets.datalad.org/shub/khanlab/template-circleci/latest/2019-01-11-0503649c-4a332ac3/4a332ac3f179e3b3681c9e46f0a6cd4e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/template-circleci/latest/2019-01-11-0503649c-4a332ac3/
recipe: https://datasets.datalad.org/shub/khanlab/template-circleci/latest/2019-01-11-0503649c-4a332ac3/Singularity
collection: khanlab/template-circleci
---

# khanlab/template-circleci:latest

```bash
$ singularity pull shub://khanlab/template-circleci:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: khanlab/template-circleci:latest
%labels
CIRCLE_BUILD_URL https://circleci.com/gh/khanlab/template-circleci/251
```

## Collection

 - Name: [khanlab/template-circleci](https://github.com/khanlab/template-circleci)
 - License: None

