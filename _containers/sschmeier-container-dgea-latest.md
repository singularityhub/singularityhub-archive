---
id: 11387
name: "sschmeier/container-dgea"
branch: "master"
tag: "latest"
commit: "491d20ecd9dc6c6ee360494d0a376807a1fd6d6c"
version: "5a9df8f5f7598e9f9c0751e74d477c367a40775eb158c4e53e22ec1fb2f3664e"
build_date: "2020-11-23T08:40:14.052Z"
size_mb: 582.92578125
size: 611241984
sif: "https://datasets.datalad.org/shub/sschmeier/container-dgea/latest/2020-11-23-491d20ec-5a9df8f5/5a9df8f5f7598e9f9c0751e74d477c367a40775eb158c4e53e22ec1fb2f3664e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/container-dgea/latest/2020-11-23-491d20ec-5a9df8f5/
recipe: https://datasets.datalad.org/shub/sschmeier/container-dgea/latest/2020-11-23-491d20ec-5a9df8f5/Singularity
collection: sschmeier/container-dgea
---

# sschmeier/container-dgea:latest

```bash
$ singularity pull shub://sschmeier/container-dgea:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sebio/dgea

%labels
   AUTHOR s.schmeier@protonmail.com

%post
  touch /`date -u -Iseconds`
```

## Collection

 - Name: [sschmeier/container-dgea](https://github.com/sschmeier/container-dgea)
 - License: None

