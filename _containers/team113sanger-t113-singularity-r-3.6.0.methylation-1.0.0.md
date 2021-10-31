---
id: 9922
name: "team113sanger/t113-singularity"
branch: "master"
tag: "r-3.6.0.methylation-1.0.0"
commit: "4dc2c1f3d6d79f142aeba699005c93a32ced7390"
version: "284dd0d77ca7233a318279a2eac04772"
build_date: "2019-12-09T12:41:31.284Z"
size_mb: 1809
size: 699994143
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/r-3.6.0.methylation-1.0.0/2019-12-09-4dc2c1f3-284dd0d7/284dd0d77ca7233a318279a2eac04772.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/r-3.6.0.methylation-1.0.0/2019-12-09-4dc2c1f3-284dd0d7/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/r-3.6.0.methylation-1.0.0/2019-12-09-4dc2c1f3-284dd0d7/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:r-3.6.0.methylation-1.0.0

```bash
$ singularity pull shub://team113sanger/t113-singularity:r-3.6.0.methylation-1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: team113sanger/t113-singularity:r-3.6.0.base-1.0.0
IncludeCmd: no

%help
Help message

%labels
        Maintainer Team113 Wellcome Sanger Institute
        Version v1.0.0
        R_Version 3.6.0

%environment
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

%post

	# Install R packages from bioconductor
	Rscript -e "install.packages('BiocManager', repos='https://www.stats.bris.ac.uk/R/', dependencies=TRUE, clean = TRUE)"
	Rscript -e "BiocManager::install('methylKit')"
  
	# Clean up
	yum clean all && rm -rf /var/cache/yum
	#rm -rf /tmp/${R_VERSION}
	#rm -rf /tmp/install-tl*
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

