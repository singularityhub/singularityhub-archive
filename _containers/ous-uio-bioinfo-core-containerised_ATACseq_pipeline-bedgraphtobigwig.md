---
id: 14454
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "bedgraphtobigwig"
commit: "d2eb117398b087dae36fce0f7172b036c843cb8b"
version: "cdaf181adced08b6ab311ffd4d09e45c83b880e34e0927043f727804ee1d4b6f"
build_date: "2020-10-12T18:41:51.046Z"
size_mb: 55.8984375
size: 58613760
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedgraphtobigwig/2020-10-12-d2eb1173-cdaf181a/cdaf181adced08b6ab311ffd4d09e45c83b880e34e0927043f727804ee1d4b6f.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedgraphtobigwig/2020-10-12-d2eb1173-cdaf181a/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/bedgraphtobigwig/2020-10-12-d2eb1173-cdaf181a/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bedgraphtobigwig

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:bedgraphtobigwig
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%post
	apt-get update && apt-get install -y \
	curl && \
	apt-get clean autoclean && \
	apt-get autoremove -y && \
	apt-get install -y rsync

	rsync -aP \
		rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/bedGraphToBigWig /usr/bin/

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with bedgraphtobigwig v4"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

