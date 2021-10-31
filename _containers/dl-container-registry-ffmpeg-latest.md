---
id: 1525
name: "dl-container-registry/ffmpeg"
branch: "master"
tag: "latest"
commit: "9cf4277ca02528b3170dce9b71054650960ef021"
version: "857b30a29383dd5a585d437a07bdb3e1"
build_date: "2020-08-12T09:31:49.905Z"
size_mb: 968
size: 595161119
sif: "https://datasets.datalad.org/shub/dl-container-registry/ffmpeg/latest/2020-08-12-9cf4277c-857b30a2/857b30a29383dd5a585d437a07bdb3e1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dl-container-registry/ffmpeg/latest/2020-08-12-9cf4277c-857b30a2/
recipe: https://datasets.datalad.org/shub/dl-container-registry/ffmpeg/latest/2020-08-12-9cf4277c-857b30a2/Singularity
collection: dl-container-registry/ffmpeg
---

# dl-container-registry/ffmpeg:latest

```bash
$ singularity pull shub://dl-container-registry/ffmpeg:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: willprice/nvidia-ffmpeg:latest

%post
    ldconfig

%help
    Hardware Accelerated build of FFmpeg
```

## Collection

 - Name: [dl-container-registry/ffmpeg](https://github.com/dl-container-registry/ffmpeg)
 - License: None

