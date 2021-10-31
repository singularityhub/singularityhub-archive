---
id: 8540
name: "sternacht/tf_singu"
branch: "master"
tag: "v3"
commit: "91decb21eee5fdeb48d02165bacbca4dc11098df"
version: "a159651a2690f09c1d96cf6b53c72202"
build_date: "2019-04-21T16:47:20.643Z"
size_mb: 7273
size: 4488642591
sif: "https://datasets.datalad.org/shub/sternacht/tf_singu/v3/2019-04-21-91decb21-a159651a/a159651a2690f09c1d96cf6b53c72202.simg"
url: https://datasets.datalad.org/shub/sternacht/tf_singu/v3/2019-04-21-91decb21-a159651a/
recipe: https://datasets.datalad.org/shub/sternacht/tf_singu/v3/2019-04-21-91decb21-a159651a/Singularity
collection: sternacht/tf_singu
---

# sternacht/tf_singu:v3

```bash
$ singularity pull shub://sternacht/tf_singu:v3
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: bensonyang88/tensorflow-rdma:v6

%post  
echo "This section happens once after bootstrap to build the image." 

#set enviroment
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

## Collection

 - Name: [sternacht/tf_singu](https://github.com/sternacht/tf_singu)
 - License: None

