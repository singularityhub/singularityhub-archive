---
id: 2744
name: "ISU-HPC/plasflow"
branch: "master"
tag: "latest"
commit: "bcf9b8991b3098a410937531b7c7f1fd232b135d"
version: "95c620ceae632ce2094deff5f3d74ec0"
build_date: "2018-05-10T14:15:21.691Z"
size_mb: 2409
size: 802148383
sif: "https://datasets.datalad.org/shub/ISU-HPC/plasflow/latest/2018-05-10-bcf9b899-95c620ce/95c620ceae632ce2094deff5f3d74ec0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/plasflow/latest/2018-05-10-bcf9b899-95c620ce/
recipe: https://datasets.datalad.org/shub/ISU-HPC/plasflow/latest/2018-05-10-bcf9b899-95c620ce/Singularity
collection: ISU-HPC/plasflow
---

# ISU-HPC/plasflow:latest

```bash
$ singularity pull shub://ISU-HPC/plasflow:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
FROM: bioconductor/release_core2

%labels
AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%post
apt install -y python3-pip libreadline-dev libpcre3 libpcre3-dev lzma lzma-dev liblzma-dev bzip2 libbz2-dev
pip3 install --no-cache-dir https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0rc0-cp35-cp35m-linux_x86_64.whl
pip3 install --no-cache-dir plasFlow
pip3 install --no-cache-dir biopython
# Setting required library paths
echo 'export LD_LIBRARY_PATH=/usr/local/lib/R/lib' >>$SINGULARITY_ENVIRONMENT
echo 'export TMPDIR=/local/scratch' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ISU-HPC/plasflow](https://github.com/ISU-HPC/plasflow)
 - License: None

