---
id: 14451
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "bowtie2"
commit: "d2eb117398b087dae36fce0f7172b036c843cb8b"
version: "854da6db2fdc96f3da8abfeed56a9112238e3ea07e36751fafd6c7f3cdf256f1"
build_date: "2021-03-06T01:06:10.071Z"
size_mb: 250.2890625
size: 262447104
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bowtie2/2021-03-06-d2eb1173-854da6db/854da6db2fdc96f3da8abfeed56a9112238e3ea07e36751fafd6c7f3cdf256f1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bowtie2/2021-03-06-d2eb1173-854da6db/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bowtie2/2021-03-06-d2eb1173-854da6db/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bowtie2

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bowtie2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biocontainers/bowtie2:v2.3.1_cv1


%runscript
	echo "Running container biocontainers/bowtie2:v2.3.1_cv1, bowtie2 v2.2.9"
	exec /bin/bash "$@"

%post
	mkdir /cluster /work /tsd /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

