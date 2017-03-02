#!python
#==========================================================================#
# sjdillon
# 1. quick smoke test to confirm nodes, buckets, credentials are correct
# 	sets, gets, deletes keys against nodes in cluster, output exec time
#	stores cluster nodes in pickled json file
#==========================================================================#
from couchbase import Couchbase
import pickledb
import timeit

def get_config(key, dbfile):
	pdb=pickledb.load(dbfile, False)
	config=pdb.dgetall(key)
	return config

def key_test(bucket,pw,env):
	server=env
	start = timeit.default_timer()
	print 'bucket: %s' % (bucket)
	print 'pw: %s' % pw
	print 'nodes: %s' % server
	cb=Couchbase.connect(host=server,bucket=bucket,password=pw, timeout=10)
	key='miskatonic'
	val={"first_name":"Keziah", "last_name":"Mason", "town":"Arkham"}
	print '1. setting key...'
	cb.set(key,val)
	print '\t2. getting key...'
	result=cb.get(key)
	print '\t' + str(result.value)
	print '\t3. deleting key...'
	#cb.delete(key)
	stop = timeit.default_timer()
	print '\texecution time:%fs' % (stop-start)
	print '\n'


def smoke(bucket,pw,env):
	print 'environment: %s' % env 
	servers=get_config(env,'couchbase.db')
	key_test(bucket,pw,servers)

def smoke_each_node(bucket,pw,env):
	servers=get_config(env,'couchbase.db')
	print servers
	for server in servers:
		key_test(bucket,pw,server)
		 


# run test
env='my_cluster'
smoke_each_node('CoinOpCache','Aki9kak9ujj',env)
smoke_each_node('YarsReveng','Loev213ddaa',env)
smoke_each_node('BatConfiguration','woolw98rcccaw1',env)


