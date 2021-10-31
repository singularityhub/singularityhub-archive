---
id: 8688
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v9"
commit: "094bb7cd59e6c2c931b6c455116b45f212393e56"
version: "a1b14d1029dc890b194a995645adca11"
build_date: "2019-04-27T17:36:59.314Z"
size_mb: 7278
size: 4491178015
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v9/2019-04-27-094bb7cd-a1b14d10/a1b14d1029dc890b194a995645adca11.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/alan0415/singularity_tf_rdma/v9/2019-04-27-094bb7cd-a1b14d10/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v9/2019-04-27-094bb7cd-a1b14d10/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v9

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v9
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: alan0415/singularity_tf_rdma:v8

%post  
echo "This section happens once after bootstrap to build the image."

cd /benchmarks && git checkout cnn_tf_v1.12_compatible
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

