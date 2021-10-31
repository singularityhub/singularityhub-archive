---
id: 14441
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "fastqc"
commit: "7464be54cdc67a3419ac218d6e1fb574eb5322b6"
version: "ecf5cd8fd25da8ec0b30451cb428940fec9a035db51cfafdebf11eab51bab55d"
build_date: "2021-01-12T15:51:16.967Z"
size_mb: 351.23046875
size: 368291840
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/fastqc/2021-01-12-7464be54-ecf5cd8f/ecf5cd8fd25da8ec0b30451cb428940fec9a035db51cfafdebf11eab51bab55d.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/fastqc/2021-01-12-7464be54-ecf5cd8f/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/fastqc/2021-01-12-7464be54-ecf5cd8f/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:fastqc

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:fastqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biocontainers/fastqc:v0.11.5_cv4


%runscript
	echo "Running container biocontainers/fastqc:v0.11.5_cv4, FastQC v0.11.5"
	exec /bin/bash "$@"

%post
	mkdir /cluster /work /tsd /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

