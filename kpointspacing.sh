#
# To run VASP this script calls $vasp_std
# (or posibly $vasp_gam and/or $vasp_ncl).
# These variables can be defined by sourcing vaspcmd
. vaspcmd 2> /dev/null

#
# When vaspcmd is not available and $vasp_std,
# $vasp_gam, and/or $vasp_ncl are not set as environment
# variables, you can specify them here
[ -z "`echo $vasp_std`" ] && vasp_std="mpirun -np 8 /opt/proprietary-apps/vasp/5.4.4/bin/vasp_std"
[ -z "`echo $vasp_gam`" ] && vasp_gam="mpirun -np 8 /opt/proprietary-apps/vasp/5.4.4/bin/vasp_gam"
[ -z "`echo $vasp_ncl`" ] && vasp_ncl="mpirun -np 8 /opt/proprietary-apps/vasp/5.4.4/bin/vasp_ncl"

#
# The real work starts here
#

	#Energy Calculation
	cp INCAR.ENERGY INCAR

	sbatch --wait submit-vasp-ncl.sh 


for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 25 30 35 40 45 50 55 60 75 80 85 90 95 100 120 140 160 180 200
do
	echo " "	
	echo "Testing a kpoint spacing of $i"
	echo " "

	sed -i "2s/.*/$i/" KPOINTS.BAND
	mkdir kpointspacing$i 

	#Bandstructure Calculation
	cp KPOINTS.BAND KPOINTS
	cp INCAR.BAND INCAR

	sbatch --wait submit-vasp-ncl.sh 

	#The wavecar tends to get rather large, deleting these to save storage space
	rm WAVECAR 
	rm CHGCAR 

	cp vasprun.xml /kpointspacing$i 

done
