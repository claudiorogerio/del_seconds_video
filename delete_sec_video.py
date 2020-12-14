import sys
import os
import time
import platform
import subprocess

"""
claudiorogerio@unifap.br
24.05.2020
Function which del some final seconds from video
input_vd - 
seconds - seconds to be retired

return a new video without seconds
"""
def delete_seconds_video( input_vd, seconds, output ):

    # total seconds from input
    cmd = "ffprobe -i " + input_vd + " -show_format -v quiet | grep duration | awk {'print substr($1,10,length($0))'} > conf.duration "
    subprocess.Popen( cmd, shell=True )
    time.sleep(1)   
    file_object  = open( "conf.duration", "r" )
    tmp = file_object.read()
    tmp = tmp.split('.')        # apenas os segundos
    tmp = int( tmp[0] )           # desconsidera milesimos de sec
    tmp = tmp - seconds

    cmd = "ffmpeg -t " + str(tmp) + " -i " + input_vd + " -c copy " + output + " -y "
    print( cmd )
    #subprocess.Popen( cmd, shell=True )
    os.system( cmd )
    time.sleep(1)   #precisa sleep para que possa pegar o valor atualizado
#    cmd = "mv " + input_vd[:-4] + "_sec.mp4 " + input_vd
#    os.system( cmd )
#    subprocess.Popen( cmd, shell=True )

no, input_vd, seconds, output_vd = sys.argv
print( "Deleting seconds from file:", input_vd, seconds, " s ", " creating ", output_vd )
seconds = int(seconds)

delete_seconds_video( input_vd, seconds, output_vd )
