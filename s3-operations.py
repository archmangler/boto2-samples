import boto
import boto.s3.connection
from boto.s3.key import Key

'''Sample boto2 operations (FAST AND DIRTY. NOT SUITABLE PRODUCTION CODE): create a bucket, check permissions of access user, upload file to bucket, list files in bucket '''

access_key = ''
secret_key = ''
conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host='s3.endpoint.aws.com',
port=8067,
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
bucket = conn.create_bucket('artifacts')

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
)

acp = bucket.get_acl()
for grant in acp.acl.grants:
    print(grant.display_name, grant.permission)

file_name='/tmp/data.gz'
my_bucket = conn.lookup('artifacts')


k=Key(bucket)
k.key='testfile'
k.set_contents_from_filename(file_name)

#Get the file backc:wq
k.get_contents_to_filename(str(k.key).replace('/', '_'))

for i in my_bucket.list():
 print "beep: ",i
