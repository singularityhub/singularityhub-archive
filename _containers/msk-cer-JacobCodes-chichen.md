---
id: 9766
name: "msk-cer/JacobCodes"
branch: "master"
tag: "chichen"
commit: "95785721f675aa1f6e8039f3110c593f20329a1c"
version: "242e8fcec14e545c134dca0f13f37956"
build_date: "2019-06-13T19:51:59.545Z"
size_mb: 4681
size: 2030497823
sif: "https://datasets.datalad.org/shub/msk-cer/JacobCodes/chichen/2019-06-13-95785721-242e8fce/242e8fcec14e545c134dca0f13f37956.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/msk-cer/JacobCodes/chichen/2019-06-13-95785721-242e8fce/
recipe: https://datasets.datalad.org/shub/msk-cer/JacobCodes/chichen/2019-06-13-95785721-242e8fce/Singularity
collection: msk-cer/JacobCodes
---

# msk-cer/JacobCodes:chichen

```bash
$ singularity pull shub://msk-cer/JacobCodes:chichen
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2:R3.4.4_Bioc3.6

%post
	apt-get update 
	apt-get install -y libssl-dev libssh2-1-dev libcurl4-openssl-dev libxml2-dev texlive pandoc

	# Install R packages
	R --slave -e 'install.packages(c("glue", "devtools", "optparse", "rmarkdown", "roxygen2", "testthat", "knitr", "boot", "gplots", "ggthemes", "ggrepel", "ggpubr", "Rtsne"))'
	R --slave -e 'install.packages(c("https://cran.r-project.org/src/contrib/Archive/xfun/xfun_0.4.tar.gz", "https://cran.r-project.org/src/contrib/Archive/mvtnorm/mvtnorm_1.0-8.tar.gz", "https://cran.r-project.org/src/contrib/Archive/multcomp/multcomp_1.4-8.tar.gz", "https://cran.r-project.org/src/contrib/Archive/rms/rms_5.1-2.tar.gz"))'
  	R --slave -e 'devtools::install_github("sartorlab/methylSig")'
	R --slave -e 'devtools::install_github("msk-cer/methylTools", auth_token="7955fd8863036fdc1c78c4c03b6f19b87e62296b")'
	Rscript -e "source('http://bioconductor.org/biocLite.R'); biocLite(c('ComplexHeatmap', 'BiocCheck', 'BiocStyle', 'annotatr', 'bsseq', 'chipenrich', 'DelayedArray', 'DSS', 'GO.db', 'org.Dm.eg.db', 'org.Dr.eg.db', 'org.Gg.eg.db', 'org.Hs.eg.db', 'org.Mm.eg.db', 'org.Rn.eg.db', 'TxDb.Dmelanogaster.UCSC.dm3.ensGene', 'TxDb.Dmelanogaster.UCSC.dm6.ensGene', 'TxDb.Drerio.UCSC.danRer10.refGene', 'TxDb.Ggallus.UCSC.galGal5.refGene', 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'TxDb.Hsapiens.UCSC.hg38.knownGene', 'TxDb.Mmusculus.UCSC.mm9.knownGene', 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'TxDb.Rnorvegicus.UCSC.rn4.ensGene', 'TxDb.Rnorvegicus.UCSC.rn5.refGene', 'TxDb.Rnorvegicus.UCSC.rn6.refGene'), ask = TRUE);"
```

## Collection

 - Name: [msk-cer/JacobCodes](https://github.com/msk-cer/JacobCodes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

