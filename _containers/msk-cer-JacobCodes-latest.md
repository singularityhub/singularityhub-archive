---
id: 9751
name: "msk-cer/JacobCodes"
branch: "master"
tag: "latest"
commit: "fc1978320bdb5ad81ef43a617d8dac96f95e003c"
version: "04ea5e51edb4c530d763ded40181f03e"
build_date: "2019-06-11T20:52:50.977Z"
size_mb: 4666
size: 2021498911
sif: "https://datasets.datalad.org/shub/msk-cer/JacobCodes/latest/2019-06-11-fc197832-04ea5e51/04ea5e51edb4c530d763ded40181f03e.simg"
url: https://datasets.datalad.org/shub/msk-cer/JacobCodes/latest/2019-06-11-fc197832-04ea5e51/
recipe: https://datasets.datalad.org/shub/msk-cer/JacobCodes/latest/2019-06-11-fc197832-04ea5e51/Singularity
collection: msk-cer/JacobCodes
---

# msk-cer/JacobCodes:latest

```bash
$ singularity pull shub://msk-cer/JacobCodes:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2:R3.4.4_Bioc3.6

%post
	apt-get update 
	apt-get install -y libssl-dev libssh2-1-dev libcurl4-openssl-dev libxml2-dev texlive pandoc

	# Install R packages
	R --slave -e 'install.packages(c("glue", "devtools", "optparse", "rmarkdown", "roxygen2", "testthat", "knitr", "boot", "gplots", "ggthemes", "Rtsne", "xfun", "mvtnorm", "multcomp", "rms"))'
  	R --slave -e 'devtools::install_github("sartorlab/methylSig")'
	Rscript -e "source('http://bioconductor.org/biocLite.R'); biocLite(c('ComplexHeatmap', 'BiocCheck', 'BiocStyle', 'annotatr', 'bsseq', 'chipenrich', 'DelayedArray', 'DSS', 'GO.db', 'org.Dm.eg.db', 'org.Dr.eg.db', 'org.Gg.eg.db', 'org.Hs.eg.db', 'org.Mm.eg.db', 'org.Rn.eg.db', 'TxDb.Dmelanogaster.UCSC.dm3.ensGene', 'TxDb.Dmelanogaster.UCSC.dm6.ensGene', 'TxDb.Drerio.UCSC.danRer10.refGene', 'TxDb.Ggallus.UCSC.galGal5.refGene', 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'TxDb.Hsapiens.UCSC.hg38.knownGene', 'TxDb.Mmusculus.UCSC.mm9.knownGene', 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'TxDb.Rnorvegicus.UCSC.rn4.ensGene', 'TxDb.Rnorvegicus.UCSC.rn5.refGene', 'TxDb.Rnorvegicus.UCSC.rn6.refGene'), ask = TRUE);"
```

## Collection

 - Name: [msk-cer/JacobCodes](https://github.com/msk-cer/JacobCodes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

