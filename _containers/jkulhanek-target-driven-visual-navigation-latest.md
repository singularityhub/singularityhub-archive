---
id: 7876
name: "jkulhanek/target-driven-visual-navigation"
branch: "master"
tag: "latest"
commit: "2fac0c94ebb07773c50c2563fc1d5f28becb0525"
version: "a8d07657cdc743d8b8f3fc4b8e8088b4"
build_date: "2020-04-15T19:40:36.132Z"
size_mb: 5056
size: 2980024351
sif: "https://datasets.datalad.org/shub/jkulhanek/target-driven-visual-navigation/latest/2020-04-15-2fac0c94-a8d07657/a8d07657cdc743d8b8f3fc4b8e8088b4.simg"
url: https://datasets.datalad.org/shub/jkulhanek/target-driven-visual-navigation/latest/2020-04-15-2fac0c94-a8d07657/
recipe: https://datasets.datalad.org/shub/jkulhanek/target-driven-visual-navigation/latest/2020-04-15-2fac0c94-a8d07657/Singularity
collection: jkulhanek/target-driven-visual-navigation
---

# jkulhanek/target-driven-visual-navigation:latest

```bash
$ singularity pull shub://jkulhanek/target-driven-visual-navigation:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: kulhanek/target-driven-visual-navigation:latest

%post
pip3 install git+https://github.com/jkulhanek/deep-rl-pytorch.git


%runscript
echo "Verifying mounted repository"
if [ -e /experiment ]
then
    echo "Experiment directory mounted"
    echo "Container is ready!"
    echo "Launching experiment with arguments [$@]"
    exec python3 "/experiment/$@"
else
    echo "You have to mount your repository to /experiment"
fi
```

## Collection

 - Name: [jkulhanek/target-driven-visual-navigation](https://github.com/jkulhanek/target-driven-visual-navigation)
 - License: [MIT License](https://api.github.com/licenses/mit)

