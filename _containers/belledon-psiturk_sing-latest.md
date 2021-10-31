---
id: 2505
name: "belledon/psiturk_sing"
branch: "master"
tag: "latest"
commit: "2eb124901ef391075c05a32ce71cca89acb0d1a2"
version: "0b3558d222afcef03df392805677e9e8"
build_date: "2018-04-13T04:44:02.333Z"
size_mb: 502
size: 203976735
sif: "https://datasets.datalad.org/shub/belledon/psiturk_sing/latest/2018-04-13-2eb12490-0b3558d2/0b3558d222afcef03df392805677e9e8.simg"
url: https://datasets.datalad.org/shub/belledon/psiturk_sing/latest/2018-04-13-2eb12490-0b3558d2/
recipe: https://datasets.datalad.org/shub/belledon/psiturk_sing/latest/2018-04-13-2eb12490-0b3558d2/Singularity
collection: belledon/psiturk_sing
---

# belledon/psiturk_sing:latest

```bash
$ singularity pull shub://belledon/psiturk_sing:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: ubuntu:16.04

%post
	
	apt-get update
	apt-get install -y 	build-essential \
						python-dev \
						python-pip \
						procps \
						ufw

	pip install --upgrade pip
	pip install --upgrade \
					psiturk


%environment
    export LC_ALL=C
    export PATH=/bin:/sbin:/usr/bin:/usr/sbin:$PATH
    export PSITURK_GLOBAL_CONFIG_LOCATION=~/.psiturkconfig
```

## Collection

 - Name: [belledon/psiturk_sing](https://github.com/belledon/psiturk_sing)
 - License: None

