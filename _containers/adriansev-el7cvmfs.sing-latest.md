---
id: 12616
name: "adriansev/el7cvmfs.sing"
branch: "master"
tag: "latest"
commit: "e39656aef72d6f065f4e6f5a47a9707eb10f18ac"
version: "5c5d65cc8431edc48ab1dd8af7da1c47e3bf6afaa28aaa03af4cd848adf1df4f"
build_date: "2021-04-14T19:20:55.974Z"
size_mb: 364.453125
size: 382156800
sif: "https://datasets.datalad.org/shub/adriansev/el7cvmfs.sing/latest/2021-04-14-e39656ae-5c5d65cc/5c5d65cc8431edc48ab1dd8af7da1c47e3bf6afaa28aaa03af4cd848adf1df4f.sif"
url: https://datasets.datalad.org/shub/adriansev/el7cvmfs.sing/latest/2021-04-14-e39656ae-5c5d65cc/
recipe: https://datasets.datalad.org/shub/adriansev/el7cvmfs.sing/latest/2021-04-14-e39656ae-5c5d65cc/Singularity
collection: adriansev/el7cvmfs.sing
---

# adriansev/el7cvmfs.sing:latest

```bash
$ singularity pull shub://adriansev/el7cvmfs.sing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: adriansevcenco/el7cvmfs:latest

%labels
    Author Adrian.Sevcenco@spacescience.ro
    Version 0.0.1
    Description Minimal el7, HEP_OSlibs + cvmfs (configs: default+egi+osg) container


%help
Generic HEP oriented container (it includes HEP_OSlibs dependency list)
that allows mounting of CVMFS repositories without any host requirement.
The proxies are defined as generic PAC urls, with fallback to DIRECT.
CVMFS configuration is the merge of cvmfs-config-default cvmfs-config-egi cvmfs-config-osg
The container can be pre-setup by the usage of files prefixed with CVMFS2GO_EXEC_ or CVMFS2GO_LOAD_
that are searched in the current directory and in $HOME (if not found in cwd).
If given as 1st argument a name prefixed with CVMFS2GO_LOAD_ the name will be sourced before running a command or starting the shell
If given as 1st argument a name prefixed with CVMFS2GO_EXEC_ the first line of name file will be exec'ed
If given as 1st argument a name prefixed with CVMFS2GO_RUN_ the first line of name file will be exec'ed
The default is either run the argument list or just start bash

%runscript
ARG="${1}"

if [[ ${ARG} == CVMFS2GO_LOAD_*  ]]; then
    shift
    NAME=$(echo "${ARG}" | sed 's/CVMFS2GO_LOAD_//')
    # check existence of file in current dir then in $HOME
    [[ -e ./${NAME} ]] && APPFILE="./${NAME}"
    [[ -z "${APPFILE}" ]] && [[ -e ${HOME}/${NAME} ]] && APPFILE="${HOME}/${NAME}"
    [[ -n "${APPFILE}" ]] && source "${APPFILE}"
fi

# we start an application specified by CVMFS2GO_EXEC_ prefix
if [[ ${ARG} == CVMFS2GO_EXEC_*  ]]; then
    DO_EXEC=1
    shift
    NAME=$(echo "${ARG}" | sed 's/CVMFS2GO_EXEC_//')
    # check existence of file in current dir then in $HOME
    [[ -e ./${NAME} ]] && APPFILE="./${NAME}"
    [[ -z "${APPFILE}" ]] && [[ -e ${HOME}/${NAME} ]] && APPFILE="${HOME}/${NAME}"
    [[ -n "${APPFILE}" ]] && exec "$(head -1 ${APPFILE})" "${@}"
elif [[ ${ARG} == CVMFS2GO_RUN_* ]]; then
    DO_EXEC=1
    shift
    NAME=$(echo "${ARG}" | sed 's/CVMFS2GO_RUN_//')
    # check existence of file in current dir then in $HOME
    [[ -e ./${NAME} ]] && APPFILE="./${NAME}"
    [[ -z "${APPFILE}" ]] && [[ -e ${HOME}/${NAME} ]] && APPFILE="${HOME}/${NAME}"
    [[ -n "${APPFILE}" ]] && /usr/bin/bash -lc "${APPFILE} ${@}"
fi
[[ -n ${DO_EXEC} ]] && exit

if [[ -n "${@}" ]]; then  # if we have arguments string
  exec bash -lc "${@}"  # just run the command+args
else
  exec bash -li
fi
```

## Collection

 - Name: [adriansev/el7cvmfs.sing](https://github.com/adriansev/el7cvmfs.sing)
 - License: None

