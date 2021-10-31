---
id: 14453
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "bedtools"
commit: "7464be54cdc67a3419ac218d6e1fb574eb5322b6"
version: "6b29909cab8879b927629fa04cc9935098a9e29128419c5713a4fe95c4d31572"
build_date: "2020-09-25T13:57:30.738Z"
size_mb: 486.7890625
size: 510435328
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedtools/2020-09-25-7464be54-6b29909c/6b29909cab8879b927629fa04cc9935098a9e29128419c5713a4fe95c4d31572.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedtools/2020-09-25-7464be54-6b29909c/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedtools/2020-09-25-7464be54-6b29909c/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bedtools

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bedtools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biocontainers/bedtools:v2.28.0_cv2


%runscript
	echo "Running container biocontainers/bedtools:v2.28.0_cv2, bedtools v2.28.0"
	exec /bin/bash "$@"

%post
	mkdir /cluster /work /tsd /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

