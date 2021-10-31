---
id: 1539
name: "dl-container-registry/opencv2"
branch: "master"
tag: "latest"
commit: "59991ca40ea1f276044c81cf3c39955a99b4145e"
version: "b613eea163d23d5bea48742072b96ec0"
build_date: "2020-10-15T15:19:16.898Z"
size_mb: 5972
size: 2097414175
sif: "https://datasets.datalad.org/shub/dl-container-registry/opencv2/latest/2020-10-15-59991ca4-b613eea1/b613eea163d23d5bea48742072b96ec0.simg"
url: https://datasets.datalad.org/shub/dl-container-registry/opencv2/latest/2020-10-15-59991ca4-b613eea1/
recipe: https://datasets.datalad.org/shub/dl-container-registry/opencv2/latest/2020-10-15-59991ca4-b613eea1/Singularity
collection: dl-container-registry/opencv2
---

# dl-container-registry/opencv2:latest

```bash
$ singularity pull shub://dl-container-registry/opencv2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: willprice/opencv2-cuda8:latest

%post
    ldconfig

%help
    Hardware Accelerated build of FFmpeg
```

## Collection

 - Name: [dl-container-registry/opencv2](https://github.com/dl-container-registry/opencv2)
 - License: None

