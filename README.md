# Screen Otter

### Get a screenshot from url

Usage:
```
python screen_otter.py [host]
```

This is especially handy when dealing with a list of hosts, for example after a Nmap scan:
```
nmap -p 80 [network] --open -oG list_of_hosts.txt
cat list_of_hosts.txt | grep 'Status: Up' | cut -d ' ' -f 2
while read host; do python screen_otter.py $host; done < list_of_hosts.txt
```

Screen Otter uses PhantomJS, which saves the screenshots in png format. In some cases the background might be transparent. The following command fixes the issue, and saves some space as well:
```
mogrify -flatten -format jpg *.png && rm *.png
```
