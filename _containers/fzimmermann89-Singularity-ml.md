---
id: 15345
name: "fzimmermann89/Singularity"
branch: "master"
tag: "ml"
commit: "513caf3e5d1d418c779f0c670ed4dc99002aa36c"
version: "66d6edd0de91490f7319b183eb4b2350226fa86169f6bb5893d6e2e43ce74754"
build_date: "2021-01-22T04:54:14.457Z"
size_mb: 4875.0
size: 5111808000
sif: "https://datasets.datalad.org/shub/fzimmermann89/Singularity/ml/2021-01-22-513caf3e-66d6edd0/66d6edd0de91490f7319b183eb4b2350226fa86169f6bb5893d6e2e43ce74754.sif"
url: https://datasets.datalad.org/shub/fzimmermann89/Singularity/ml/2021-01-22-513caf3e-66d6edd0/
recipe: https://datasets.datalad.org/shub/fzimmermann89/Singularity/ml/2021-01-22-513caf3e-66d6edd0/Singularity
collection: fzimmermann89/Singularity
---

# fzimmermann89/Singularity:ml

```bash
$ singularity pull shub://fzimmermann89/Singularity:ml
```

## Singularity Recipe

```singularity
bootstrap: docker
from: nvidia/cuda:10.2-devel-centos7




%help
Centos7 with conda python, jupyter, cuda




%environment
CUDA_ROOT=/usr/local/cuda
export CUDA_ROOT
SINGULARITY_SHELL=/bin/zsh
export SINGULARITY_SHELL
PATH=$PATH:/opt/anaconda3/bin:/usr/local/cuda/bin
export PATH


%post
##yum
yum -y install epel-release https://repo.ius.io/ius-release-el7.rpm && yum update -y && yum upgrade -y
yum install -y aria2 bsdtar curl git224 gzip lz4 p7zip p7zip-plugins perl-Digest-MD5 perl-File-Fetch perl-LWP-Protocol-https perl-Mozilla-CA perl-libwww-perl rsync unzip wget xz zip
yum install -y axel binutils cmake curl diffutils elfutils environment-modules gcc gcc-c++ gdb gettext ghostscript htop less libstdc++ libtiff libtool ltrace make man man-pages mc mosh openmpi-devel openssh patch patchutils perf psmisc screen strace tmux vim zsh && yum clean all && rm -rf /var/cache/yum &



#miniconda
echo "installing miniconda"
wget -q -O /tmp/Miniconda3.sh https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh
cd /tmp/&& bash /tmp/Miniconda3.sh -b -p /opt/anaconda3
rm /tmp/Miniconda3.sh
ln -s /opt/anaconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh
PATH=$PATH:/usr/local/cuda/bin:/opt/anaconda3/bin


#conda env
. /etc/profile.d/conda.sh
echo "installing conda extensions"
conda activate
conda install -q -y -c conda-forge mamba
mamba install -q -y  pillow  seaborn "numpy>1.18" hdf5 h5py colorama "jupyterlab>=2.2.6,<3" ipython memory_profiler isort mkl-devel fastrlock six setuptools scikit-learn scipy seaborn pandas line_profiler black matplotlib "python>=3.7" scikit-image
mamba install -q -y -c pkgs -c pytorch -c nvidia -c conda-forge "pytorch>=1.4" "torchvision>=0.5" torchaudio cudatoolkit=10 "tensorflow-gpu>=2" cupy numba lmfit ipympl pathos "nodejs>=14"  ptvsd xeus-python pytools nbdime "pip>=20.3" jupyter-dash ipyvolume jupyter-server-proxy six openssl "jupyterlab>=2.2.6,<3"
conda clean -a -y &


#jupyterlab extensions
echo "installing jlab extensions"

jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install ipyvolume --no-build
jupyter labextension install jupyter-threejs --no-build
jupyter labextension install @krassowski/jupyterlab_go_to_definition --no-build
jupyter labextension install @aquirdturtle/collapsible_headings --no-build
jupyter labextension install @jupyterlab/google-drive --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install @jupyterlab/server-proxy --no-build

pip install -q jupyterlab-git "jupyterlab_code_formatter<1.4"   jupyter-dash jupyter-tensorboard "jupyterlab<3"
jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build
jupyter labextension install @jupyterlab/git --no-build
jupyter labextension install @jupyterlab/debugger --no-build
jupyter labextension install  jupyterlab-dash --no-build
jupyter labextension install jupyterlab_tensorboard --no-build
jupyter serverextension enable --py jupyterlab_code_formatter --sys-prefix
jupyter serverextension enable --py jupyterlab_git --sys-prefix
jupyter serverextension enable --py jupyter_server_proxy --sys-prefix
jupyter serverextension enable --py nbdime --sys-prefix
jupyter serverextension enable jupyter_tensorboard --user

echo 'waiting'

sleep 10
wait #make sure not to run out of memory
sleep 30

echo 'building lab'
jupyter lab build --dev-build=False ||true
cat /tmp/jupyterlab-debug-* ||true

cat > /opt/anaconda3/etc/jupyter/jupyter_config.json << "EOF3"
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyterlab_git": true,
      "jupyterlab": true,
      "jupyter_tensorboard": true,
      "nbdime": true,
      "jupyterlab_code_formatter": true,
      "jupyter_server_proxy": true
    }
  }
}
EOF3


#pip
#echo "installing pycuda from pip" && LIBRARY_PATH=/usr/local/cuda/lib64/stubs CPATH=/usr/local/cuda/include CUDA_ROOT=/usr/local/cuda pip install pycuda && \
#echo 'installing cupy from pip' && pip install cupy-cuda101  &

#conda config
conda config  --file /opt/anaconda3/.condarc --set changeps1 False
conda config  --file /opt/anaconda3/.condarc --set auto_activate_base true

cat > /etc/profile.d/zconda.sh << "EOF1"
#. /etc/profile.d/conda.sh
conda activate
EOF1

cat > /opt/runscript.sh << "EOF2"
#!/bin/bash
. /etc/profile.d/conda.sh
conda activate
exec "$@"
EOF2
chmod +x /opt/runscript.sh


#cleanup
wait
conda clean -a -y
pip cache purge
rm -rf /root/.conda
rm -rf /root/.npm
rm -rf /root/.cache
rm -rf /tmp/npm*
rm -rf /tmp/yarn*
rm -rf /var/cache/*
echo '####ALL DONE####'




%labels
    Maintainer zimmf
    Version 0.1-201111
        
%runscript
exec /opt/runscript.sh python "$@"

%startscript
exec /opt/runscript.sh jupyter lab "$@"

%apprun jupyter
exec /opt/runscript.sh jupyter "$@"

%apprun ipython
exec /opt/runscript.sh ipython "$@"
```

## Collection

 - Name: [fzimmermann89/Singularity](https://github.com/fzimmermann89/Singularity)
 - License: None

