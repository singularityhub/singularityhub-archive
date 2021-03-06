---
id: 15301
name: "fzimmermann89/idi"
branch: "master"
tag: "py38"
commit: "70127b8d883b8b1e6d6671503397fc5cf37f82d8"
version: "4dae3a1276088665e6c940e2b3b4a882489375a77d2dd7774b1df85ce1cfd170"
build_date: "2021-01-25T14:57:55.946Z"
size_mb: 3956.5
size: 4148690944
sif: "https://datasets.datalad.org/shub/fzimmermann89/idi/py38/2021-01-25-70127b8d-4dae3a12/4dae3a1276088665e6c940e2b3b4a882489375a77d2dd7774b1df85ce1cfd170.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fzimmermann89/idi/py38/2021-01-25-70127b8d-4dae3a12/
recipe: https://datasets.datalad.org/shub/fzimmermann89/idi/py38/2021-01-25-70127b8d-4dae3a12/Singularity
collection: fzimmermann89/idi
---

# fzimmermann89/idi:py38

```bash
$ singularity pull shub://fzimmermann89/idi:py38
```

## Singularity Recipe

```singularity
bootstrap: docker
from: nvidia/cuda:10.2-devel-centos7




%help
Centos7 with conda python, jupyter, latex, cuda




%environment
CUDA_ROOT=/usr/local/cuda
export CUDA_ROOT
SINGULARITY_SHELL=/bin/zsh
export SINGULARITY_SHELL
MKLROOT=/opt/intel/compilers_and_libraries/linux/mkl
export MKLROOT
TBBROOT=/opt/intel/compilers_and_libraries/linux/tbb
export TBBROOT
INTEL_LICENSE_FILE=/opt/intel/compilers_and_libraries/linux/licenses
export INTEL_LICENSE_FILE
LIBRARY_PATH=$LIBRARY_PATH:/opt/intel/compilers_and_libraries/linux/compiler/lib/intel64_lin:/opt/intel/compilers_and_libraries/linux/mkl/lib/intel64_lin:/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.8:/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.8
export LIBRARY_PATH
CPATH=$CPATH:/opt/intel/compilers_and_libraries/linux/mkl/include:/opt/intel/compilers_and_libraries/linux/tbb/include:/opt/intel/compilers_and_libraries/linux/tbb/include
export CPATH
PATH=$PATH:/opt/anaconda3/bin:/usr/local/texlive/bin/x86_64-linux:/usr/local/cuda/bin
PATH=$PATH:/opt/intel/compilers_and_libraries/linux/bin/intel64:/opt/intel/compilers_and_libraries/linux/bin
export PATH
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/intel/compilers_and_libraries/linux/mkl/bin/pkgconfig
export PKG_CONFIG_PATH
LD_PRELOAD=/usr/local/lib64/mklpatch.so
export LD_PRELOAD
SHELL=/usr/bin/zsh
export SHELL




%post
##yum
yum-config-manager --add-repo https://yum.repos.intel.com/mkl/setup/intel-mkl.repo
yum -y install epel-release https://repo.ius.io/ius-release-el7.rpm && yum update -y && yum upgrade -y
yum install -y aria2 bsdtar curl git224 gzip lz4 p7zip p7zip-plugins perl-Digest-MD5 perl-File-Fetch perl-LWP-Protocol-https perl-Mozilla-CA perl-libwww-perl rsync unzip wget xz zip
#intel-mkl-64bit-2020.3-111.x86_64 intel-mkl-gnu-2020.3-279.x86_64 intel-mkl-tbb-rt-2020.3-279.x86_64 
yum install -y axel binutils cmake curl diffutils elfutils environment-modules file gcc gcc-c++ gdb gettext ghostscript htop less libstdc++ libtiff libtool ltrace make man man-pages mc mosh openmpi-devel openssh patch patchutils perf psmisc screen strace tmux vim zsh  openssl openssl-devel pam-devel numactl numactl-devel hwloc hwloc-devel lua lua-devel readline-devel rrdtool-devel ncurses-devel man2html libibmad libibumad munge-libs && yum clean all && rm -rf /var/cache/yum &


##texlive
echo "installing texlive"
cat > /tmp/texlive.profile << "EOF0"
# texlive.profile
selected_scheme scheme-custom
collection-basic 1
collection-bibtexextra 1
collection-context 0
collection-fontsextra 1
collection-fontsrecommended 1
collection-fontutils 1
collection-formatsextra 1
collection-humanities 1
collection-langenglish 1
collection-langfrench 1
collection-langgerman 1
collection-langgreek 1
collection-latex 1
collection-latexextra 1
collection-latexrecommended 1
collection-luatex 1
collection-mathscience 1
collection-metapost 1
collection-pictures 1
collection-plaingeneric 1
collection-pstricks 1
collection-publishers 1
collection-xetex 1
TEXDIR /usr/local/texlive/
TEXMFCONFIG ~/.texlive/texmf-config
TEXMFHOME ~/.texlive/texmf
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSCONFIG /usr/local/texlive/texmf-config
TEXMFSYSVAR /usr/local/texlive/texmf-var
TEXMFVAR ~/.texlive/texmf-var
binary_x86_64-linux 1
instopt_adjustpath 0
instopt_adjustrepo 1
instopt_letter 0
instopt_portable 0
instopt_write18_restricted 1
tlpdbopt_autobackup 0
tlpdbopt_backupdir tlpkg/backups
tlpdbopt_create_formats 1
tlpdbopt_desktop_integration 1
tlpdbopt_file_assocs 1
tlpdbopt_generate_updmap 0
tlpdbopt_install_docfiles 0
tlpdbopt_install_srcfiles 0
tlpdbopt_post_code 1
tlpdbopt_sys_bin /usr/local/bin
tlpdbopt_sys_info /usr/local/share/info
tlpdbopt_sys_man /usr/local/share/man
tlpdbopt_w32_multi_user 1
EOF0

#mounting iso (not possible on shub)
#cd /tmp && aria2c -q -j8 -x8 http://mirror.ctan.org/systems/texlive/Images/texlive2020.iso && mkdir /mnt/iso &&  mount -o loop /tmp/texlive2020.iso /mnt/iso && cd /mnt/iso && ./install-tl -profile /tmp/texlive.profile -no-verify-downloads -persistent-downloads  && sleep 60 &&  umount /mnt/iso || true && rm -f /tmp/texlive2020.iso && echo 'done' &

#unpacking iso (can cause checksum fails?)
#cd /tmp && aria2c -q -j8 -x8 http://mirror.ctan.org/systems/texlive/Images/texlive2020.iso && mkdir /tmp/iso &&  bsdtar -xf texlive2020.iso -C /tmp/iso && rm /tmp/texlive2020.iso && cd /tmp/iso && ./install-tl -profile /tmp/texlive.profile -no-verify-downloads -persistent-downloads -q &&  rm /tmp/texlive2020.iso && rm -rf /tmp/iso && echo 'done' &

#online install
wget -q -O /tmp/install-tl-unx.tar.gz http://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    cd /tmp/ && tar xzf install-tl-unx.tar.gz && \
    cd /tmp/install-tl-* && ./install-tl -profile /tmp/texlive.profile -no-verify-downloads -persistent-downloads -q && \
    rm -rf /tmp/install-tl* && echo 'tl install done' &


#miniconda
echo "installing miniconda"
wget -q -O /tmp/Miniconda3.sh https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh
cd /tmp/&& bash /tmp/Miniconda3.sh -b -p /opt/anaconda3
rm /tmp/Miniconda3.sh
ln -s /opt/anaconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh
PATH=$PATH:/usr/local/cuda/bin:/opt/anaconda3/bin


#conda env
. /etc/profile.d/conda.sh
echo "installing conda extensions"
conda activate
conda install -q -y -c conda-forge mamba conda
mamba install -q -y simplejson colorama   protobuf requests "numexpr>=2.7.2" "numpy>=1.17" hdf5 scipy "jedi=0.17" numba mkl cython  "jupyterlab=2.2"  jupyter scikit-image appdirs mako scikit-learn "python>=3.8" seaborn pandas line_profiler black ninja colorama memory_profiler isort mkl-devel fastrlock six setuptools
mamba install -q -y -c anaconda -c  conda-forge -c plotly gpustat colorful "h5py>3" lmfit ipympl pathos "nodejs>=14"  ptvsd xeus-python pytools nbdime "pip>=20.1" jupyter-dash ipyvolume jupyter-server-proxy six openssl
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

pip install -q --upgrade jupyterlab-git "jupyterlab_code_formatter<1.4"  jupyterlab_latex jupyter-dash "jupyterlab<3" jupyterlab_hdf
jupyter labextension install @jupyterlab/latex --no-build
jupyter labextension install "@ryantam626/jupyterlab_code_formatter@<1.4" --no-build
jupyter labextension install @jupyterlab/git --no-build
jupyter labextension install @jupyterlab/debugger --no-build
jupyter labextension install  jupyterlab-dash --no-build
jupyter labextension install jupyterlab-tabular-data-editor
jupyter labextension install @jupyterlab/hdf5
jupyter serverextension enable --py jupyterlab_code_formatter --sys-prefix
jupyter serverextension enable --sys-prefix jupyterlab_latex
jupyter serverextension enable --py jupyterlab_git --sys-prefix
jupyter serverextension enable --py jupyter_server_proxy --sys-prefix
jupyter serverextension enable --py nbdime --sys-prefix
jupyter serverextension enable --py jupyterlab_hdf --sys-prefix

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
      "jupyterlab_hdf": true,
      "jupyterlab": true,
      "jupyterlab_latex": true,
      "nbdime": true,
      "jupyterlab_code_formatter": true,
      "jupyter_server_proxy": true
    }
  }
}
EOF3


#pip
echo "installing pycuda from pip" && LIBRARY_PATH=/usr/local/cuda/lib64/stubs CPATH=/usr/local/cuda/include CUDA_ROOT=/usr/local/cuda pip install pycuda && \
echo 'installing cupy from pip' && pip install cupy-cuda102  &

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


#patch for mkl
echo 'compiling mkl patch'
cat > /tmp/mklpatch.c << "EOF4"
//https://danieldk.eu/Posts/2020-08-31-MKL-Zen.html
int mkl_serv_intel_cpu_true() {
  return 1;
}
EOF4
gcc -shared -fPIC -o /tmp/mklpatch.so /tmp/mklpatch.c
cp /tmp/mklpatch.so /usr/local/lib64/mklpatch.so && chmod 775 /usr/local/lib64/mklpatch.so && echo 'done'



#idi
wait
echo 'install idi' && pip install git+https://github.com/fzimmermann89/idi


#cleanup
wait
conda clean -a -y
pip cache purge
rm -rf /root/.conda
rm -rf /root/.npm
rm -rf /root/.cache
rm -rf /tmp/npm*
rm -rf /tmp/texlive*
rm -rf /tmp/yarn*
rm -rf /var/cache/*
echo '####ALL DONE####'

#slurm user
useradd -r --shell /usr/sbin/nologin slurm


%labels
    Maintainer zimmf
    Version 0.1-200910
        
%runscript
exec /opt/runscript.sh python "$@"

%startscript
exec /opt/runscript.sh jupyter lab "$@"

%apprun jupyter
exec /opt/runscript.sh jupyter "$@"

%apprun ipython
exec /opt/runscript.sh ipython "$@"

%apprun pdftex
exec pdftex "$@"
```

## Collection

 - Name: [fzimmermann89/idi](https://github.com/fzimmermann89/idi)
 - License: None

