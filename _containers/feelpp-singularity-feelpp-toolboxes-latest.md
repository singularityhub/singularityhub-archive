---
id: 822
name: "feelpp/singularity"
branch: "master"
tag: "feelpp-toolboxes-latest"
commit: "19ffe87e2a2dc606b32c78824926208c81f75f7c"
version: "c6ceb1e37c89a287b2fb202bd64fc5b6"
build_date: "2019-09-17T07:15:39.750Z"
size_mb: 9766
size: 3124617247
sif: "https://datasets.datalad.org/shub/feelpp/singularity/feelpp-toolboxes-latest/2019-09-17-19ffe87e-c6ceb1e3/c6ceb1e37c89a287b2fb202bd64fc5b6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/feelpp/singularity/feelpp-toolboxes-latest/2019-09-17-19ffe87e-c6ceb1e3/
recipe: https://datasets.datalad.org/shub/feelpp/singularity/feelpp-toolboxes-latest/2019-09-17-19ffe87e-c6ceb1e3/Singularity
collection: feelpp/singularity
---

# feelpp/singularity:feelpp-toolboxes-latest

```bash
$ singularity pull shub://feelpp/singularity:feelpp-toolboxes-latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: feelpp/feelpp-toolboxes:latest

%help
USAGE: feelpp_<appname> --config-file <cfgfile>

    Applications are installed in "/usr/local/bin" and prefixed with
    "feelpp_<appname>". All testcases with their configuration files
    are available in the container under "/opt/feelpp/" directory.

NOTES:

    1) This image is read-only! You might want to copy in you home
       directory from the container
       $ cp -r /opt/feelpp ~/

    2) (If necessary) to edit the image, create your own image to
       based on this image adding write access
       $ singularity build --writable <thisimage> myimage.img


EXAMPLES:
    List availailable apps
	$ singularity apps <image-name>

    Run an application (demo):
        $ singularity run --app demo <image-name>

    Sequential run:
	$ singularity exec <image-name> feelpp_qs_laplacian_2d

    Parallel run:
	$ mpirun -np 4 singularity exec <image-name> feelpp_qs_laplacian_2d

    Toolbox run (CSM):
	$ singularity exec <image-name> feelpp_toolbox_solid_3d --config-file \
	$     /opt/feelpp/Testcases/CSM/torsionbar/torsionbar.cfg

SEE ALSO:

    - www.feelpp.org                         Feel++ website
    - book.feelpp.org                        Feel++ documentation
    - https://github.com/feelpp/feelpp       Feel++ sources and issues
    - https://github.com/feelpp/singularity  Feel++ singularity sources
                                             and issues

%labels
    Maintainer: Guillaume Dollé
    Maintainer_email: guillaume.dolle@cemosis.fr
    Version 1.1
    License: LGPLv2.1

%files
    singularity.d/env/99-feelpp_env.sh /.singularity.d/env/

%setup
    echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
    if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
        echo "Hrmm, this container does not have /bin/sh installed..."
        exit 1
    fi
    exit 0

%post
    echo "Post install"
    sed -i 's/.*PS1 *=.*//g' /etc/bash.bashrc
    sed -i 's/.*PS1 *=.*//g' /.singularity.d/actions/shell
    sed -i 's/.*PS1 *=.*//g' /.singularity.d/env/99-base.sh
    sed -i 's/.*HOME *=.*//g' /.singularity.d/env/10-docker.sh
    mkdir -p /feel
    chmod 777 /feel
    mv /home/feelpp /opt/feelpp
    userdel feelpp
    chown -R root:root /opt/feelpp
    chmod -R 777 /opt/feelpp
    
    # Clean temporary files. 
    rm -rf `find /opt/feelpp -name ".*" ! -path .`

    echo "alias ls='ls --color=auto'" >> /etc/bash.bashrc
    echo "alias ll='ls -ls'" >> /etc/bash.bashrc
    echo "alias grep='grep --color'" >> /etc/bash.bashrc

    PACKAGES="dapl2-utils libdapl-dev libdapl2 libibverbs1 librdmacm1 libcxgb3-1 libipathverbs1 libmlx4-1 libmlx5-1 libmthca1 libnes1 libpmi0 libpmi0-dev"
    apt-get update
    apt-get -y --allow-unauthenticated install $PACKAGES

    exit 0

%runscript
    echo "type: singularity help <image-name>"
    #echo "Arguments received: $*"
    #exec /usr/bin/python "$@"


%startscript
    echo "Start script exec"

    if [ -d /feel/crbdb ]; then
        service mongodb start
        if [ -d /feel/crbdb/mongodb ]; then
            /usr/lib/juju/mongo3.2/bin/mongorestore /feel/crbdb/mongodb
        fi
    fi

%test
    # Section that should be updated with ctest.
    feelpp_qs_laplacian_2d --config-file=/opt/feelpp/Testcases/quickstart/laplacian/circle/circle-all.cfg --checker.tolerance.exact=5.e-14

%environment
    white=`tput setaf 7`
    cyan=`tput setaf 6`
    reset=`tput sgr0`
    bold=`tput bold`
    escleft="\[" # `if [ "${SHELL##*/}" == "bash" ]; then echo '\['; fi`
    escright="\]" #`if [ "${SHELL##*/}" == "bash" ]; then echo '\]'; fi`
    USER=`id -un`
    HOSTNAME=`hostname`
    
    SINGULARITY_SHELL=bash
    FEELPP_TUTORIAL=/opt/feelpp
    PS1="${escleft}${bold}${white}${escright}[singularity]:${escleft}${cyan}${escright} ${USER}@${HOSTNAME}${escleft}${reset}${escright}:\w> "

    LD_LIBRARY_PATH=${FEELPP_DEP_INSTALL_PREFIX}/lib:${FEELPP_DEP_INSTALL_PREFIX}/lib/paraview-5.3:$LD_LIBRARY_PATH
    PKG_CONFIG_PATH=${FEELPP_DEP_INSTALL_PREFIX}/lib/pkgconfig:$PKG_CONFIG_PATH
    PYTHONPATH=${FEELPP_DEP_INSTALL_PREFIX}/lib/python2.7/site-packages:${FEELPP_DEP_INSTALL_PREFIX}/lib/paraview-5.3/site-packages:$PYTHONPATH
    MANPATH=${FEELPP_DEP_INSTALL_PREFIX}/share/man:$MANPATH

%apprun demo
    APP1=`which feelpp_qs_laplacian_2d`
    APP2=`which feelpp_mesh_partitioner`
    VIEWER=`which paraview`
    NP=2
    export FEELPP_REPOSITORY=${HOME}/feel/singularity
    if [ ! -z "${APP1}" ]; then
        echo "Running Feel++ demonstration 'qs_laplacian_2d' with paraview visualisation on 2 cores."
        mpirun -np $NP feelpp_qs_laplacian_2d --config-file=/opt/feelpp/Testcases/quickstart/laplacian/circle/circle-all.cfg --checker.tolerance.exact=5.e-14
        if [ ! -z "${VIEWER}" ]; then
            paraview ${FEELPP_REPOSITORY}/qs_laplacian/circle-all/np_${NP}/exports/ensightgold/qs_laplacian/qs_laplacian.case
        fi
    else
        echo "Nothing to show for this image!"
    fi
```

## Collection

 - Name: [feelpp/singularity](https://github.com/feelpp/singularity)
 - License: None

