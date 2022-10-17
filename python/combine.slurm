#!/bin/bash
#SBATCH -p bii # partition/queue
#SBATCH --nodes=1		# number of compute nodes
#SBATCH --ntasks=1		# number of program instances
#SBATCH --cpus-per-task=8       # use 1 cpu core
#SBATCH --time=12:00:00		# max time before job cancels
#SBATCH --mem=256GB               # memory

module purge
module load anaconda/2020.11-py3.8

python combine.py