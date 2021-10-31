---
id: 12174
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "jupyter3"
commit: "0f0e2130acfb186e3c07aaeaf0b845c7960d1e3e"
version: "355229609b5626f5996553d90cf3f31341243353753ec135853d93f916a61c36"
build_date: "2020-02-08T22:16:30.608Z"
size_mb: 968.484375
size: 1015529472
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter3/2020-02-08-0f0e2130-35522960/355229609b5626f5996553d90cf3f31341243353753ec135853d93f916a61c36.sif"
url: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter3/2020-02-08-0f0e2130-35522960/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter3/2020-02-08-0f0e2130-35522960/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:jupyter3

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:jupyter3
```

## Singularity Recipe

```singularity
#BootStrap: localimage
#From: centos
Bootstrap: shub
From: MBlaschek/singularity-jupyter:centos

%help

Container Centos 6.10 (docker)

Jupyter Notebook/Lab Server
Options:
  --NotebookApp.token='super-secret'    Token when not using a password
  --ip=0.0.0.0                          port forwarding from VirtualBox
  --NotebookApp.base_url='/ipython/'    Directory path
  --port=????                           Server port

Create Notebook Password (HOME/.jupyter/jupyter_notebook_config.json):
	jupyter notebook password

Check Jupyter paths:
	jupyter --paths

Check Jupyter Notebook Server running:
	jupyter notebook list

Anaconda Python 3 (Xarray, cfgrib, eccodes)
Eccodes and CFgrib are Software from ECMWF

%files
	run.sh /usr/bin

%runscript
	exec /usr/bin/run.sh "$@"

%apprun notebook
	echo "Notebook..."
	echo "Arguments are passed to jupyter!"

	echo "$(/opt/conda/bin/jupyter --paths)"
	echo "Check .jupyter3.log for Debug Infos"
	echo "PID in .jupyter3.pid"
	nohup /opt/conda/bin/jupyter notebook --NotebookApp.allow_origin="*" --no-browser $@ 2>&1 >> .jupyter3.log &
	echo "kill $!" > .jupyter3.pid
	sleep 5 && echo "Goto: $(cat .jupyter3.log | grep '] http' | tail -n1 | cut -d' ' -f 4)"

%apprun lab
	echo "Lab..."
	echo "Arguments are passed to jupyter!"
	if [ ! -e ${JUPYTERLAB_DIR}/static/index.html ]; then
		echo "First time launch, need to build laboratory ... (may take a while)"
		/opt/conda/bin/jupyter lab build
	fi
	echo "$(/opt/conda/bin/jupyter --paths)"
	echo "Check .jupyter3.log for Debug Infos"
	echo "PID in .jupyter3.pid"
	nohup /opt/conda/bin/jupyter lab --NotebookApp.allow_origin="*" --no-browser $@ 2>&1 >> .jupyter3.log &
	echo "kill $!" > .jupyter3.pid
	sleep 5 && echo "Goto: $(cat .jupyter3.log | grep '] http' | tail -n1 | cut -d' ' -f 4)"

%startscript
	# This is executed when instances are started
  	nohup /opt/conda/bin/jupyter notebook --NotebookApp.allow_origin="*" --no-browser $@ 2>&1 >> .jupyter3.log &
  	echo "kill $!" > .jupyter3.pid

%post
	wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh && \
	/opt/conda/bin/conda clean -tipsy && \
	ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
	echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
	echo "conda activate base" >> ~/.bashrc
	# Install jupyter notebook
	/opt/conda/bin/conda install jupyter jupyterlab numpy matplotlib pandas xarray bottleneck dask numba scipy netcdf4 cartopy -y --quiet
	/opt/conda/bin/pip install h5netcdf
	/opt/conda/bin/conda install -c conda-forge -y cfgrib eccodes nodejs
	/opt/conda/bin/conda clean -a -y
	# rename Container Kernel:
	sed -i 's/Python 3/Sy3/' /opt/conda/share/jupyter/kernels/python3/kernel.json
	#
	# Add tex and pandoc
	#
	wget https://github.com/jgm/pandoc/releases/download/2.9.1.1/pandoc-2.9.1.1-linux-amd64.tar.gz
	tar xvzf pandoc*.tar.gz --strip-components 1 -C /usr/local
	rm pandoc*.tar.gz
	yum install -y texlive-xetex texlive-latex texlive-texmf-fonts texlive-texmf-xetex texlive-texmf-latex
	yum clean -y all


%environment
	export PATH=/opt/conda/bin:$PATH
	# important part otherwise the server will try to access /run/user and fail
	export JUPYTER_RUNTIME_DIR=$PWD/.runtime
	# make sure we use container kernels, otherwise this will be overwritten
	# by $HOME/.local/share/jupyter/kernels
	export JUPYTER_DATA_DIR=$PWD/.kernels
	export JUPYTERLAB_DIR=$PWD/.lab
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

