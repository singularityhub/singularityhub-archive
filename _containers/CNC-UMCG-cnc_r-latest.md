---
id: 3035
name: "CNC-UMCG/cnc_r"
branch: "master"
tag: "latest"
commit: "e4d8f7bd674968718b24924b2c578705bec8a916"
version: "93215479234baed268ebfe42c23199af"
build_date: "2018-06-05T00:16:52.104Z"
size_mb: 1755
size: 585625631
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_r/latest/2018-06-05-e4d8f7bd-93215479/93215479234baed268ebfe42c23199af.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_r/latest/2018-06-05-e4d8f7bd-93215479/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_r/latest/2018-06-05-e4d8f7bd-93215479/Singularity
collection: CNC-UMCG/cnc_r
---

# CNC-UMCG/cnc_r:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_r:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_base


%post
        apt-get install -y software-properties-common
 	echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
	gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
	gpg -a --export E084DAB9 | apt-key add -

	apt-get update

	apt-get install -y r-base r-base-dev
```

## Collection

 - Name: [CNC-UMCG/cnc_r](https://github.com/CNC-UMCG/cnc_r)
 - License: None

