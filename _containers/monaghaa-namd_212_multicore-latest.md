---
id: 5067
name: "monaghaa/namd_212_multicore"
branch: "master"
tag: "latest"
commit: "1eddfde9edc863b05fa25e94f2d21e5b4ac45cbb"
version: "520d1e26fdc38ab5aa988ee0881144d5"
build_date: "2018-10-01T22:51:29.099Z"
size_mb: 216
size: 99282975
sif: "https://datasets.datalad.org/shub/monaghaa/namd_212_multicore/latest/2018-10-01-1eddfde9-520d1e26/520d1e26fdc38ab5aa988ee0881144d5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/namd_212_multicore/latest/2018-10-01-1eddfde9-520d1e26/
recipe: https://datasets.datalad.org/shub/monaghaa/namd_212_multicore/latest/2018-10-01-1eddfde9-520d1e26/Singularity
collection: monaghaa/namd_212_multicore
---

# monaghaa/namd_212_multicore:latest

```bash
$ singularity pull shub://monaghaa/namd_212_multicore:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%files 
NAMD_2.12_Linux-x86_64-multicore.tar.gz /opt

%post
apt-get update
apt-get install -y vim 
cd /opt
tar -xzvf NAMD_2.12_Linux-x86_64-multicore.tar.gz

echo 'export PATH=/opt/NAMD_2.12_Linux-x86_64-multicore:$PATH' >>$SINGULARITY_ENVIRONMENT

% environment
export PATH=/opt/NAMD_2.12_Linux-x86_64-multicore:$PATH
```

## Collection

 - Name: [monaghaa/namd_212_multicore](https://github.com/monaghaa/namd_212_multicore)
 - License: None

