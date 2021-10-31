---
id: 9443
name: "abdm/Singularity-test2"
branch: "master"
tag: "latest"
commit: "56df0bbca8d0b0add57a4b8f1caf4129338287a7"
version: "755e67630fd2d3a136a1d0aa9a17eb8d"
build_date: "2019-05-31T19:07:36.032Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/abdm/Singularity-test2/latest/2019-05-31-56df0bbc-755e6763/755e67630fd2d3a136a1d0aa9a17eb8d.simg"
url: https://datasets.datalad.org/shub/abdm/Singularity-test2/latest/2019-05-31-56df0bbc-755e6763/
recipe: https://datasets.datalad.org/shub/abdm/Singularity-test2/latest/2019-05-31-56df0bbc-755e6763/Singularity
collection: abdm/Singularity-test2
---

# abdm/Singularity-test2:latest

```bash
$ singularity pull shub://abdm/Singularity-test2:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu

%runscript
    exec echo "This is a test only"

%files

%environment
    VARIABLE=MEATBALLVALUE
    export VARIABLE

%labels
   AUTHOR vsochat@stanford.edu

%post
echo "The post section is where you can install, and configure your container."
```

## Collection

 - Name: [abdm/Singularity-test2](https://github.com/abdm/Singularity-test2)
 - License: None

