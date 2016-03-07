# screen_otter

### Gets a screenshot from url and saves it as png

Usage:
```
python screen_otter.py [host]
```

This is especially handy when dealing with a list of hosts, for example after a Nmap scan.
```
nmap -p 80 [network] --open -oG list_of_hosts.txt
cat list_of_hosts.txt | grep 'Status: Up' | cut -d ' ' -f 2
while read host; do python screen_otter.py $host; done < list_of_hosts.txt
mogrify -flatten -format jpg *.png && rm *.png
```
