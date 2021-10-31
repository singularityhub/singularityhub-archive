---
id: 6686
name: "acharles7/Singularity"
branch: "master"
tag: "latest"
commit: "1d0f1fff2886ff485920300448427c7a8283b69c"
version: "75c938ba0cdb68ca98ac20ff995370e6"
build_date: "2019-01-29T17:36:14.961Z"
size_mb: 76
size: 27955231
sif: "https://datasets.datalad.org/shub/acharles7/Singularity/latest/2019-01-29-1d0f1fff-75c938ba/75c938ba0cdb68ca98ac20ff995370e6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/acharles7/Singularity/latest/2019-01-29-1d0f1fff-75c938ba/
recipe: https://datasets.datalad.org/shub/acharles7/Singularity/latest/2019-01-29-1d0f1fff-75c938ba/Singularity
collection: acharles7/Singularity
---

# acharles7/Singularity:latest

```bash
$ singularity pull shub://acharles7/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu
IncludeCmd: no

%post
	mkdir test
	touch test/test.txt

%runscript
	echo "Hello I am Test Container"
```

## Collection

 - Name: [acharles7/Singularity](https://github.com/acharles7/Singularity)
 - License: None

