---
id: 3594
name: "Shotgunosine/mindcontrol"
branch: "master"
tag: "latest"
commit: "272f8de372ce8511859a2e4960b3e636764d8f9d"
version: "6208e82cbf12e10abda5ce19029dface"
build_date: "2019-10-15T17:13:30.080Z"
size_mb: 5489
size: 1219780639
sif: "https://datasets.datalad.org/shub/Shotgunosine/mindcontrol/latest/2019-10-15-272f8de3-6208e82c/6208e82cbf12e10abda5ce19029dface.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Shotgunosine/mindcontrol/latest/2019-10-15-272f8de3-6208e82c/
recipe: https://datasets.datalad.org/shub/Shotgunosine/mindcontrol/latest/2019-10-15-272f8de3-6208e82c/Singularity
collection: Shotgunosine/mindcontrol
---

# Shotgunosine/mindcontrol:latest

```bash
$ singularity pull shub://Shotgunosine/mindcontrol:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
Namespace:shotgunosine
From: mindcontrol:latest

%labels
    Mainteiner Dylan Nielson\

%startscript
    export HOME=$(find /home/ -maxdepth 1 -mindepth 1 -writable -not -name "singularity_home")
    if [ ! -d  /mc_files/singularity_home/mindcontrol ] || [ ! -d  /mc_files/singularity_home/.meteor ] ||  [ ! -d  /mc_files/singularity_home/.cordova ] ; then
        echo "Copying meteor files into singularity_home" > /output/out
        rsync -rlD /mc_files/mindcontrol/mindcontrol /mc_files/singularity_home/ > /output/rsync 2>&1
        chmod -R 770 /mc_files/singularity_home/mindcontrol
        echo "/mc_files/mindcontrol/mindcontrol copied to $HOME" >> /output/out
        rsync -rlD /mc_files/mindcontrol/.meteor /mc_files/singularity_home/ >> /output/rsync 2>&1
        chmod -R 770 /mc_files/singularity_home/.meteor
        echo "/mc_files/mindcontrol/.meteor copied to $HOME" >> /output/out
        rsync -rlD /mc_files/mindcontrol/.cordova /mc_files/singularity_home/ >> /output/rsync 2>&1
        chmod -R 770 /mc_files/singularity_home/.cordova
        echo "/mc_files/mindcontrol/.cordova copied to $HOME" >> /output/out
    fi
    cd $HOME/mindcontrol
    # grab proper meteor port from settings file
    MC_PORT=$(cat /mc_settings/mc_port)
    MONGO_PORT=$(expr ${MC_PORT} + 1)

    # Check if we need to reset meteor
    DB_OWNER="NONE"
    if [ -d /mc_files/singularity_home/mindcontrol/.meteor/local/db ] ; then
        DB_OWNER=$(stat -c %U /mc_files/singularity_home/mindcontrol/.meteor/local/db)
    fi
    RESTORE_DB=0
    if [ ${DB_OWNER} != $(stat -c %U $HOME) ]  && [ ${DB_OWNER} != "NONE" ] ; then
        if [ ! -d  /output/mindcontrol_database ] ; then
            echo "Someone else owns the mongo database and there's no database dump to load from at /output/mindcontrol_database. Something's gone wrong. Exiting so we don't destroy data." >> /output/out
            exit 64
        fi
        echo "Someone else owns the db and a database dump was found, resetting Meteor" >> /output/out
        meteor reset
        RESTORE_DB=1
    fi
    echo "Starting mindcontrol and nginx" >> /output/out
    nginx
    nohup meteor --settings /mc_settings/mc_nginx_settings.json --port $MC_PORT > /output/mindcontrol.out 2>&1 &
    if [ ${RESTORE_DB} -eq 1 ] ; then
        echo "a"
        bash -c 'grep -m 1 "=> Started your app." <( tail -f /output/mindcontrol.out)'
        echo "b"
        mongorestore  --port=${MONGO_PORT} --drop --preserveUUID --gzip /output/mindcontrol_database/
    fi
```

## Collection

 - Name: [Shotgunosine/mindcontrol](https://github.com/Shotgunosine/mindcontrol)
 - License: [Other](None)

