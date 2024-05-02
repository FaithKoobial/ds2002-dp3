import boto3
import requests 
import json

url = "https://sqs.us-east-1.amazonaws.com/4408499236/rpy2ja"
sqs = boto3.client('sqs')

messages = {}
receipt_handle = []

def = delete_message(handles):
  try:
    sqs.delete_message(
      QueueUrl=url,
      ReceiptHandle=handle
    )
    print("Message deleted")
  except ClientError as e:
    print(e.response['Error']['Message'])

def get_message():
  try:
    for _ in range(10): 
      response = sqs.recieve_message(
        QueueUrl=url
        AttributeNames= [
            'All'
      ],
      MaxNumberOfMessages=1,
      MessageAttributeNames=[
          'All'
      ]
  )

          if "Messages" in response:
              order = response['Messages'][0]['MessagesAttributes']['order']['StringValue']
              word = response['Messages'][0]['MessagesAttributes']['word']['StringValue']
              handle = response['Messages'][0]['MessagesAttributes']['ReceiptHandle']

              Dict[f'{order}'] = f'{word}'
              sortDict = list(Dict.keys())
              sortDict.sort()
              final_dict = {i: Dict[i] for i in sortDict}

              print(final_dict)

          else:
              print("No message in the queue")
              exit(1)

      except ClientError as e:
          print(e.response['Error']['Message'])

      try: 
          sqs.delete_message(
              QueueUrl=url,
              ReceiptHandle=handle
          )
          print("Message deleted")
      except ClientError as e: 
           print(e.response['Error']['Message'])

if __name__ == "__main__":
    while True:
      get_message()









