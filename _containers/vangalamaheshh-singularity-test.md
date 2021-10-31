---
id: 9094
name: "vangalamaheshh/singularity"
branch: "master"
tag: "test"
commit: "2b16d154b5d64723f43b46f98bd95ff41ab65f19"
version: "998022f0f5c7fd158d28ca0cd41fb62f"
build_date: "2019-05-15T18:46:10.369Z"
size_mb: 296
size: 121962527
sif: "https://datasets.datalad.org/shub/vangalamaheshh/singularity/test/2019-05-15-2b16d154-998022f0/998022f0f5c7fd158d28ca0cd41fb62f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vangalamaheshh/singularity/test/2019-05-15-2b16d154-998022f0/
recipe: https://datasets.datalad.org/shub/vangalamaheshh/singularity/test/2019-05-15-2b16d154-998022f0/Singularity
collection: vangalamaheshh/singularity
---

# vangalamaheshh/singularity:test

```bash
$ singularity pull shub://vangalamaheshh/singularity:test
```

## Singularity Recipe

```singularity
Bootstrap: shub
FROM: singularityhub/ubuntu

%runscript
	exec echo "Hello from ubuntu world"

%labels
	AUTHOR Mahesh Vangala

%post
	apt-get update -y &&
	apt-get install -y vim
```

## Collection

 - Name: [vangalamaheshh/singularity](https://github.com/vangalamaheshh/singularity)
 - License: None

