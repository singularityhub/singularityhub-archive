---
id: 1500
name: "wdconinc/pythiadire"
branch: "master"
tag: "latest"
commit: "626b65d45ddfd9ef66e6b9402f80b1839154d572"
version: "d128734a6d928696b2205f957cee4095"
build_date: "2018-01-29T21:32:16.172Z"
size_mb: 2101
size: 711475231
sif: "https://datasets.datalad.org/shub/wdconinc/pythiadire/latest/2018-01-29-626b65d4-d128734a/d128734a6d928696b2205f957cee4095.simg"
url: https://datasets.datalad.org/shub/wdconinc/pythiadire/latest/2018-01-29-626b65d4-d128734a/
recipe: https://datasets.datalad.org/shub/wdconinc/pythiadire/latest/2018-01-29-626b65d4-d128734a/Singularity
collection: wdconinc/pythiadire
---

# wdconinc/pythiadire:latest

```bash
$ singularity pull shub://wdconinc/pythiadire:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:nadinefischer/pythiadire:v1

%files

%labels

%environment

%runscript
exec echo "Try running with --app [rivet|dire|runOnCluster]"

%apprun runOnCluster
exec /usr/local/bin/runOnCluster "$@"

%apprun rivet
exec /usr/local/bin/rivet "$@"

%apprun dire
exec /usr/local/bin/dire "$@"

%post
```

## Collection

 - Name: [wdconinc/pythiadire](https://github.com/wdconinc/pythiadire)
 - License: None

