---
id: 9677
name: "sternacht/tf_singu"
branch: "master"
tag: "v9"
commit: "6c9970a0b0f40ae65f3fdede64034555f7fb80a7"
version: "f9926f764e91392ab95bc84d5a3fbed0"
build_date: "2019-06-10T14:59:15.434Z"
size_mb: 1098
size: 299765791
sif: "https://datasets.datalad.org/shub/sternacht/tf_singu/v9/2019-06-10-6c9970a0-f9926f76/f9926f764e91392ab95bc84d5a3fbed0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sternacht/tf_singu/v9/2019-06-10-6c9970a0-f9926f76/
recipe: https://datasets.datalad.org/shub/sternacht/tf_singu/v9/2019-06-10-6c9970a0-f9926f76/Singularity
collection: sternacht/tf_singu
---

# sternacht/tf_singu:v9

```bash
$ singularity pull shub://sternacht/tf_singu:v9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sternacht/hpcc_openblas:v4

RUN cp /home/hpcc-1.5.0/hpccinf.txt /*
```

## Collection

 - Name: [sternacht/tf_singu](https://github.com/sternacht/tf_singu)
 - License: None

