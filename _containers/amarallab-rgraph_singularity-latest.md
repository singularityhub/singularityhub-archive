---
id: 10679
name: "amarallab/rgraph_singularity"
branch: "master"
tag: "latest"
commit: "3248f708ef7d78c17404af0ef55f59adbeedbf1c"
version: "bb89eedb85e582687b4e63a281fc5e26"
build_date: "2019-08-21T19:35:08.899Z"
size_mb: 125.0
size: 54624287
sif: "https://datasets.datalad.org/shub/amarallab/rgraph_singularity/latest/2019-08-21-3248f708-bb89eedb/bb89eedb85e582687b4e63a281fc5e26.sif"
url: https://datasets.datalad.org/shub/amarallab/rgraph_singularity/latest/2019-08-21-3248f708-bb89eedb/
recipe: https://datasets.datalad.org/shub/amarallab/rgraph_singularity/latest/2019-08-21-3248f708-bb89eedb/Singularity
collection: amarallab/rgraph_singularity
---

# amarallab/rgraph_singularity:latest

```bash
$ singularity pull shub://amarallab/rgraph_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: ubuntu:18.10

%labels
MAINTAINER amaral lab

%post
	apt-get update
	apt-get upgrade -y
	apt-get install -y git build-essential autoconf libtool libgsl0-dev gsl-bin
	cd /
	rm -rf /rgraph
	git clone https://github.com/seeslab/rgraph.git
	cd /rgraph
	./autogen.sh
	./configure
	make
	apt-get remove -y --purge git build-essential autoconf libtool libgsl0-dev
	apt-get autoremove -y
	cp /rgraph/netcarto/netcarto /usr/bin
	cp /rgraph/netcarto/netcarto-legacy /usr/bin
	cp /rgraph/only_deg/only_degeneration_mb /usr/bin
	cp /rgraph/only_deg/only_degeneration_mb_gibbs /usr/bin
	cp /rgraph/recommender/multi_recommend_2 /usr/bin
	cp /rgraph/recommender/multi_recommend_k /usr/bin
	cp /rgraph/recommender/multi_recommend_k_gibbs /usr/bin
	cp /rgraph/reliability/reliability_links /usr/bin
	cp /rgraph/reliability/reliability_links_gibbs /usr/bin
	cp /rgraph/reliability/reliability_links_gibbs_sparse /usr/bin
	cp /rgraph/reliability/reliability_links_k /usr/bin
	cp /rgraph/reliability/reliability_reconstruct /usr/bin
	cp /rgraph/test-driver /usr/bin
	cp /rgraph/utils/bipartitemodularity /usr/bin
	cp /rgraph/utils/bipartitemodularity_w /usr/bin
	cp /rgraph/utils/countlinks /usr/bin
	cp /rgraph/utils/getgiant /usr/bin
	cp /rgraph/utils/lapspec /usr/bin
	cp /rgraph/utils/modularbipart /usr/bin
	cp /rgraph/utils/multinetlayout /usr/bin
	cp /rgraph/utils/mutualinfo /usr/bin
	cp /rgraph/utils/netcompare /usr/bin
	cp /rgraph/utils/netlayout /usr/bin
	cp /rgraph/utils/netprop /usr/bin
	cp /rgraph/utils/netrandomize /usr/bin
	cp /rgraph/utils/nodeprop /usr/bin
	rm -rf /rgraph
	
%runscript
	exec  /usr/bin/netcarto "$@"
```

## Collection

 - Name: [amarallab/rgraph_singularity](https://github.com/amarallab/rgraph_singularity)
 - License: None

