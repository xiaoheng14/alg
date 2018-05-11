#/bin/bash

#set -e
#set -x

deploy_for=('fkfk')

deploy_list=("root:192.168.1.2:2232")


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


function valid_port()
{
	local port=$1
	local stat=1
	if [[ $port =~ ^[0-9]{1,5}$ ]]; then
		[[ $port -le 65535 && $port -ge 0 ]]
		stat=$?
	fi
	return $stat
}


function add_to_history()
{
	user=$1
	IFS=":"
	ssh_list=($2)
	if [[ ${#ssh_list[@]} != 3 ]]; then
		echo "wrong args: $2, each args should not include : "
		return 1 
	fi

	ssh_user=${ssh_list[0]}
	ssh_ipaddress=${ssh_list[1]}
	ssh_port=${ssh_list[2]}

	if [[ ! $user ]]; then
		echo "no such user: $user"
		return 1
	fi

	if [[ ! $ssh_user ]]; then
		echo "no found ssh_user: $ssh_user"
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


	if [ $ssh_port ]; then
		valid_port "$ssh_port"
		if [[ $? != 0 ]]; then
			echo "unuseful port: $ssh_port, please check again"
			return 1
		fi
	fi 


	ssh_line="$ssh_user@$ssh_ipaddress $ssh_port"
	echo $ssh_line


	user_path=`cat /etc/passwd | grep $user | awk -F ":" '{print $6}'`  
	if [[ ! -e $user_path ]]; then
		mkdir -p $user_path
	fi

	bash_history_path=${user_path}/.bash_history

	if [[ -e $bash_history_path ]]; then 
		egrep -q "^$ssh_line$" $bash_history_path
		if [[ $? == 0 ]]; then
			echo "this record: $ssh_line already exists"
			return 0
		fi
	fi


	if [[ -e $bash_history_path ]]; then 
		num=`cat $bash_history_path | wc -l`
		mid_num=`expr $num / 2`

		check_mid=`$mid_num % 2`
		if [[ $check_mid == 1 ]]; then
			mid_num=`expr $mid_num + 1`
		fi

		sed -i 'N;$mid_numa$ssh_line' $bash_history_path
		if [[ $? == 0 ]]; then
			echo "successful add this record: ${ssh_line} to $bash_history_path"
		fi
	else
		echo -e $ssh_line >> $bash_history_path
		if [[ $? == 0 ]]; then
			echo "successful add this record: ${ssh_line} to $bash_history_path"
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
			add_to_history $u $i
			IFS=" "
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
		ssh_user=$3
		ssh_ipaddress=$4
		ssh_port=$5
	else
		last_user=$(last -n 1 | awk '{ print $1}')
		user_list=($last_user)
		user=${user_list[0]}	
		ssh_user=$1
		ssh_ipaddress=$2
		ssh_port=$3
	fi
	add_to_history "$user" "$ssh_user:$ssh_ipaddress:$ssh_port"
fi
