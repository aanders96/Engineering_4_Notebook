gpio mode 0 out 
for i in [1,2,3, .. 10]
do 
	gpio write 0 1
	sleep 3
	gpio  write 0 0
 	sleep 3
done

