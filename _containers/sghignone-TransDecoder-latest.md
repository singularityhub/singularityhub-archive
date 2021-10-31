---
id: 15492
name: "sghignone/TransDecoder"
branch: "main"
tag: "latest"
commit: "9a4002cc9a1e1df738f4bc4957014bb51ce2e847"
version: "5adea192cea348f732656fdec42870dc"
build_date: "2021-02-05T16:22:27.751Z"
size_mb: 738.0
size: 230543391
sif: "https://datasets.datalad.org/shub/sghignone/TransDecoder/latest/2021-02-05-9a4002cc-5adea192/5adea192cea348f732656fdec42870dc.sif"
url: https://datasets.datalad.org/shub/sghignone/TransDecoder/latest/2021-02-05-9a4002cc-5adea192/
recipe: https://datasets.datalad.org/shub/sghignone/TransDecoder/latest/2021-02-05-9a4002cc-5adea192/Singularity
collection: sghignone/TransDecoder
---

# sghignone/TransDecoder:latest

```bash
$ singularity pull shub://sghignone/TransDecoder:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%help
	Container with Brian Haas' TransDecoder, which identifies candidate coding regions within transcript sequences, such as those generated by de novo RNA-Seq transcript assembly using Trinity, or constructed based on RNA-Seq alignments to the genome using Tophat and Cufflinks.
	This installation is based on bioconda transdecoder 5.5.0

%labels
        author Stefano Ghignone
        maintainer sghignone
        name TransDecoder
        version 5.5.0

%post
        #SET CONDA ENVIRONMENT
        export PATH=/opt/conda/bin:${PATH}
	conda update -y conda
        conda update -n base -c defaults conda
        conda config --add channels conda-forge && \
        conda config --add channels bioconda && \
        conda config --add channels default
        #INSTALL SOFTWARE
        conda install -c bioconda transdecoder  && conda clean -a
```

## Collection

 - Name: [sghignone/TransDecoder](https://github.com/sghignone/TransDecoder)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)
