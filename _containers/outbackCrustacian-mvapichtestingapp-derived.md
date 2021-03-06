---
id: 3510
name: "outbackCrustacian/mvapichtestingapp"
branch: "master"
tag: "derived"
commit: "d5bc739e4239720d4bbabcf090bf6ee0fdfd4f9e"
version: "efaafc392a2aaa1ddc5013b654db3486"
build_date: "2020-04-25T05:34:10.086Z"
size_mb: 875
size: 255963167
sif: "https://datasets.datalad.org/shub/outbackCrustacian/mvapichtestingapp/derived/2020-04-25-d5bc739e-efaafc39/efaafc392a2aaa1ddc5013b654db3486.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/outbackCrustacian/mvapichtestingapp/derived/2020-04-25-d5bc739e-efaafc39/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/mvapichtestingapp/derived/2020-04-25-d5bc739e-efaafc39/Singularity
collection: outbackCrustacian/mvapichtestingapp
---

# outbackCrustacian/mvapichtestingapp:derived

```bash
$ singularity pull shub://outbackCrustacian/mvapichtestingapp:derived
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:latest

%setup
   # make directory for test MPI program
   mkdir ${SINGULARITY_ROOTFS}/testmvapich
   # get updated files
   cd ${SINGULARITY_ROOTFS}/testmvapich/
   git clone https://github.com/outbackCrustacian/updated-osu_mbw_mr.c-file.git .

%post
   yum install -y wget
   yes | yum install vim-X11 vim-common vim-enhanced vim-minimal
   # add to local environment to build pi.c
   export PATH=$PATH:/mpich/install/lib
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort
   cd /testmvapich
   wget -q http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-5.4.2.tar.gz
   tar xf osu-micro-benchmarks-5.4.2.tar.gz --strip-components=1
   # move updated files
   mv osu_mbw_mr.c mpi/pt2pt/
   mv osu_multi_lat.c mpi/pt2pt/
   mv osu_bcast.c mpi/collective/
   mv osu_allreduce.c mpi/collective/
   mv osu_gather.c mpi/collective/
   mv osu_util.h  util/
   mv osu_util.c util/


   ./configure CC=/mpich/install/bin/mpicc CXX=/mpich/install/bin/mpicxx --prefix=/usr
	make
	make install

#push please
#Point To Point MPI Benchmarks
#
#
##############################
# latency
##############################
%apprun latency
   # run the command to perform a latency test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency

%apphelp latency
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   The latency tests are carried out in a ping-pong fashion. The sender
   sends a message with a certain data size to the receiver and waits for a
   reply from the receiver. The receiver receives the message from the sender
   and sends back a reply with the same data size. Many iterations of this
   ping-pong test are carried out and average one-way latency numbers are
   obtained. Blocking version of MPI functions (MPI_Send and MPI_Recv) are
   used in the tests.



##############################
# bandwith
##############################
%apprun bandwith
   # run the command to perform a bandwith test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw

%apphelp bandwith
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   The bandwidth tests were carried out by having the sender sending out a
   fixed number (equal to the window size) of back-to-back messages to the
   receiver and then waiting for a reply from the receiver. The receiver
   sends the reply only after receiving all these messages. This process is
   repeated for several iterations and the bandwidth is calculated based on
   the elapsed time (from the time sender sends the first message until the
   time it receives the reply back from the receiver) and the number of bytes
   sent by the sender. The objective of this bandwidth test is to determine
   the maximum sustained date rate that can be achieved at the network level.
   Thus, non-blocking version of MPI functions (MPI_Isend and MPI_Irecv) were
   used in the test.




##############################
# latency_mt
##############################
%apprun latency_mt
   # run the command to perform a multi threaded latency test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency_mt

%apphelp latency_mt
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   The multi-threaded latency test performs a ping-pong test with a single
   sender process and multiple threads on the receiving process. In this test
   the sending process sends a message of a given data size to the receiver
   and waits for a reply from the receiver process. The receiving process has
   a variable number of receiving threads (set by default to 2), where each
   thread calls MPI_Recv and upon receiving a message sends back a response
   of equal size. Many iterations are performed and the average one-way
   latency numbers are reported.



##############################
# bibw
##############################
%apprun bibw
   #run the command to perform a bidirectional bandwith test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bibw

%apphelp bibw
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   The bidirectional bandwidth test is similar to the bandwidth test, except
   that both the nodes involved send out a fixed number of back-to-back
   messages and wait for the reply. This test measures the maximum
   sustainable aggregate bandwidth by two nodes.



##############################
# mbw_mr
##############################
%apprun mbw_mr
   #run the command to perform a multiple bandwith / messaging rate test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_mbw_mr

%apphelp mbw_mr
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   The multi-pair bandwidth and message rate test evaluates the aggregate
   uni-directional bandwidth and message rate between multiple pairs of
   processes. Each of the sending processes sends a fixed number of messages
   (the window size) back-to-back to the paired receiving process before
   waiting for a reply from the receiver. This process is repeated for
   several iterations. The objective of this benchmark is to determine the
   achieved bandwidth and message rate from one node to another node with a
   configurable number of processes running on each node.



##############################
# multi_lat
##############################
%apprun multi_lat
   #run the command to perform a multi pair latency test
   /usr/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_multi_lat

%apphelp latency_mt
   Documentation from http://mvapich.cse.ohio-state.edu/benchmarks
   This test is very similar to the latency test. However, at the same
   instant multiple pairs are performing the same test simultaneously.
   In order to perform the test across just two nodes the hostnames must
   be specified in block fashion.









#Collective MPI Benchmarks
#
#
#00000000000000000000000000000
#allcollectives
#00000000000000000000000000000
%apprun allcollectives
   #run every benchmark included in the collective library
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allgather
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allgatherv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allreduce
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoall
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoallv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_barrier
   sleep
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_bcast
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_gather
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_gatherv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce_scatter
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_scatter
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_scatterv
   wait


#00000000000000000000000000000
# allgather
#00000000000000000000000000000
%apprun allgather
   #run an MPI allgather latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allgather


#00000000000000000000000000000
# allgatherv
#00000000000000000000000000000
%apprun allgatherv
   #run an MPI allgatherv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allgatherv


#00000000000000000000000000000
#allreduce
#00000000000000000000000000000
%apprun allreduce
   #run an MPI allreduce latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_allreduce


#00000000000000000000000000000
#alltoall
#00000000000000000000000000000
%apprun alltoall
   #run an MPI alltoall latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoall


#00000000000000000000000000000
#alltoallv
#00000000000000000000000000000
%apprun alltoallv
   #run an MPI alltoallv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_alltoallv


#00000000000000000000000000000
#barrier
#00000000000000000000000000000
%apprun barrier
   #run an MPI barrier latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_barrier


#00000000000000000000000000000
#bcast
#00000000000000000000000000000
%apprun bcast
   #run an MPI bcast latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_bcast


#00000000000000000000000000000
#gather
#00000000000000000000000000000
%apprun gather
   #run an MPI gather latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_gather


#00000000000000000000000000000
#gatherv
#00000000000000000000000000000
%apprun gatherv
   #run an MPI gatherv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_gatherv


#00000000000000000000000000000
#reduce
#00000000000000000000000000000
%apprun reduce
   #run an mpi reduce latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce


#00000000000000000000000000000
#reduce_scatter
#00000000000000000000000000000
%apprun reduce_scatter
   #run an mpi reduce_scatter latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce_scatter


#00000000000000000000000000000
#scatter
#00000000000000000000000000000
%apprun scatter
   #run an mpi scatter latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_scatter


#00000000000000000000000000000
#scatterv
#00000000000000000000000000000
%apprun scatterv
   #run an mpi scatterv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_scatterv









#Non blocking collective MPI benchmarks
#
#
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#allnonblocking
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun allnonblocking
   #run every benchmark included in the collective library
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgather
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgatherv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoall
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoallv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ibarrier
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ibcast
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_igather
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_igatherv
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatter
   sleep 1
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatterv
   wait


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# iallgather
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun iallgather
   #run an MPI iallgather latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgather


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# iallgatherv
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun iallgatherv
   #run an MPI iallgatherv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iallgatherv


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#ialltoall
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun ialltoall
   #run an MPI ialltoall latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoall


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#ialltoallv
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun ialltoallv
   #run an MPI ialltoallv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoallv


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#ialltoallw
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun ialltoallw
   #run an MPI ialltoallw latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ialltoallw


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#ibarrier
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun ibarrier
   #run an MPI ibarrier latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ibarrier


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#ibcast
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun ibcast
   #run an MPI ibcast latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_ibcast


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#igather
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun igather
   #run an MPI igather latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_igather


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#igatherv
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun igatherv
   #run an MPI igatherv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_igatherv


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#iscatter
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun iscatter
   #run an mpi iscatter latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatter


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#iscatterv
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%apprun iscatterv
   #run an mpi iscatterv latency benchmark
   /usr/libexec/osu-micro-benchmarks/mpi/collective/osu_iscatterv
```

## Collection

 - Name: [outbackCrustacian/mvapichtestingapp](https://github.com/outbackCrustacian/mvapichtestingapp)
 - License: None

