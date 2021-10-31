---
id: 3874
name: "hpcdevops/tensorflow-gpu-nih"
branch: "master"
tag: "latest"
commit: "dde20e7febb7dcca39c96510db601af117d55451"
version: "4e013945f99196dfe5648feb4baaa462"
build_date: "2021-03-19T21:37:15.195Z"
size_mb: 3026
size: 1368989727
sif: "https://datasets.datalad.org/shub/hpcdevops/tensorflow-gpu-nih/latest/2021-03-19-dde20e7f-4e013945/4e013945f99196dfe5648feb4baaa462.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hpcdevops/tensorflow-gpu-nih/latest/2021-03-19-dde20e7f-4e013945/
recipe: https://datasets.datalad.org/shub/hpcdevops/tensorflow-gpu-nih/latest/2021-03-19-dde20e7f-4e013945/Singularity
collection: hpcdevops/tensorflow-gpu-nih
---

# hpcdevops/tensorflow-gpu-nih:latest

```bash
$ singularity pull shub://hpcdevops/tensorflow-gpu-nih:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: tensorflow/tensorflow:latest-devel-gpu

%labels
    MAINTAINER hpcdevops
    WHATAMI tensorflow-gpu

%files
    hello.tensorflow.py /hello.tensorflow.py

%runscript
    exec /usr/bin/python "$@"

%post

    # create bind points for SDSC HPC environment
    mkdir /oasis /projects /scratch

    # build info
    echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [hpcdevops/tensorflow-gpu-nih](https://github.com/hpcdevops/tensorflow-gpu-nih)
 - License: [Other](None)

