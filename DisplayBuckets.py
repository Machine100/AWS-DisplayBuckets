

import boto3
s3 = boto3.client('s3')                                #nstantiate a client connection to S3

response = s3.list_buckets()
print('<---rcvd from s3.list_buckets()---', response)  #response comes in as a dict

response2 = response['Buckets']                        #from key 'Buckets', extract a list
print('<---rcvd the Buckets key---', response2)

print('These are the buckets in your account:')        #display key 'Name' for each item in that list 
for item in response2:                                 #these are the bucketnames for the account configured
	print(item['Name'])                                #under the pc's AWS console configuration.

  

#Use more compact syntax to do the same thing:
#buckets = [bucket['Name'] for bucket in response['Buckets']]
#print('Bucket List: %s' % buckets)   

#Or use the resource:
#for bucket in s3resource.buckets.all():
#print(bucket.name)

#A call to client.list_objects will return the objects in a bucket:
#response = s3client.list_objects(Bucket='asdfasdf-s3bucket-tftui51y564p')

               
