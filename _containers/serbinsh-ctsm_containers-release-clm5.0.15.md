---
id: 7627
name: "serbinsh/ctsm_containers"
branch: "master"
tag: "release-clm5.0.15"
commit: "6e34200a46e3208c3fc88298ec63e48463a25d70"
version: "a474494865b3b862a239be3542342da8"
build_date: "2019-03-06T15:11:52.708Z"
size_mb: 1385
size: 554811423
sif: "https://datasets.datalad.org/shub/serbinsh/ctsm_containers/release-clm5.0.15/2019-03-06-6e34200a-a4744948/a474494865b3b862a239be3542342da8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/serbinsh/ctsm_containers/release-clm5.0.15/2019-03-06-6e34200a-a4744948/
recipe: https://datasets.datalad.org/shub/serbinsh/ctsm_containers/release-clm5.0.15/2019-03-06-6e34200a-a4744948/Singularity
collection: serbinsh/ctsm_containers
---

# serbinsh/ctsm_containers:release-clm5.0.15

```bash
$ singularity pull shub://serbinsh/ctsm_containers:release-clm5.0.15
```

## Singularity Recipe

```singularity
# ----------------------------------------------------------------------
# Debian baseOS with CTSM docker container
# ----------------------------------------------------------------------

Bootstrap: docker
From: serbinsh/ctsm_containers:baseos-stable-gcc550
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
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/ctsm_run_scripts/create_run1_f09_f09_clm5_test.sh \
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/ctsm_run_scripts/create_case_custom_res_compset.sh \
	&& wget https://raw.githubusercontent.com/serbinsh/ctsm_containers/master/ctsm_run_scripts/create_case_1pt_example_USNR1.sh \
	&& chmod 775 create_run1_f09_f09_clm5_test.sh \
	&& chmod 775 create_case_custom_res_compset.sh \
	&& chmod 775 create_case_1pt_example_USNR1.sh \
	&& chown clmuser /ctsm
	
	cd / \
	&& mkdir -p ctsm_example_data \
	&& chown clmuser /ctsm_example_data \
	&& cd ctsm_example_data \
	&& wget https://github.com/serbinsh/ctsm_containers/raw/master/ctsm_example_data/USNR1/USNR1_CTSM_Example_Data.tar.gz \
	&& tar -zxvf USNR1_CTSM_Example_Data.tar.gz \
	&& rm USNR1_CTSM_Example_Data.tar.gz

	## setup clmuser to use with docker - temporary hack, need to sort out how best to manage this
	export USER=clmuser

### EOF
```

## Collection

 - Name: [serbinsh/ctsm_containers](https://github.com/serbinsh/ctsm_containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

