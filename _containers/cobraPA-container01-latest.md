---
id: 14178
name: "cobraPA/container01"
branch: "conda_python_extrasitepacks"
tag: "latest"
commit: "1d1deba7afa5e4c041aecba04baa3c5d25f66a07"
version: "838ec79eda2bc91ee12a4fbd45db1455b3f3fc2a34d43d3aa3fb05794348e10a"
build_date: "2020-09-08T17:57:07.296Z"
size_mb: 659.5859375
size: 691625984
sif: "https://datasets.datalad.org/shub/cobraPA/container01/latest/2020-09-08-1d1deba7-838ec79e/838ec79eda2bc91ee12a4fbd45db1455b3f3fc2a34d43d3aa3fb05794348e10a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cobraPA/container01/latest/2020-09-08-1d1deba7-838ec79e/
recipe: https://datasets.datalad.org/shub/cobraPA/container01/latest/2020-09-08-1d1deba7-838ec79e/Singularity
collection: cobraPA/container01
---

# cobraPA/container01:latest

```bash
$ singularity pull shub://cobraPA/container01:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:conda/miniconda3-centos7

%labels
MAINTAINER singular55

%environment
	LANG=C.UTF-8
	# couldn't change LC_ALL on target
	#LC_ALL=C.UTF-8
	PATH=/bin_override:$PATH
	LIBRARY_PATH=/lib_override:$LIBRARY_PATH
	LD_LIBRARY_PATH=/lib_override:$LD_LIBRARY_PATH
	#LD_LIBRARY_PATH=/lib_override:/usr/local/envs/idp/lib/libfabric:$LD_LIBRARY_PATH
	#FI_PROVIDER_PATH=/usr/local/envs/idp/lib/libfabric/prov:$FI_PROVIDER_PATH
	#WORKDIR=/work
	WRITEABLE=~/Container_Writeable
	#SITEEXTRA=$WRITEABLE/site-packages-extra
	#export LC_ALL LANG PATH LIBRARY_PATH LD_LIBRARY_PATH WORKDIR
	export LANG PATH LIBRARY_PATH LD_LIBRARY_PATH WRITEABLE


	## https://github.com/hpcng/singularity/issues/5075
	#action="${1##*/}"
    #if [ "$action" = "shell" ]; then
    #    if [ "${SINGULARITY_SHELL:-}" = "/bin/bash" ]; then
    #        set -- --noprofile --init-file /.sing_bash
    #    elif test -z "${SINGULARITY_SHELL:-}"; then
    #        export SINGULARITY_SHELL=/bin/bash
    #        set -- --noprofile --init-file /.sing_bash
    #    fi
    #fi
	
	
#%setup
	#mkdir -p $SINGULARITY_ROOTFS/lib_override
	#mkdir -p $SINGULARITY_ROOTFS/bin_override
	#mkdir -p $SINGULARITY_ROOTFS/work




	## mysql - full install
	# https://dev.mysql.com/downloads/file/?id=495278 - login
	# https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz
	#wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz -O /tmp/mysql.tar.xz
	#tar -xf /tmp/mysql.tar.xz -C $SINGULARITY_ROOTFS/bin_override
	#rm /tmp/mysql.tar.xz




%post
	mkdir -p /lib_override
	mkdir -p /bin_override
	
	#yum --enablerepo=extras install -y epel-release
	yum -y install epel-release	
	
	
	
	yum repolist
	yum install -y wget less which libfabric
	
	# even with gpgcheck=0, still fails to install?
	#yum install intelpython3 intel-mpi


	#wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	#sh Miniconda3-latest-Linux-x86_64.sh

	#sh bashrc
	
	# no prompt, no progress bars (-q)
	conda update -y -q conda
	
	conda config --add channels intel
	# full install fails, seems to die when we add conda franz package
	#conda create -y -q -n idp intelpython3_full python=3
	# intel-mpi not available in intel channel...
	# mpi4py intel build has some issues with libfabric...
	# but yum install libfabric seems to fix them
	conda create -y -q -n idp intelpython3_core python=3 mpi4py
	
	conda -V

	conda config --set pip_interop_enabled True
	
	## setup conda / pip interop
	#echo $SHELL
	#conda init bash
	#source .bashrc
	#conda activate idp
	##grab the one package we need from pip
	#pip install cpe
	#conda deactivate
	
	
	## try pip before conda packages, add which with yum
	# enable env for pip install
	. /usr/local/etc/profile.d/conda.sh
	conda activate idp
	#conda config --set pip_interop_enabled True
	#grab the one package we need from pip
	#workaround issue in Intel MPI
	# https://community.intel.com/t5/Intel-Distribution-for-Python/mpi4py-ImportError-libfabric-so-1/td-p/1139856
	#LD_LIBRARY_PATH=/usr/local/envs/idp/lib/libfabric:$LD_LIBRARY_PATH  FI_PROVIDER_PATH=/usr/local/envs/idp/lib/libfabric/prov:$FI_PROVIDER_PATH  pip install cpe
	pip install cpe
	#LD_LIBRARY_PATH=/usr/local/envs/idp/lib/libfabric:$LD_LIBRARY_PATH  FI_PROVIDER_PATH=/usr/local/envs/idp/lib/libfabric/prov:$FI_PROVIDER_PATH  conda deactivate
	conda deactivate
	##
	
	
	# avoid intel for mpi (recipe to override default intel channel for a package)
	#conda install -c anaconda mpi4py --override-channels

	conda install -y -q -n idp -c franzinc agraph-python
	# auto cpe errors because it is python 2.7 only
	#conda install -y -n idp -c auto cpe
	conda install -y -q -n idp -c anaconda keyring more-itertools
	# argparse removed, py2 only, and builtin in py3_2
	conda install -y -q -n idp -c conda-forge plotly pylint rdflib tqdm
	# functools builtin in py3?
	#conda install -y -q -n idp -c travis functools 

	# cleanup install (from https://hpc.nih.gov/apps/singularity.html )
	conda clean --index-cache --tarballs --packages --yes


	# works for conda defines
	#echo "source /usr/local/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT
	# doesn't seem to work, still complains about conda init 'shell'
	#echo "source /condainit_rc.sh" >> $SINGULARITY_ENVIRONMENT


	#echo "source /usr/local/etc/profile.d/conda.sh" >> /.sing_bash	
	#echo "source /condainit_rc.sh" >> ./sing_bash
	
	# could also activate
	#echo "conda activate idp"
	
	
	# says bash - but not interactive?
	#echo $SHELL
	## Doesn't work on HPC
	#conda init bash
	#source .bashrc
	
	
	### disabled, trying before conda installs
	## enable env for pip install
	#. /usr/local/etc/profile.d/conda.sh
	#conda activate idp
	##conda config --set pip_interop_enabled True
	##grab the one package we need from pip
	#pip install cpe
	#conda deactivate
	
	
	#fix some X / DBus issues?
	#dbus-uuidgen > /var/lib/dbus/machine-id

	# make a hook for extra python module installs
	#ln -s ${SITEEXTRA} /usr/local/envs/idp/lib/python3.7/site-packages/site-packages-extra
	
	##############
	## make some HPC root dirs
	mkdir -p /app /apps /gpfs
	
	

#%setup
#	echo $SHELL
#	conda init bash
#	source .bashrc
#	conda activate idp
#	#conda config --set pip_interop_enabled True
#	#grab the one package we need from pip
#	pip install cpe
#	conda deactivate


%files
	#eclipse.ini eclipse.ini
	#eclipse-parallel.ini eclipse-parallel.ini
	condainit_rc.sh /condainit_rc.sh
	# not used?
	#sitecustomize.py /usr/local/envs/idp/lib/python3.7/site-packages/sitecustomize.py
	sitecustomize.py /usr/local/envs/idp/lib/python3.7/sitecustomize.py

%startscript
	source /usr/local/etc/profile.d/conda.sh
	source /condainit_rc.sh

%runscript
	#exec /bin/echo "Hi there, container runscript!"
	#exec /usr/bin/meld

	#mkdir -p ${WRITEABLE}
	#touch ${WRITEABLE}/HiThere

	#/bin/echo "Config files should go in ${WRITEABLE}."


#%apprun meld
	#exec meld "$@"


#%apprun eclipse
	#exec /bin_override/eclipse/eclipse "$@"
```

## Collection

 - Name: [cobraPA/container01](https://github.com/cobraPA/container01)
 - License: None

