import numpy
import sys

disf_time_file = sys.argv[1]
start_time = float(sys.argv[2])
end_time = float(sys.argv[3])

disf_times = numpy.matrix(numpy.genfromtxt(disf_time_file,delimiter=' ',dtype='float'))

num_disf = disf_times.shape[0]
num_label_stamps = int(100*(end_time - start_time))

lables = numpy.zeros(num_label_stamps)
print disf_times

for ind in range(0,num_disf):
	start_disf = int((disf_times[ind,0] - start_time) *100)
	end_disf = int((disf_times[ind,1] - start_time)*100)
	print start_disf 
	
	lables[start_disf:end_disf] = 1


numpy.savetxt('temp_lables',lables,fmt='%d')
