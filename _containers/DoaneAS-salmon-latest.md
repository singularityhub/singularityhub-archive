---
id: 3337
name: "DoaneAS/salmon"
branch: "master"
tag: "latest"
commit: "d0e1e05fc29180e96cf526ddfa91dfc1da44d3e9"
version: "02bbe2949114779f085ec0df351fbc71"
build_date: "2018-08-15T09:33:42.192Z"
size_mb: 1176
size: 350208031
sif: "https://datasets.datalad.org/shub/DoaneAS/salmon/latest/2018-08-15-d0e1e05f-02bbe294/02bbe2949114779f085ec0df351fbc71.simg"
url: https://datasets.datalad.org/shub/DoaneAS/salmon/latest/2018-08-15-d0e1e05f-02bbe294/
recipe: https://datasets.datalad.org/shub/DoaneAS/salmon/latest/2018-08-15-d0e1e05f-02bbe294/Singularity
collection: DoaneAS/salmon
---

# DoaneAS/salmon:latest

```bash
$ singularity pull shub://DoaneAS/salmon:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: combinelab/salmon:latest

%post
    mkdir -p /athena
    mkdir -p /scratchLocal
    echo "All Set!"
```

## Collection

 - Name: [DoaneAS/salmon](https://github.com/DoaneAS/salmon)
 - License: None

