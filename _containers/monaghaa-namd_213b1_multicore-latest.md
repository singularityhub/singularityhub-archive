---
id: 5068
name: "monaghaa/namd_213b1_multicore"
branch: "master"
tag: "latest"
commit: "a8d101962d43f2f9018b2e40e236b03938d21976"
version: "63579b1b3e1ce3d558ad9b3d0861becb"
build_date: "2018-10-01T22:51:29.108Z"
size_mb: 240
size: 107720735
sif: "https://datasets.datalad.org/shub/monaghaa/namd_213b1_multicore/latest/2018-10-01-a8d10196-63579b1b/63579b1b3e1ce3d558ad9b3d0861becb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/namd_213b1_multicore/latest/2018-10-01-a8d10196-63579b1b/
recipe: https://datasets.datalad.org/shub/monaghaa/namd_213b1_multicore/latest/2018-10-01-a8d10196-63579b1b/Singularity
collection: monaghaa/namd_213b1_multicore
---

# monaghaa/namd_213b1_multicore:latest

```bash
$ singularity pull shub://monaghaa/namd_213b1_multicore:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%files 
NAMD_2.13b1_Linux-x86_64-multicore.tar.gz /opt

%post
apt-get update
apt-get install -y vim 
cd /opt
tar -xzvf NAMD_2.13b1_Linux-x86_64-multicore.tar.gz

echo 'export PATH=/opt/NAMD_2.13b1_Linux-x86_64-multicore:$PATH' >>$SINGULARITY_ENVIRONMENT

% environment
export PATH=/opt/NAMD_2.13b1_Linux-x86_64-multicore:$PATH
```

## Collection

 - Name: [monaghaa/namd_213b1_multicore](https://github.com/monaghaa/namd_213b1_multicore)
 - License: None

