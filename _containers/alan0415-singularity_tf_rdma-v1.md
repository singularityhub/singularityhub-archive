---
id: 8514
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v1"
commit: "f832d3f016a5c0437df5e3f74624965f95bc8ad2"
version: "00cdb46e005ad0e49af8e7f9746527b0"
build_date: "2019-04-20T16:49:54.126Z"
size_mb: 5620
size: 3002060831
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v1/2019-04-20-f832d3f0-00cdb46e/00cdb46e005ad0e49af8e7f9746527b0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alan0415/singularity_tf_rdma/v1/2019-04-20-f832d3f0-00cdb46e/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v1/2019-04-20-f832d3f0-00cdb46e/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v1

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v1
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: bensonyang88/tensorflow-rdma:v4

%post  
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

