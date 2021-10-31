---
id: 2701
name: "DoaneAS/crispr-mageck-nf"
branch: "master"
tag: "latest"
commit: "0f4b0324c107243e64eb8b43d0b14572d3cc074a"
version: "a01a46e7f529b6816a8e7432e2bb65af"
build_date: "2018-05-03T16:27:47.519Z"
size_mb: 2649
size: 958697503
sif: "https://datasets.datalad.org/shub/DoaneAS/crispr-mageck-nf/latest/2018-05-03-0f4b0324-a01a46e7/a01a46e7f529b6816a8e7432e2bb65af.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DoaneAS/crispr-mageck-nf/latest/2018-05-03-0f4b0324-a01a46e7/
recipe: https://datasets.datalad.org/shub/DoaneAS/crispr-mageck-nf/latest/2018-05-03-0f4b0324-a01a46e7/Singularity
collection: DoaneAS/crispr-mageck-nf
---

# DoaneAS/crispr-mageck-nf:latest

```bash
$ singularity pull shub://DoaneAS/crispr-mageck-nf:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: zuberlab/crispr-nf:latest

%post
    mkdir /athena
    mkdir /scratchLocal
```

## Collection

 - Name: [DoaneAS/crispr-mageck-nf](https://github.com/DoaneAS/crispr-mageck-nf)
 - License: [MIT License](https://api.github.com/licenses/mit)

