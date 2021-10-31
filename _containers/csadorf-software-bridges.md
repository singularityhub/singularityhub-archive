---
id: 2827
name: "csadorf/software"
branch: "master"
tag: "bridges"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "e5158a8c2dfad3bc507d92803f2fde0e"
build_date: "2019-01-08T23:44:45.539Z"
size_mb: 5191
size: 2187391007
sif: "https://datasets.datalad.org/shub/csadorf/software/bridges/2019-01-08-3d509362-e5158a8c/e5158a8c2dfad3bc507d92803f2fde0e.simg"
url: https://datasets.datalad.org/shub/csadorf/software/bridges/2019-01-08-3d509362-e5158a8c/
recipe: https://datasets.datalad.org/shub/csadorf/software/bridges/2019-01-08-3d509362-e5158a8c/Singularity
collection: csadorf/software
---

# csadorf/software:bridges

```bash
$ singularity pull shub://csadorf/software:bridges
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:bridges

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade \
		Click==7.0 \
		Keras==2.2.4 \
		rmsd==1.3.0 \
		tensorflow==1.12.0 \
		umap-learn==0.3.6

%environment
	export LC_ALL=C
```

## Collection

 - Name: [csadorf/software](https://github.com/csadorf/software)
 - License: [MIT License](https://api.github.com/licenses/mit)

