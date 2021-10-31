---
id: 14440
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "macs2"
commit: "7464be54cdc67a3419ac218d6e1fb574eb5322b6"
version: "ccf06ff1157ac5e1d213c87e96c3bb98074c0b1593816118bac43a5444a76a74"
build_date: "2020-09-24T20:01:24.528Z"
size_mb: 918.26171875
size: 962867200
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/macs2/2020-09-24-7464be54-ccf06ff1/ccf06ff1157ac5e1d213c87e96c3bb98074c0b1593816118bac43a5444a76a74.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/macs2/2020-09-24-7464be54-ccf06ff1/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/macs2/2020-09-24-7464be54-ccf06ff1/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:macs2

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:macs2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fooliu/macs2


%runscript
	echo "Running container fooliu/macs2:v2.2.5, macs2 v2.1.3"
	exec "$@"

%post
	mkdir /cluster /work /tsd /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

