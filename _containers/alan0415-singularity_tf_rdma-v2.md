---
id: 8531
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v2"
commit: "3655f3de5c031bc17e49438dfbd1bf6d4e07de93"
version: "825cf468110b8c17f2da20f721cd968e"
build_date: "2019-04-21T09:06:21.121Z"
size_mb: 6626
size: 3921059871
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v2/2019-04-21-3655f3de-825cf468/825cf468110b8c17f2da20f721cd968e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alan0415/singularity_tf_rdma/v2/2019-04-21-3655f3de-825cf468/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v2/2019-04-21-3655f3de-825cf468/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v2

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v2
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: bensonyang88/tensorflow-rdma:v4

%post  
echo "This section happens once after bootstrap to build the image." 
cd /
mkdir tf_test
cd tf_test
git clone https://github.com/tensorflow/models.git
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

