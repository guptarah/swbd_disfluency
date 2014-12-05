import numpy
import sys

time_file = sys.argv[1]
start_time = float(sys.argv[2])
end_time = float(sys.argv[3])

time_mat = numpy.genfromtxt(time_file,delimiter=' ',dtype='float')

length_file = time_mat.shape[0]
vec1 = numpy.tile(start_time,(length_file,1))
vec2 = numpy.tile(end_time,(length_file,1))

vec1_diff = numpy.matrix(time_mat[:,0]).T - vec1
vec2_diff = numpy.matrix(time_mat[:,1]).T - vec2
 
f1=open('./temp_start_end', 'w+')
f1.write(str(numpy.nonzero(numpy.diff(numpy.sign(vec1_diff).T))[1][0,0] + 2))
f1.write('\n')
f1.write(str(numpy.nonzero(numpy.diff(numpy.sign(vec2_diff).T))[1][0,0] + 1))
f1.close
