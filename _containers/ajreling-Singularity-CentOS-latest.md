---
id: 2297
name: "ajreling/Singularity-CentOS"
branch: "master"
tag: "latest"
commit: "f3c46af4b0596e854b501e833b19dedabc01a873"
version: "83244bab09b01e3b7542ab186d8cb875"
build_date: "2018-03-26T20:31:23.727Z"
size_mb: 298
size: 104480799
sif: "https://datasets.datalad.org/shub/ajreling/Singularity-CentOS/latest/2018-03-26-f3c46af4-83244bab/83244bab09b01e3b7542ab186d8cb875.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ajreling/Singularity-CentOS/latest/2018-03-26-f3c46af4-83244bab/
recipe: https://datasets.datalad.org/shub/ajreling/Singularity-CentOS/latest/2018-03-26-f3c46af4-83244bab/Singularity
collection: ajreling/Singularity-CentOS
---

# ajreling/Singularity-CentOS:latest

```bash
$ singularity pull shub://ajreling/Singularity-CentOS:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%post

    yum update -y
```

## Collection

 - Name: [ajreling/Singularity-CentOS](https://github.com/ajreling/Singularity-CentOS)
 - License: None

