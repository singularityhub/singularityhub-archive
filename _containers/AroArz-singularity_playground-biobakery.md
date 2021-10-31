---
id: 15056
name: "AroArz/singularity_playground"
branch: "biobakery"
tag: "biobakery"
commit: "19f4709df6b5c97549d8b960be915685a9d30669"
version: "cb8340179644777f660fa7d04ff3daa22c73dc0f220853c915171bfca2edcd8c"
build_date: "2021-04-19T12:57:53.480Z"
size_mb: 3628.68359375
size: 3804950528
sif: "https://datasets.datalad.org/shub/AroArz/singularity_playground/biobakery/2021-04-19-19f4709d-cb834017/cb8340179644777f660fa7d04ff3daa22c73dc0f220853c915171bfca2edcd8c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/AroArz/singularity_playground/biobakery/2021-04-19-19f4709d-cb834017/
recipe: https://datasets.datalad.org/shub/AroArz/singularity_playground/biobakery/2021-04-19-19f4709d-cb834017/Singularity
collection: AroArz/singularity_playground
---

# AroArz/singularity_playground:biobakery

```bash
$ singularity pull shub://AroArz/singularity_playground:biobakery
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3


%post
	### Sets correct channels and installs metaphlan3, humann3, strainphlan3 and krona

	PATH=/opt/conda/bin:$PATH
        export PATH	

	conda config --add channels defaults
	conda config --add channels bioconda
	conda config --add channels conda-forge
	conda config --add channels biobakery

	conda install -c bioconda -c biobakery python=3.7 metaphlan humann krona=2.7.1 -y


	humann_databases --download utility_mapping full /opt/humann --update-config yes
%files


%runscript
	echo "$@"
```

## Collection

 - Name: [AroArz/singularity_playground](https://github.com/AroArz/singularity_playground)
 - License: None

