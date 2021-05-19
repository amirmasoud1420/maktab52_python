#!/bin/bash
read file
if [[ -f $file ]];then
tac $file > rev.txt
n=0
while read line && [[ $n -lt 10 ]]; do
	 
	echo "$line">>ver.txt
	n=$((n+1))
done < rev.txt
echo "this file is exist"
tac ver.txt > rev.txt
cat rev.txt
rm -f rev.txt
rm -f ver.txt
else
echo "File dose not exist"
fi

