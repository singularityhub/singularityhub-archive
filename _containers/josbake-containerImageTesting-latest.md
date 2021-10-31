---
id: 4562
name: "josbake/containerImageTesting"
branch: "master"
tag: "latest"
commit: "561c04478e6aefa0ec36b9681bffc235bfbc141c"
version: "a1d16bf435b36c5fe85e7300bbb02405"
build_date: "2018-08-31T03:21:36.669Z"
size_mb: 220
size: 93384735
sif: "https://datasets.datalad.org/shub/josbake/containerImageTesting/latest/2018-08-31-561c0447-a1d16bf4/a1d16bf435b36c5fe85e7300bbb02405.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/josbake/containerImageTesting/latest/2018-08-31-561c0447-a1d16bf4/
recipe: https://datasets.datalad.org/shub/josbake/containerImageTesting/latest/2018-08-31-561c0447-a1d16bf4/Singularity
collection: josbake/containerImageTesting
---

# josbake/containerImageTesting:latest

```bash
$ singularity pull shub://josbake/containerImageTesting:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:16.04


%post

    apt-get -y update

    apt-get -y install fortune cowsay lolcat


%environment
    export SINGULARITY_HTTP_PROXY="http://wwwproxy.sandia.gov:80/"
    export SINGULARITY_HTTPS_PROXY="https://wwwproxy.sandia.gov:80/"
    export LC_ALL=C

    export PATH=/usr/games:$PATH


%runscript

    fortune | cowsay | lolcat
```

## Collection

 - Name: [josbake/containerImageTesting](https://github.com/josbake/containerImageTesting)
 - License: None

