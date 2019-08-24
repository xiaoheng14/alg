#!/bin/bash

#set -e
#set -x

host_array=("192.1.1.1:hello 192.168.1.2:world")

host_file='/etc/hosts'


function valid_ip()
{
    local  ip=$1
    local  stat=1
  	
  	# if [[ $ip =~ ^[0-9]{1,3}/.[0-9]{1,3}/.[0-9]{1,3}/.[0-9]{1,3}$ ]]; then
    res=$(echo $ip | egrep -q '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
    if [[ $res -eq 0 ]]; then
        OIFS=$IFS
        IFS='.'
        ip=($ip)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
        stat=$?
    fi
    return $stat
}


function write_to_host ()
{
	IFS=":" 
	array=($1)
	if [[ ${#array[@]} != 2 ]]; then
		echo "wrong args: $1, each args should not include : "
		return  
	fi

	ipaddress=${array[0]}
	hostname=${array[1]}
	valid_ip "$ipaddress"
	if [[ $? != 0 ]]; then
		echo 'unuseful ipaddress, please check again'
		return
	fi

	if [[ ! -e $host_file ]]; then
		touch $host_file
	fi


	target="$ipaddress\t$hostname"

	line=$(egrep -q "^$ipaddress\s+$hostname$" $host_file)
	if [ $line ]; then
		echo "this record: $target already exists"
		return
	fi


	echo -e  $target >> $host_file

	if [ $? -eq 0 ]; then
		echo -e "successful add $target to $host_file"
	else
		echo -e "unsuccessful add $target to $host_file"
	fi
}


if [ $USER != 'root' ]; then
	echo 'You must execute this program as root'
	exit 1
fi


if [ $# -eq 0 ]; then
    for i in ${host_array[@]}; do
    	write_to_host $i
    	IFS=" "
    done
elif [ $# -eq 2 ]; then
    write_to_host "$1:$2"
else
	echo 'Wrong args, need IpAddress and HostName' 
	exit 1
fi
