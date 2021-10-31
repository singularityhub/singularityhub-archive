---
id: 12756
name: "pab2163/voxel"
branch: "master"
tag: "latest"
commit: "1379122b82bd678bd4df9fd0239b7192510b8b69"
version: "8eb1dca9b9eb94c41bdc31298dee0c4f"
build_date: "2020-04-21T02:08:39.852Z"
size_mb: 862.0
size: 329687071
sif: "https://datasets.datalad.org/shub/pab2163/voxel/latest/2020-04-21-1379122b-8eb1dca9/8eb1dca9b9eb94c41bdc31298dee0c4f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pab2163/voxel/latest/2020-04-21-1379122b-8eb1dca9/
recipe: https://datasets.datalad.org/shub/pab2163/voxel/latest/2020-04-21-1379122b-8eb1dca9/Singularity
collection: pab2163/voxel
---

# pab2163/voxel:latest

```bash
$ singularity pull shub://pab2163/voxel:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest


# Installations
%post
apt-get update

apt-get install -y r-base-core
R --slave -e 'install.packages("voxel")'

# Test load package
%runscript
#!/bin/bash
Rscript --slave "test_load_voxel_package.R"
```

## Collection

 - Name: [pab2163/voxel](https://github.com/pab2163/voxel)
 - License: None

