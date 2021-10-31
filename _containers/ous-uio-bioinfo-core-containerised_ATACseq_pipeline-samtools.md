---
id: 14437
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "samtools"
commit: "7464be54cdc67a3419ac218d6e1fb574eb5322b6"
version: "49c2d64dfeee90963e905addc556943e10ffb66c7cf6e9969cebf49bf476a8b1"
build_date: "2021-03-06T01:07:02.280Z"
size_mb: 396.9453125
size: 416227328
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/samtools/2021-03-06-7464be54-49c2d64d/49c2d64dfeee90963e905addc556943e10ffb66c7cf6e9969cebf49bf476a8b1.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/samtools/2021-03-06-7464be54-49c2d64d/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/samtools/2021-03-06-7464be54-49c2d64d/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:samtools

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:samtools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biocontainers/samtools:v1.7.0_cv4


%runscript
	echo "Running container biocontainers/samtools:v1.7.0_cv4, samtools v1.3.1"
	exec /bin/bash "$@"

%post
	mkdir /cluster /work /tsd /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

