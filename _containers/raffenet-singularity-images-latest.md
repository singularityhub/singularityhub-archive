---
id: 14050
name: "raffenet/singularity-images"
branch: "master"
tag: "latest"
commit: "ae4372b24a10a18237456b8a287ad34bec999faa"
version: "11fa9c087507e5ffd57ecc0617039874"
build_date: "2020-08-24T20:49:44.442Z"
size_mb: 395.0
size: 142282783
sif: "https://datasets.datalad.org/shub/raffenet/singularity-images/latest/2020-08-24-ae4372b2-11fa9c08/11fa9c087507e5ffd57ecc0617039874.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/raffenet/singularity-images/latest/2020-08-24-ae4372b2-11fa9c08/
recipe: https://datasets.datalad.org/shub/raffenet/singularity-images/latest/2020-08-24-ae4372b2-11fa9c08/Singularity
collection: raffenet/singularity-images
---

# raffenet/singularity-images:latest

```bash
$ singularity pull shub://raffenet/singularity-images:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:7

%labels
MAINTAINER raffenet

%post
echo "This section happens once after bootstrap to build the image."
yum -y install mpich-devel
```

## Collection

 - Name: [raffenet/singularity-images](https://github.com/raffenet/singularity-images)
 - License: None

