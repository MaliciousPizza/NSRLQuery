
import sqlite3
import argparse,textwrap,pathlib
import os
from unittest import result

class HashCompare:
    def __init__(self,args):
        self.args = args

    ## if the option to find the known hashes then return the result, if the hash is not in the database exit
    def known_hashes(self,hash_compare_result):
        
        if hash_compare_result == None:
            exit
        else:
            print(hash_compare_result)
    
    ## if the option to find unknown hashes that are not in the database then return the hash that is being looked up
    def unknown_hashes(self,hash_compare_result,hash_value):
        if hash_compare_result == None:
           print(hash_value)
        else:
            exit

    ## lookup the hashes in the database  
    def hash_compare(self, hash):
        
        ## lookup the MD5 hashes
        def md5_hash_compare(self,md5_hash):
            con = sqlite3.connect(self.args.database)
            cur = con.cursor()
            res = cur.execute('SELECT md5 FROM FILE where md5 = ?',[md5_hash] )
            query_output = res.fetchone()
            if query_output == None:
                return query_output
            else:
                return query_output[0]

        ## lookup the sha1 hashes.
        def sha1_hash_compare(self,sha1_hash):
            con = sqlite3.connect(self.args.database)
            cur = con.cursor()
            res = cur.execute('SELECT sha1 FROM FILE where sha1 = ?',[sha1_hash] )
            query_output = res.fetchone()
            if query_output == None:
                return query_output
            else:
                return query_output[0]
        
        ## lookup the sha256 hashes
        def sha256_hash_compare(self,sha256_hash):
            con = sqlite3.connect(self.args.database)
            cur = con.cursor()
            res = cur.execute('SELECT sha256 FROM FILE WHERE sha256 = ? ',[sha256_hash])
            query_output = res.fetchone()
            if query_output == None:
                return query_output
            else:
                query_output = query_output[0]
                return query_output

        if self.args.algorithm == 'md5':
            hash_compare_result = md5_hash_compare(self,hash)
        if self.args.algorithm == 'sha1':
            hash_compare_result = sha1_hash_compare(self,hash)
        if self.args.algorithm == 'sha256':
            hash_compare_result = sha256_hash_compare(self,hash)

        return hash_compare_result


    def handle(self):
        
        if (self.args.unknown == True):
            hash = self.args.hash
            results = self.hash_compare(hash)
            self.unknown_hashes(results,hash)
            
        else:
            hash = self.args.hash
            results = self.hash_compare(hash)
            self.known_hashes(results)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description= 'RDSV3 Query Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            nsrlquery.py -a sha256 -d /nsrl/rdsv3.db 000000ADA6DDCA899E68D00512489768A1A330CBB02716CEC3BD73FE36B28DE7
            nsrlquery.py -m /nsrl/databases/
        ''')
    )
    parser.add_argument('-a','--algorithm',type=str,help='sha256, md5, sha1',default='md5')
    parser.add_argument('-d','--database',type=str,help='directory to the sqlite3 database')
    parser.add_argument('-k','--known',action='store_true',help='Known hashes default')
    parser.add_argument('-u','--unknown',action='store_true',help='Unknown hashes')
    parser.add_argument('hash',type=str)
    args = parser.parse_args()

    h = HashCompare(args)
    h.handle()
