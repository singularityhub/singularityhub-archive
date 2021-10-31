---
id: 3208
name: "csadorf/software"
branch: "master"
tag: "comet"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "7fd154645ab0c6fd160a4fa12e95f711"
build_date: "2019-01-08T23:44:45.551Z"
size_mb: 5238
size: 2199572511
sif: "https://datasets.datalad.org/shub/csadorf/software/comet/2019-01-08-3d509362-7fd15464/7fd154645ab0c6fd160a4fa12e95f711.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/csadorf/software/comet/2019-01-08-3d509362-7fd15464/
recipe: https://datasets.datalad.org/shub/csadorf/software/comet/2019-01-08-3d509362-7fd15464/Singularity
collection: csadorf/software
---

# csadorf/software:comet

```bash
$ singularity pull shub://csadorf/software:comet
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:comet

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

