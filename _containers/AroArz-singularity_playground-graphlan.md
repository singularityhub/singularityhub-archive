---
id: 15059
name: "AroArz/singularity_playground"
branch: "graphlan"
tag: "graphlan"
commit: "0a0e282daa6a67e70e66dc098165fe178286b612"
version: "8c01b451e3db8d2ea5f0519059c0f4a18e8c0cffd0f8c7cb126b2b998287079e"
build_date: "2021-02-08T22:30:15.537Z"
size_mb: 667.9375
size: 700383232
sif: "https://datasets.datalad.org/shub/AroArz/singularity_playground/graphlan/2021-02-08-0a0e282d-8c01b451/8c01b451e3db8d2ea5f0519059c0f4a18e8c0cffd0f8c7cb126b2b998287079e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/AroArz/singularity_playground/graphlan/2021-02-08-0a0e282d-8c01b451/
recipe: https://datasets.datalad.org/shub/AroArz/singularity_playground/graphlan/2021-02-08-0a0e282d-8c01b451/Singularity
collection: AroArz/singularity_playground
---

# AroArz/singularity_playground:graphlan

```bash
$ singularity pull shub://AroArz/singularity_playground:graphlan
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda



%post
        ### Installs graphlan, hclust2 and export2graphlan to conda environment "graphlan", then activates it.

        PATH=/opt/conda/bin:$PATH
        export PATH

	conda config --add channels defaults
	conda config --add channels bioconda
	conda config --add channels conda-forge

	conda install -c bioconda graphlan
        conda install -c bioconda export2graphlan

%runscript
        echo "$@"
```

## Collection

 - Name: [AroArz/singularity_playground](https://github.com/AroArz/singularity_playground)
 - License: None

