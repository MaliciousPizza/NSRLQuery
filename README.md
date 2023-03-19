# NSRLQuery
Tool to query the new RDSV3 NSRL database. 

Currently under construction, the tool is very simple to use. 
First you must have a version of the RDSV3 NSRL database on your system. 
Second if you would like to merge a delta file, or merge the Legacy with the modern, place them in the same directory. Then run the NSRLMerge.py tool with the directory as an argument. This will merge any databases in the directory. 
Lastly, if you would like to query the database use the NSRLQuery tool. To find unknowns use the -u option, finding knowns is the default action, but you can also add the -k option to find knowns. to execute the program run python nsrlqeury.py -d /directory/to/the/database -a sha256 <HASH>
