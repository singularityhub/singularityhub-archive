---
id: 10140
name: "romxero/R-singularity"
branch: "master"
tag: "latest"
commit: "fb0c4c5e6aa990b8e330bdc2d33cce5fe5a58cdc"
version: "1380e845eb425ce65dac7bb248224335"
build_date: "2019-07-01T20:21:50.894Z"
size_mb: 650
size: 256049183
sif: "https://datasets.datalad.org/shub/romxero/R-singularity/latest/2019-07-01-fb0c4c5e-1380e845/1380e845eb425ce65dac7bb248224335.simg"
url: https://datasets.datalad.org/shub/romxero/R-singularity/latest/2019-07-01-fb0c4c5e-1380e845/
recipe: https://datasets.datalad.org/shub/romxero/R-singularity/latest/2019-07-01-fb0c4c5e-1380e845/Singularity
collection: romxero/R-singularity
---

# romxero/R-singularity:latest

```bash
$ singularity pull shub://romxero/R-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:sid-slim
#
# Clush
#
#

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


%post
# Debian / Ubuntu
apt-get -ym update 
apt-get -ym install r-base r-base-dev r-base-core r-base-html

%runscript
	exec /usr/bin/R "$@"
```

## Collection

 - Name: [romxero/R-singularity](https://github.com/romxero/R-singularity)
 - License: None

