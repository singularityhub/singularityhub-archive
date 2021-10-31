---
id: 4190
name: "ncy9371/singularity-buildtest"
branch: "master"
tag: "latest"
commit: "482df601ba14fdd3b24bd34b4bd6b5d9418c73c2"
version: "d43d387c64c76b70c43511235a4632b6"
build_date: "2018-08-28T03:21:34.884Z"
size_mb: 172
size: 82468895
sif: "https://datasets.datalad.org/shub/ncy9371/singularity-buildtest/latest/2018-08-28-482df601-d43d387c/d43d387c64c76b70c43511235a4632b6.simg"
url: https://datasets.datalad.org/shub/ncy9371/singularity-buildtest/latest/2018-08-28-482df601-d43d387c/
recipe: https://datasets.datalad.org/shub/ncy9371/singularity-buildtest/latest/2018-08-28-482df601-d43d387c/Singularity
collection: ncy9371/singularity-buildtest
---

# ncy9371/singularity-buildtest:latest

```bash
$ singularity pull shub://ncy9371/singularity-buildtest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:18.04

%help

hahahahahah

%labels

	Maintainer Eric Yeh
	Version v1.0

%post
	apt update
	apt install nginx -y

%runscript
	nginx
```

## Collection

 - Name: [ncy9371/singularity-buildtest](https://github.com/ncy9371/singularity-buildtest)
 - License: None

