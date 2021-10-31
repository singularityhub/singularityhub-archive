---
id: 12175
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "jupyter23"
commit: "0f0e2130acfb186e3c07aaeaf0b845c7960d1e3e"
version: "d412ddde435316f3d4db05065ab5460f4e204b42e1f9fb699315158f27348b8f"
build_date: "2020-02-11T16:06:23.284Z"
size_mb: 1231.12109375
size: 1290924032
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter23/2020-02-11-0f0e2130-d412ddde/d412ddde435316f3d4db05065ab5460f4e204b42e1f9fb699315158f27348b8f.sif"
url: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter23/2020-02-11-0f0e2130-d412ddde/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jupyter23/2020-02-11-0f0e2130-d412ddde/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:jupyter23

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:jupyter23
```

## Singularity Recipe

```singularity
# Local centos 6.10 image
# Bootstrap: localimage
# From: centos610
Bootstrap: shub
From: MBlaschek/singularity-jupyter:centos
# most recent and debian image
# BootStrap: docker
# From: continuumio/miniconda3

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

Anaconda Python 3 & 2.7 (Xarray, cfgrib, eccodes)
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
	sleep 5 && echo "Goto: $(cat .jupyter3.log | grep ' http://localhost' | tail -n1 | cut -d' ' -f 4)"

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
	sleep 5 && echo "Goto: $(cat .jupyter3.log | grep ' http://localhost' | tail -n1 | cut -d' ' -f 4)"

%apprun py2
	echo "Starting Ipython 2"
	echo "$(/opt/conda/envs/py2/bin/jupyter --paths)"
	exec /opt/conda/envs/py2/bin/ipython $@

%startscript
# This is executed when instances are started
  	nohup /opt/conda/bin/jupyter notebook --NotebookApp.allow_origin="*" --no-browser $@ 2>&1 >> .jupyter3.log &
  	echo "kill $!" > .jupyter3.pid

%post
	export PATH=/opt/conda/bin:$PATH
	wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh && \
	/opt/conda/bin/conda clean -tipsy && \
	ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
	echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
	echo "conda activate base" >> ~/.bashrc
	# Install jupyter notebook
	/opt/conda/bin/conda install jupyter jupyterlab numpy matplotlib pandas netcdf4 scipy numba xarray cartopy bottleneck dask -y
	/opt/conda/bin/pip install h5netcdf
	/opt/conda/bin/conda install -c conda-forge -y cfgrib eccodes nodejs
	/opt/conda/bin/conda create -n py2 python=2 ipykernel numpy pandas matplotlib scipy xarray numba netcdf4 -y
	/opt/conda/envs/py2/bin/python -m ipykernel install
	sed -i 's/Python 3/Sy3/' /opt/conda/share/jupyter/kernels/python3/kernel.json
	sed -i 's/Python 2/Sy2/' /usr/local/share/jupyter/kernels/python2/kernel.json
	/opt/conda/bin/conda clean -a -y
	#
	# Add tex and pandoc
	#
	wget https://github.com/jgm/pandoc/releases/download/2.9.1.1/pandoc-2.9.1.1-linux-amd64.tar.gz
	tar xvzf pandoc*.tar.gz --strip-components 1 -C /usr/local
	rm pandoc*.tar.gz
	yum install -y texlive-xetex texlive-latex texlive-texmf-fonts texlive-texmf-xetex texlive-texmf-latex
	# Clean
	yum clean -y all

%environment
	export PATH=/opt/conda/bin:$PATH
	# important part otherwise the server will try to access /run/user and fail
	export JUPYTER_RUNTIME_DIR=$PWD/.runtime
	# Make sure we use container kernels
	export JUPYTER_DATA_DIR=$PWD/.kernels
    export JUPYTERLAB_DIR=$PWD/.jupyter/lab
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

