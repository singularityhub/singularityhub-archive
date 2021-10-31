---
id: 3365
name: "whit2333/cool_halls"
branch: "master"
tag: "latest"
commit: "b97193fca7df854a4f82fc10310ba6c0e9e2c0f7"
version: "e2909d8ee4d0eab091e6ef08e4c709df"
build_date: "2019-02-09T23:03:26.675Z"
size_mb: 3229
size: 1128701983
sif: "https://datasets.datalad.org/shub/whit2333/cool_halls/latest/2019-02-09-b97193fc-e2909d8e/e2909d8ee4d0eab091e6ef08e4c709df.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/whit2333/cool_halls/latest/2019-02-09-b97193fc-e2909d8e/
recipe: https://datasets.datalad.org/shub/whit2333/cool_halls/latest/2019-02-09-b97193fc-e2909d8e/Singularity
collection: whit2333/cool_halls
---

# whit2333/cool_halls:latest

```bash
$ singularity pull shub://whit2333/cool_halls:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: docker://whit2333/cool_halls

%labels
  Maintainer "Whitney Armstrong"
  Version v0.3.2

%help
  Cool (A/C) hall's software container
    Libraries and tools:
     - evio        : EVIO DAQ data format    https://github.com/whit2333/hallac_evio
     - analyzer    : Hall A analyzer (podd)  https://github.com/whit2333/analyzer
     - hcana       : Hall C analyzer (hcana) https://github.com/whit2333/hcana
     - hallc_tools : Hall C analyzer (hcana) https://github.com/whit2333/hallc_tools

%setup -c /bin/bash
  export SINGULARITY_SHELL=/bin/bash
  #ls -lrth /usr/local/bin
  #/bin/bash "$@"

%post -c /bin/bash
  source /usr/local/bin/thisroot.sh
  echo "Hello from inside the container"
  echo "Install additional software here"

%environment
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include:/usr/local/include/podd:/usr/local/include/hcana
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
# analyzer
# =======================
%apprun analyzer
  analyzer "$@"

%appenv analyzer
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh

# =======================
# hcana
# =======================
%apphelp hcana
  Run the Hall-C analyzer with same root-style arguments.

%apprun hcana
  hcana "$@"

%appenv hcana
  export DB_DIR=DBASE
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOTSYS=/usr/local
  export ROOT_INCLUDE_PATH=/usr/local/include
  #source /usr/local/bin/thisroot.sh

# =======================
# root-config
# =======================
%apprun root-config
  #source /usr/local/bin/thisroot.sh
  root-config "$@"

%appenv root-config
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh


# =======================
# rootbrowse
# =======================
%apprun rootbrowse
  #source /usr/local/bin/thisroot.sh
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
  #source /usr/local/bin/thisroot.sh
  rootls "$@"

%appenv rootls
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include/podd:/usr/local/include/hcana
  #source /usr/local/bin/thisroot.sh
```

## Collection

 - Name: [whit2333/cool_halls](https://github.com/whit2333/cool_halls)
 - License: None

