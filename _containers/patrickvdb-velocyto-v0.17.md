---
id: 5588
name: "patrickvdb/velocyto"
branch: "master"
tag: "v0.17"
commit: "7f039a83e00dec28fca7d112335051cf06d75a39"
version: "497e7121060b845c6eec753284352540"
build_date: "2020-03-02T13:27:13.152Z"
size_mb: 4533
size: 1953026079
sif: "https://datasets.datalad.org/shub/patrickvdb/velocyto/v0.17/2020-03-02-7f039a83-497e7121/497e7121060b845c6eec753284352540.simg"
url: https://datasets.datalad.org/shub/patrickvdb/velocyto/v0.17/2020-03-02-7f039a83-497e7121/
recipe: https://datasets.datalad.org/shub/patrickvdb/velocyto/v0.17/2020-03-02-7f039a83-497e7121/Singularity
collection: patrickvdb/velocyto
---

# patrickvdb/velocyto:v0.17

```bash
$ singularity pull shub://patrickvdb/velocyto:v0.17
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/velocyto:v0.17



%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/velocyto](https://github.com/patrickvdb/velocyto)
 - License: None

