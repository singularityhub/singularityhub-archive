---
id: 8805
name: "Eric716/singularity"
branch: "master"
tag: "latest"
commit: "567a1bb05cace74013ff90709749156714acf754"
version: "d8d6073213d95a0d7f0e51e4917dc5c8"
build_date: "2019-05-03T14:43:31.745Z"
size_mb: 4757
size: 1964711967
sif: "https://datasets.datalad.org/shub/Eric716/singularity/latest/2019-05-03-567a1bb0-d8d60732/d8d6073213d95a0d7f0e51e4917dc5c8.simg"
url: https://datasets.datalad.org/shub/Eric716/singularity/latest/2019-05-03-567a1bb0-d8d60732/
recipe: https://datasets.datalad.org/shub/Eric716/singularity/latest/2019-05-03-567a1bb0-d8d60732/Singularity
collection: Eric716/singularity
---

# Eric716/singularity:latest

```bash
$ singularity pull shub://Eric716/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: eric716/tensorflow-18.12-py3:v1

%post  
echo "This section happens once after bootstrap to build the image."
```

## Collection

 - Name: [Eric716/singularity](https://github.com/Eric716/singularity)
 - License: None

