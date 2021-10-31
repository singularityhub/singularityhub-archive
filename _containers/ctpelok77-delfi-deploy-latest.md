---
id: 13403
name: "ctpelok77/delfi-deploy"
branch: "master"
tag: "latest"
commit: "a155dbf7311d4210fa464de1d74e9b292e8a7417"
version: "fc7500fe2871e0da33d4c55ed69a5edc"
build_date: "2021-04-06T10:55:48.618Z"
size_mb: 1514.0
size: 683573279
sif: "https://datasets.datalad.org/shub/ctpelok77/delfi-deploy/latest/2021-04-06-a155dbf7-fc7500fe/fc7500fe2871e0da33d4c55ed69a5edc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ctpelok77/delfi-deploy/latest/2021-04-06-a155dbf7-fc7500fe/
recipe: https://datasets.datalad.org/shub/ctpelok77/delfi-deploy/latest/2021-04-06-a155dbf7-fc7500fe/Singularity
collection: ctpelok77/delfi-deploy
---

# ctpelok77/delfi-deploy:latest

```bash
$ singularity pull shub://ctpelok77/delfi-deploy:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ctpelok77/delfi:latest

%setup
    # Just for diagnosis purposes
    hostname -f > $SINGULARITY_ROOTFS/etc/build_host
%runscript
    # This will be called whenever the Singularity container is invoked
    python /workspace/delfi/plan-ipc.py --image-from-lifted-task $@

%post

%labels
Name        Delfi1 (winner of IPC2018, optimal track)
Description This planner uses an offline learned algorithm selector to choose the "best" planner online based on a abstract structure graph of the PDDL description of the planning task. In particular, the learning algorithm uses such graphs of a planning task, turns them into an image and uses the planner runtime to train a neural net. The learned model thus predicts runtime of planners on a given task and chooses a planner accordingly.
Authors     Michael Katz <michael.katz1@ibm.com>, Shirin Sohrabi <ssohrab@us.ibm.com>, Horst Samulowitz <samulowitz@us.ibm.com>, and Silvan Sievers <silvan.sievers@unibas.ch>
```

## Collection

 - Name: [ctpelok77/delfi-deploy](https://github.com/ctpelok77/delfi-deploy)
 - License: None

