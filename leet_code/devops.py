# # boto  3 


# import boto3

# def list_s3_bucket():


#     s3 = boto3.client('s3')

#     responces = s3.list_buckets()

#     for buckets in responces['Buckets']:
#         print(buckets)

# if __name__ == "__main__":
#     list_s3_bucket()


# ## ec2 

# def create_ec2():

#     ec2 = boto3.resource("ec2",region_name = "ap-south-1")

#     instances = ec2.create_instances()


# def create_s3():
#     responce = boto3.client('s3',region_name="ap-south-1")

#     s3 = responce.create_bucket(Bucket= "abc_bukcet")


# def create_iam_user():
#     responce = boto3.client('iam',region_name="ap-south-1")
#     iam = responce.create_iam(UserName="bharathi")

# def create_attach_user_policy():
#     responce  = boto3.client("iam",region_name="ap-south-1")

#     responce.attach_user_policy(
#         UserName= "bharathi"
#         PolicyArn="policy_arn"
#     )


# def create_lambda_function():
#     responce = boto3.client('lambda',region_name="ap-south-1")

#     responce.create_function(FunctionName="testing",Runtime="python3")


# x = "Hello World" 	str 	
# x = 20 	int 	
# x = 20.5 	float 	
# x = 1j 	complex 	
# x = ["apple", "banana", "cherry"] 	list 	
# x = ("apple", "banana", "cherry") 	tuple 	
# x = range(6) 	range 	
# x = {"name" : "John", "age" : 36} 	dict 	
# x = {"apple", "banana", "cherry"} 	set 	
# x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
# x = True 	bool 	
# x = b"Hello" 	bytes 	
# x = bytearray(5) 	bytearray 	
# x = memoryview(bytes(5)) 	memoryview 	
# x = None 	NoneType


x = 1
x = 1.1
x = 1j
x = 1 + 2j
print("x",x)
print(type(x))