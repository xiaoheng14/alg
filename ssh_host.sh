#!/bin/bash

#set -e 
#set -x


deploy_for=('hello')

deploy_list=("192.168.1.2" "192.168.1.3")


function rand_nistp256()
{
	seqrand=$1
	length1=82
	length2=22
	length3=29

	i=1
	j=1
	k=1
	seq=(0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)

	num_seq=${#seq[@]}

	seqrand="$seqrand ecdsa-sha2-nistp256 AAAA"
	while [[ $i -le $length1 ]]; do
		seqrand=$seqrand${seq[$((RANDOM%num_seq))]}
		let "i=i+1"
	done

	seqrand=$seqrand/

	while [[ $j -le $length2 ]]; do
		seqrand="$seqrand${seq[$((RANDOM%num_seq))]}"
		let "j=j+1"
	done 

	seqrand="$seqrand+"

	while [[ $k -le $length3 ]]; do
		seqrand="$seqrand${seq[$((RANDOM%num_seq))]}"
		let "k=k+1"
	done 

	seqrand="$seqrand="
	echo $seqrand
}



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

function add_to_known_host()
{
	user=$1
	ssh_ipaddress=$2

	if [[ ! $user ]]; then
		echo "no such user: $user"
		return 1
	fi

	if [[ ! $ssh_ipaddress ]]; then
		echo "no found ssh_ipaddress: $ssh_ipaddress, please check again"
		return 1
	fi

	valid_ip "$ssh_ipaddress"
	if [[ $? != 0 ]]; then
		echo "unuseful ipaddress: $ssh_ipaddress, please check again"
		return 1
	fi

	ssh_line=`rand_nistp256 $ssh_ipaddress`
	echo $ssh_line

	user_path=`cat /etc/passwd | grep $user | awk -F ":" '{print $6}'`  
	if [[ ! -e $user_path ]]; then
		mkdir -p $user_path
	fi

	ssh_folder="$user_path/.ssh"
	if [[ ! -e $ssh_folder ]]; then
		mkdir $ssh_folder
	fi

	known_host_path=${ssh_folder}/known_hosts 
	
	if [[ -e $known_host_path ]]; then
		egrep -q "^$ssh_ipaddress" $known_host_path
		if [[ $? == 0 ]]; then
			echo "this ipaddress: $ssh_ipaddress already exists"
			return 0
		else
			echo -e $ssh_line >> $known_host_path
			if [[ $? == 0 ]]; then
				echo "successful add this record: ${ssh_line} to $known_host_path"
			fi
		fi
	else
		echo -e $ssh_line >> $known_host_path
		if [[ $? == 0 ]]; then
			echo "successful add this record: ${ssh_line} to $known_host_path"
		fi
	fi

}


if [[ $USER != 'root' ]]; then
	echo 'You must execute this program as root'
	exit 1
fi



if [[ $# -eq 0 ]]; then

	for u in ${deploy_for[@]}; do
		egrep -q "^$u:.*" /etc/passwd
		if [[ $? != 0 ]]; then
			echo "no such user: $u"
			continue
		fi
		for i in ${deploy_list[@]}; do
			add_to_known_host "$u" "$i"
		done
	done

else
	if [[ $1 == "-u" ]]; then
		user=$2
		egrep -q "^$user:.*" /etc/passwd
		if [[ $? != 0 ]]; then
			echo "no such user: $user"
			exit 1
		fi
		ssh_ipaddress=$3
	else
		last_user=$(last -n 1 | awk '{ print $1}')
		user_list=($last_user)
		user=${user_list[0]}	
		ssh_ipaddress=$1
	fi
	add_to_known_host "$user" "$ssh_ipaddress"
fi
