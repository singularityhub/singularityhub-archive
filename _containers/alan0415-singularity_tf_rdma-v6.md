---
id: 8538
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v6"
commit: "1fc3260e2f661876aca99ba12afaa40532df97d9"
version: "7404e771ff3407d8f42d5671bf8cfdb4"
build_date: "2019-04-21T11:33:29.657Z"
size_mb: 7274
size: 4488638495
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v6/2019-04-21-1fc3260e-7404e771/7404e771ff3407d8f42d5671bf8cfdb4.simg"
url: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v6/2019-04-21-1fc3260e-7404e771/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v6/2019-04-21-1fc3260e-7404e771/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v6

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v6
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: bensonyang88/tensorflow-rdma:v6

%post  
echo "This section happens once after bootstrap to build the image."
mkdir /cifar-10-job
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

