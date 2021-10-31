---
id: 6558
name: "dyxmvp/singularity-images"
branch: "master"
tag: "latest"
commit: "5e5c4581022ae4069f2632a5dd10a7451394efe1"
version: "da652dba5647fa68403933aaf0d93b03"
build_date: "2019-01-24T17:50:06.891Z"
size_mb: 95
size: 37011487
sif: "https://datasets.datalad.org/shub/dyxmvp/singularity-images/latest/2019-01-24-5e5c4581-da652dba/da652dba5647fa68403933aaf0d93b03.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dyxmvp/singularity-images/latest/2019-01-24-5e5c4581-da652dba/
recipe: https://datasets.datalad.org/shub/dyxmvp/singularity-images/latest/2019-01-24-5e5c4581-da652dba/Singularity
collection: dyxmvp/singularity-images
---

# dyxmvp/singularity-images:latest

```bash
$ singularity pull shub://dyxmvp/singularity-images:latest
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:vsoch/singularity-images

%post

    echo "The sun is shining, the weather is sweeeet..."

%runscript

    exec echo "You say please, but all I see is pizza.."
```

## Collection

 - Name: [dyxmvp/singularity-images](https://github.com/dyxmvp/singularity-images)
 - License: None

