---
id: 4178
name: "whit2333/topside_containers"
branch: "master"
tag: "topside"
commit: "120fecd3553218bc4a8afd8b211a72733ff47889"
version: "cf76ecd0bcad09554092b158fca48e1b"
build_date: "2018-08-24T05:04:46.892Z"
size_mb: 5530
size: 1893126175
sif: "https://datasets.datalad.org/shub/whit2333/topside_containers/topside/2018-08-24-120fecd3-cf76ecd0/cf76ecd0bcad09554092b158fca48e1b.simg"
url: https://datasets.datalad.org/shub/whit2333/topside_containers/topside/2018-08-24-120fecd3-cf76ecd0/
recipe: https://datasets.datalad.org/shub/whit2333/topside_containers/topside/2018-08-24-120fecd3-cf76ecd0/Singularity
collection: whit2333/topside_containers
---

# whit2333/topside_containers:topside

```bash
$ singularity pull shub://whit2333/topside_containers:topside
```

## Singularity Recipe

```singularity
bootstrap: docker
From: docker://argonneeic/topside

%labels
  Maintainer "Whitney Armstrong"
  Version v0.2.2

%help
  Todo

%setup -c /bin/bash
  export SINGULARITY_SHELL=/bin/bash
  #ls -lrth /usr/local/bin
  #whoami
  #/bin/bash "$@"
  #root-config --version

%post -c /bin/bash
  source /usr/local/bin/thisroot.sh
  echo "Hello from inside the container"
  echo "Install additional software here"

%environment
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include:/usr/local/include/podd:/usr/local/include/hcana
  export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]singularity\$'

  #source /usr/local/bin/thisroot.sh

# =======================
# global
# =======================

%runscript
  echo "You are running Cool Halls singularity container "
#  source /usr/local/bin/thisroot.sh
#  /bin/bash "$@"
#%runscript
#  #echo "This is what happens when you run the container..."
#  derp=
#  if [ -p /dev/stdin ]; then
#    # If we want to read the input line by line
#    while IFS= read line; do
#      #echo "Line: ${line}"
#      if [ -z ${derp} ]; then
#        derp="${line}"
#      else 
#        derp="${derp}\n${line}"
#      fi
#    done
#  fi
#  /bin/bash <<EOF
#  source /usr/local/bin/geant4.sh
#  echo -e ${derp} | bubble_chamber $@
#EOF
#  #exec /usr/local/bin/run_bubble_sim "$@"



# =======================
# root
# =======================
%apprun root
  root "$@"

%appenv root
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh

# =======================
# root-config
# =======================
%apprun root-config
  source /usr/local/bin/thisroot.sh
  root-config "$@"

%appenv root-config
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  source /usr/local/bin/thisroot.sh


# =======================
# rootbrowse
# =======================
%apprun rootbrowse
  source /usr/local/bin/thisroot.sh
  rootbrowse "$@"

%appenv rootbrowse
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh

# =======================
# rootls
# =======================
%apprun rootls
  source /usr/local/bin/thisroot.sh
  rootls "$@"

%appenv rootls
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh
```

## Collection

 - Name: [whit2333/topside_containers](https://github.com/whit2333/topside_containers)
 - License: None

