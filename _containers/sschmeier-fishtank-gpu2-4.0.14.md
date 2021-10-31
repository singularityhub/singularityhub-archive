---
id: 15576
name: "sschmeier/fishtank-gpu2"
branch: "master"
tag: "4.0.14"
commit: "69334da5453141cd101c33328a649c581bc4c4ce"
version: "97b0f48eb2c2c031123e312cebbcf1a8f2a38e15ea117b8848d0506ec739482c"
build_date: "2021-02-23T07:06:52.287Z"
size_mb: 1971.25390625
size: 2067009536
sif: "https://datasets.datalad.org/shub/sschmeier/fishtank-gpu2/4.0.14/2021-02-23-69334da5-97b0f48e/97b0f48eb2c2c031123e312cebbcf1a8f2a38e15ea117b8848d0506ec739482c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/fishtank-gpu2/4.0.14/2021-02-23-69334da5-97b0f48e/
recipe: https://datasets.datalad.org/shub/sschmeier/fishtank-gpu2/4.0.14/2021-02-23-69334da5-97b0f48e/Singularity
collection: sschmeier/fishtank-gpu2
---

# sschmeier/fishtank-gpu2:4.0.14

```bash
$ singularity pull shub://sschmeier/fishtank-gpu2:4.0.14
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: genomicpariscentre/guppy-gpu:4.0.14


%post
  touch /`date -u -Iseconds`~
```

## Collection

 - Name: [sschmeier/fishtank-gpu2](https://github.com/sschmeier/fishtank-gpu2)
 - License: None

