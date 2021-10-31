---
id: 7878
name: "elimoss/lathe"
branch: "master"
tag: "htsbox"
commit: "f53adf65c4ec29d1c54c1b903be887bd5254292e"
version: "3228a77487ab06b19155706d3892097a"
build_date: "2021-04-14T14:34:57.958Z"
size_mb: 388
size: 147169311
sif: "https://datasets.datalad.org/shub/elimoss/lathe/htsbox/2021-04-14-f53adf65-3228a774/3228a77487ab06b19155706d3892097a.simg"
url: https://datasets.datalad.org/shub/elimoss/lathe/htsbox/2021-04-14-f53adf65-3228a774/
recipe: https://datasets.datalad.org/shub/elimoss/lathe/htsbox/2021-04-14-f53adf65-3228a774/Singularity
collection: elimoss/lathe
---

# elimoss/lathe:htsbox

```bash
$ singularity pull shub://elimoss/lathe:htsbox
```

## Singularity Recipe

```singularity
# Metagenomics Singularity environment definition for htsbox repository
# Eli Moss
# elimoss@stanford.edu
# January 2019

# This environment is used in practice by adding --with-singularity shub://elimoss/metagenomics_workflows:longread
# to the snakemake command.

bootstrap: docker
from: ubuntu:19.04

# this command assumes at least singularity 2.3
%environment
%post
    apt-get update
    apt-get install -y eatmydata
    eatmydata apt-get install -y \
    git ca-certificates zlib1g-dev libbz2-dev liblzma-dev bedtools
    apt-get clean

    apt-get install -y build-essential

		git clone https://github.com/lh3/htsbox.git
		cd htsbox
		make
		cp htsbox /usr/bin/
```

## Collection

 - Name: [elimoss/lathe](https://github.com/elimoss/lathe)
 - License: [MIT License](https://api.github.com/licenses/mit)

