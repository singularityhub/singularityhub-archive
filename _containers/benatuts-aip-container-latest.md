---
id: 10286
name: "benatuts/aip-container"
branch: "master"
tag: "latest"
commit: "142c29dabc54b9d2846bafd2d67bb42d2ca71b03"
version: "8a6f771c659bb180460a7c195969b5c7"
build_date: "2019-08-15T12:03:49.189Z"
size_mb: 1304.0
size: 452710431
sif: "https://datasets.datalad.org/shub/benatuts/aip-container/latest/2019-08-15-142c29da-8a6f771c/8a6f771c659bb180460a7c195969b5c7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/benatuts/aip-container/latest/2019-08-15-142c29da-8a6f771c/
recipe: https://datasets.datalad.org/shub/benatuts/aip-container/latest/2019-08-15-142c29da-8a6f771c/Singularity
collection: benatuts/aip-container
---

# benatuts/aip-container:latest

```bash
$ singularity pull shub://benatuts/aip-container:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: ubuntu:latest

%labels
    MAINTAINER benjamin.johnston
    VERSION 2019.SPR.1

%help
A singularity container for NodeJS, SQLite3, MongoDB and VS Code web development.

This is used for the subject Advanced Internet Programming (AIP) at UTS.

To rebuild the container using your own computer:

sudo singularity build aip-container_latest.sif Singularity
Or, you can pull the pre-built image from Singularity Hub to your own computer:

singularity pull shub://benatuts/aip-container

How to use:
# Start a gnome-terminal-server and gnome-terminal
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app fullterm -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF
# Start a gnome-terminal
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app term -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF
# Start visual studio code
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app vscode -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF

NOTE:
1. $SINGULARITYENV_HOST_PATH is just a path where you want to be bind as $HOME in your container.
2. You will need to have GNOME session to run the above apps from the AIP containter.

%environment
    export PATH=/usr/local/bin:$PATH
    export LANG=en_US.UTF-8

%post
    apt update -y

    # Create a fairly sensible environment
    DEBIAN_FRONTEND=noninteractive apt install -y gnupg2 dirmngr curl wget lsb-release vim nano net-tools ubuntu-standard tzdata zip unzip
    DEBIAN_FRONTEND=noninteractive apt install -y language-pack-en locales
    locale-gen en_US.UTF-8

    # Run GUI apps in the container
    DEBIAN_FRONTEND=noninteractive apt install -y gnome-terminal gedit libcanberra-gtk-module libcanberra-gtk3-module libasound2 zenity

    # Setup the NodeJS package database
    curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
    echo "deb https://deb.nodesource.com/node_10.x $(lsb_release -s -c) main" | tee /etc/apt/sources.list.d/nodesource.list

    # Setup the MongoDB package database
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
    echo "deb https://repo.mongodb.org/apt/ubuntu $(lsb_release -s -c)/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list

    # Web development tools
    apt update -y
    DEBIAN_FRONTEND=noninteractive apt install -y git nodejs mongodb-org sqlite3 apache2-utils

    # Visual Studio Code
    curl -L https://go.microsoft.com/fwlink/?LinkID=760868 --out vscode.deb
    DEBIAN_FRONTEND=noninteractive apt install -y ./vscode.deb
    rm vscode.deb
    
    apt clean

%apprun term
    gnome-terminal --app-id aip.Terminal --wait

%apprun fullterm
    (/usr/lib/gnome-terminal/gnome-terminal-server --app-id aip.Terminal &) && (sleep 0.4; gnome-terminal  --app-id aip.Terminal --wait)

%apprun vscode
    code

%runscript
echo '
A singularity container for NodeJS, SQLite3, MongoDB and VS Code web development.

This is used for the subject Advanced Internet Programming (AIP) at UTS.

To rebuild the container using your own computer:

sudo singularity build aip-container_latest.sif Singularity
Or, you can pull the pre-built image from Singularity Hub to your own computer:

singularity pull shub://benatuts/aip-container

How to use:
# Start a gnome-terminal-server and gnome-terminal
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app fullterm -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF
# Start a gnome-terminal
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app term -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF
# Start visual studio code
    SINGULARITYENV_HOST_PATH=/tmp/$USER; singularity run --app vscode -B $HOME:/host$HOME -H "$SINGULARITYENV_HOST_PATH":$HOME -B /run --pwd $HOME $SIF

NOTE:
1. $SINGULARITYENV_HOST_PATH is just a path where you want to be bind as $HOME in your container.
2. You will need to have GNOME session to run the above apps from the AIP containter.

'
```

## Collection

 - Name: [benatuts/aip-container](https://github.com/benatuts/aip-container)
 - License: None

