
[[linux]]
cat == text display (good for small files) (short for concatinate)

sed == stream editor

more == text display (more sophisticated)

less == same as more but can search using /

(((less is more)))

kali-tweaks == configure shell for bash or zsh

# cat /etc/snort/snort.cof
___
replace snort with whatever

# head /etc/snort/snort.conf
___
better than cat

show first 10 lines(by default) of a tool or file

can alter amount of lines(head -20)

# tail /etc/snort/snort.conf
___
better than cat

show last 10 lines(by default) of a tool or file

can alter amount of lines(tail -20)

# sudo nl /etc/snort/snort.conf
___
number lines

# sudo nl /etc/snort/snort.conf | grep Errorlog
___
parse output nicely

# sudo sed s/mysql/MySQL/g
___
sys_change/word_with/new_word/globally

# sudo sed s/mysql/MySQL/g /etc/snort/snort.conf
___
with dir

# sudo sed s/mysql/MySQL/g /etc/snort/snort.conf > snort2.conf
___
add location for output if you do not want orgnl to change

# more /etc/snort/snort.conf
___

enter == 1 line

space == 1 page

q == exit

# less /etc/snort/snort.conf
___
enter == 1 line

space == 1 page

q == exit

/ == search

# power
___
sudo reboot = sync disk before reboot

sudo shutdown now = safe way to shut down

sudo poweroff = safe way to shut down

# dmesg | grep -i error 
___
check sys logs fo i/o errors

# df -h
___
check disk usage (if disk is full, sys might not boot)

- if "/" , "/var" , "/tmp" is 100% then it is not good

# sudo dmesg | less 
___
get more info if something is damaged

# sudo touch /forcefsck
___
force filesys integrity check

# sudo chmod o-x /usr/sbin/snort
___
chmod = change filemode

o-x = remove execute permission for non root

# sudo chmod o+x /usr/sbin/snort
___
chmod = change filemode

o+x = add execute permission for non root
