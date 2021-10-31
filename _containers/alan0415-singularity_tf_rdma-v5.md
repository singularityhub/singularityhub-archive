---
id: 8536
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v5"
commit: "98cb66a8ce4edfa57a872100030f7cdfd1115663"
version: "5da89b0e4ceabe83bd5475bc43cfdf27"
build_date: "2019-04-21T11:33:29.663Z"
size_mb: 7273
size: 4488638495
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v5/2019-04-21-98cb66a8-5da89b0e/5da89b0e4ceabe83bd5475bc43cfdf27.simg"
url: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v5/2019-04-21-98cb66a8-5da89b0e/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v5/2019-04-21-98cb66a8-5da89b0e/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v5

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v5
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: bensonyang88/tensorflow-rdma:v6

%post  
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

