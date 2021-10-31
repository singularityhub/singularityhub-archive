---
id: 15057
name: "AroArz/singularity_playground"
branch: "only_snakemake"
tag: "snakemake"
commit: "6c889370b927150f052ff86552fffb5f7c5b544f"
version: "0b2039c8ad4a676f9e4771ab9bc928f2d31098bb7fea54a94d57d376fcb5d48e"
build_date: "2020-12-05T19:50:01.745Z"
size_mb: 784.51953125
size: 822628352
sif: "https://datasets.datalad.org/shub/AroArz/singularity_playground/snakemake/2020-12-05-6c889370-0b2039c8/0b2039c8ad4a676f9e4771ab9bc928f2d31098bb7fea54a94d57d376fcb5d48e.sif"
url: https://datasets.datalad.org/shub/AroArz/singularity_playground/snakemake/2020-12-05-6c889370-0b2039c8/
recipe: https://datasets.datalad.org/shub/AroArz/singularity_playground/snakemake/2020-12-05-6c889370-0b2039c8/Singularity
collection: AroArz/singularity_playground
---

# AroArz/singularity_playground:snakemake

```bash
$ singularity pull shub://AroArz/singularity_playground:snakemake
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3



%post
	### Installs snakemake

	PATH=/opt/conda/bin:$PATH
        export PATH	
	conda install -c conda-forge mamba
	mamba create -c conda-forge -c bioconda -n snakemake snakemake -y


	### Creates a bash script to run snakemake	

	echo \#\!/bin/bash > /opt/runscript.sh
	echo source activate snakemake >> /opt/runscript.sh
	echo \$\@ >> /opt/runscript.sh

%runscript
	### Starts runscript.sh, everything you type after "sing run snakemake.sif" is forwarded to the runscript.
	### e.g. "sing run snakemake.sif snakemake --dryrun" forwards "snakemake --dryrun" to runscript.sh and executes that command. 

	bash /opt/runscript.sh "$@"
	echo "$@"
```

## Collection

 - Name: [AroArz/singularity_playground](https://github.com/AroArz/singularity_playground)
 - License: None

