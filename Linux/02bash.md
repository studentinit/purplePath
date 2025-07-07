[[linux]]


							
-------------------------------------------------------------------
                       (/) ### root
              
    /root    ------> sudo home dir
    
    	/boot   -------> location of kernel img
    	
    		/etc     -------> sys config files
    		
    			/home -------> user's dir
    			
    				/mnt   -------> general purpose mount print
    				
    					/proc   -------> a view of internal kernel data
         
    						/sys.   -------> the kernel's view of the hardware
          
    							/dev.   -------> special device files live here
           
    								/bin     -------> executables
            
    									/sbin   -------> executables
             
    										/lib      -------> libraries
              
    											/user
    												
    											bin. -------> more executables
    												sbin -------> more executables
    													lib-------> more libraries

binaries == executables

linux is case sensitive

directory(dir) == file or folder

# ls -l
___
(l) == link

(-) == file

(d) == dir

rwx == readwriteexecute
___
# sudo systemctl start apache2 
___
start apache2
___
# ps aux | grep apache2
___
filter running ps for apache2
___
