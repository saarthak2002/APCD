#!/bin/bash
#SBATCH -p bii # partition/queue
#SBATCH --nodes=1		# number of compute nodes
#SBATCH --ntasks=1		# number of program instances
#SBATCH --cpus-per-task=8       # use 1 cpu core
#SBATCH --time=52:00:00		# max time before job cancels
#SBATCH --mem=256GB               # memory

module purge
module load anaconda/2020.11-py3.8

OUTDIR=/project/biocomplexity/anil/APCD/saarthak/extracted_data_csv/UVA_prescriptions_2020
mkdir -p $OUTDIR

FILES="/project/biocomplexity/MeaslesProject/APCDdata/RX/monthlyRXData/RX2020/*"
for f in $FILES
do
  echo "Processing $f file..."
  FILENAME=$(basename $f)
  python saarthak_pres_csv.py $f $OUTDIR/prescriptions_$FILENAME
done