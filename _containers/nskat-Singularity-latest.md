---
id: 3538
name: "nskat/Singularity"
branch: "master"
tag: "latest"
commit: "25b4765528b919aa36652b8d6ecefcf6b5012ba9"
version: "bec75a3455aa18b8554df6a36b0d7d25"
build_date: "2019-03-08T13:41:24.838Z"
size_mb: 1504
size: 632655903
sif: "https://datasets.datalad.org/shub/nskat/Singularity/latest/2019-03-08-25b47655-bec75a34/bec75a3455aa18b8554df6a36b0d7d25.simg"
url: https://datasets.datalad.org/shub/nskat/Singularity/latest/2019-03-08-25b47655-bec75a34/
recipe: https://datasets.datalad.org/shub/nskat/Singularity/latest/2019-03-08-25b47655-bec75a34/Singularity
collection: nskat/Singularity
---

# nskat/Singularity:latest

```bash
$ singularity pull shub://nskat/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:tensorflow/tensorflow:1.11.0

%post
apt-get update && apt-get install -y --no-install-recommends apt-utils
apt-get --force-yes -y install wget

pip install keras
pip install tables
pip install -U scikit-learn

apt-get -y --force-yes install git-core
apt-get -y --force-yes install apt-file
apt-file update
```

## Collection

 - Name: [nskat/Singularity](https://github.com/nskat/Singularity)
 - License: None

