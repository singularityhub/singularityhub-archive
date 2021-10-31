---
id: 15074
name: "jganong/ubuntu-focal-foiegras"
branch: "main"
tag: "latest"
commit: "825898b02838ef834be5c2d1469e0de4a3a9eb0b"
version: "4d85b3c3c70ce285ae350f33decc4ac2521798dc9f3fbc50e3f3f5861a2fdaaa"
build_date: "2020-12-08T16:45:03.189Z"
size_mb: 399.86328125
size: 419287040
sif: "https://datasets.datalad.org/shub/jganong/ubuntu-focal-foiegras/latest/2020-12-08-825898b0-4d85b3c3/4d85b3c3c70ce285ae350f33decc4ac2521798dc9f3fbc50e3f3f5861a2fdaaa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jganong/ubuntu-focal-foiegras/latest/2020-12-08-825898b0-4d85b3c3/
recipe: https://datasets.datalad.org/shub/jganong/ubuntu-focal-foiegras/latest/2020-12-08-825898b0-4d85b3c3/Singularity
collection: jganong/ubuntu-focal-foiegras
---

# jganong/ubuntu-focal-foiegras:latest

```bash
$ singularity pull shub://jganong/ubuntu-focal-foiegras:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:rocker/r-ubuntu:20.04

%labels
MAINTAINER jganong@stanford.edu

%environment
# without the TERM setting, it does not backspace, actually it does but does not show it which is worse!
export TERM=xterm-256color

%runscript
exec /usr/bin/R "$@"  

%post  
apt update
apt install -y r-cran-ncdf4
apt install -y r-cran-rgeos
apt install -y r-cran-foiegras
```

## Collection

 - Name: [jganong/ubuntu-focal-foiegras](https://github.com/jganong/ubuntu-focal-foiegras)
 - License: None

