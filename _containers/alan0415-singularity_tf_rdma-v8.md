---
id: 8687
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v8"
commit: "ccb0581034a3d4274d656da1adacc285eb5c94d6"
version: "2cea469bc69a978dcdfe565294b7d863"
build_date: "2019-04-27T17:36:59.320Z"
size_mb: 7278
size: 4491218975
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v8/2019-04-27-ccb05810-2cea469b/2cea469bc69a978dcdfe565294b7d863.simg"
url: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v8/2019-04-27-ccb05810-2cea469b/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v8/2019-04-27-ccb05810-2cea469b/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v8

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v8
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: alan0415/singularity_tf_rdma:v6

%post  
echo "This section happens once after bootstrap to build the image."
cd / && git clone https://github.com/tensorflow/benchmarks.git
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

