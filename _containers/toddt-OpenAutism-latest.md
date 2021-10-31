---
id: 3989
name: "toddt/OpenAutism"
branch: "master"
tag: "latest"
commit: "2c79a15071b6ca45fcfb0824bd2baf2fea044cd3"
version: "b6d8abbaa56f5639fbd4b87c0166c20f"
build_date: "2018-08-15T09:33:42.914Z"
size_mb: 2588
size: 983277599
sif: "https://datasets.datalad.org/shub/toddt/OpenAutism/latest/2018-08-15-2c79a150-b6d8abba/b6d8abbaa56f5639fbd4b87c0166c20f.simg"
url: https://datasets.datalad.org/shub/toddt/OpenAutism/latest/2018-08-15-2c79a150-b6d8abba/
recipe: https://datasets.datalad.org/shub/toddt/OpenAutism/latest/2018-08-15-2c79a150-b6d8abba/Singularity
collection: toddt/OpenAutism
---

# toddt/OpenAutism:latest

```bash
$ singularity pull shub://toddt/OpenAutism:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nipy/heudiconv
%post
/opt/conda/bin/conda install -yq --name=neuro pandas
```

## Collection

 - Name: [toddt/OpenAutism](https://github.com/toddt/OpenAutism)
 - License: [MIT License](https://api.github.com/licenses/mit)

