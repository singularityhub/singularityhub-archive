---
id: 5621
name: "patrickvdb/knn_smoothing"
branch: "master"
tag: "v2.1"
commit: "573616ed1c8b38274a9ed0ba37f10c23eb343ec3"
version: "579eb5e73e9e970721fb427fd75394a1"
build_date: "2018-11-16T13:28:05.928Z"
size_mb: 1587
size: 606216223
sif: "https://datasets.datalad.org/shub/patrickvdb/knn_smoothing/v2.1/2018-11-16-573616ed-579eb5e7/579eb5e73e9e970721fb427fd75394a1.simg"
url: https://datasets.datalad.org/shub/patrickvdb/knn_smoothing/v2.1/2018-11-16-573616ed-579eb5e7/
recipe: https://datasets.datalad.org/shub/patrickvdb/knn_smoothing/v2.1/2018-11-16-573616ed-579eb5e7/Singularity
collection: patrickvdb/knn_smoothing
---

# patrickvdb/knn_smoothing:v2.1

```bash
$ singularity pull shub://patrickvdb/knn_smoothing:v2.1
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/knn_smoothing:v2.1


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/knn_smoothing](https://github.com/patrickvdb/knn_smoothing)
 - License: None

