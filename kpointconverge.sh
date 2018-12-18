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

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
	echo " "	
	echo "Copied KPOINTS$i in"
	echo " "
	cp KPOINTS.$i KPOINTS

	time mpirun -np 16 /opt/proprietary-apps/vasp/5.4.4/bin/vasp_ncl
done
