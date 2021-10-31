---
id: 7628
name: "serbinsh/ctsm_containers"
branch: "master"
tag: "ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0"
commit: "21d441032d9ac3abf44880659353d6460f5c4a20"
version: "df4c1df432f8ee2a0776088c499a687b"
build_date: "2019-03-06T15:11:52.701Z"
size_mb: 1383
size: 553500703
sif: "https://datasets.datalad.org/shub/serbinsh/ctsm_containers/ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0/2019-03-06-21d44103-df4c1df4/df4c1df432f8ee2a0776088c499a687b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/serbinsh/ctsm_containers/ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0/2019-03-06-21d44103-df4c1df4/
recipe: https://datasets.datalad.org/shub/serbinsh/ctsm_containers/ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0/2019-03-06-21d44103-df4c1df4/Singularity
collection: serbinsh/ctsm_containers
---

# serbinsh/ctsm_containers:ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0

```bash
$ singularity pull shub://serbinsh/ctsm_containers:ctsm-clm5.0.15-fates-fates_s1.8.1_a3.0.0
```

## Singularity Recipe

```singularity
# ----------------------------------------------------------------------
# Debian baseOS with CTSM docker container
# ----------------------------------------------------------------------

Bootstrap: docker
From: serbinsh/ctsm_containers:baseos-develop-gcc550
MAINTAINER S.P. Serbin email: sserbin@bnl.gov

%environment
	LANGUAGE=en_US.UTF-8
	LC_ALL=en_US.UTF-8
	LANG=en_US.UTF-8
	LC_TYPE=en_US.UTF-8
	USER=clmuser

%post
	echo LANGUAGE="en_US.UTF-8" > /etc/default/locale
	echo LANG="en_US.UTF-8" >> /etc/default/locale
	echo LC_ALL="en_US.UTF-8" >> /etc/default/locale
	echo LC_TYPE ="en_US.UTF-8" >> /etc/default/locale
	echo "export USER=clmuser" > /etc/environment

	export CTSM_BRANCH='release-clm5.0.15'

	## temporary fix here, needs to be in baseOS.  setting gmake
	ln -s /usr/bin/make /usr/bin/gmake

	## create data mount point in container - should change this to /mnt or something more generic in machines files
	cd / \
	&& mkdir -p data \
	&& mkdir -p ctsm_output
	chown clmuser /data
	chown clmuser /ctsm_output

	## Checkout CTSM model
	echo "*** Checkout CTSM model"
	cd / \
	&& git -c http.sslVerify=false clone -b ${CTSM_BRANCH} --single-branch --depth 1 https://github.com/ESCOMP/ctsm.git \
	&& cd ctsm \
	&& ./manage_externals/checkout_externals \
	&& git tag \
	&& cd cime/config/cesm/machines/ \
	&& rm config_compilers.xml \
	&& rm config_machines.xml \
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/cime_config_files/cesm/machines/config_compilers.xml \
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/cime_config_files/cesm/machines/config_machines.xml \
	&& cd / \
	&& mkdir -p ctsm_run_scripts \
	&& cd ctsm_run_scripts \
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/ctsm_run_scripts/create_case_ctsmfates_1pt_example_1x1brazil.sh \
	&& chmod 775 create_case_ctsmfates_1pt_example_1x1brazil.sh \
	&& chown clmuser /ctsm

	## setup clmuser to use with docker - temporary hack, need to sort out how best to manage this
	export USER=clmuser

### EOF
```

## Collection

 - Name: [serbinsh/ctsm_containers](https://github.com/serbinsh/ctsm_containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

