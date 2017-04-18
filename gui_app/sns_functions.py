import boto3
import tkinter

from secret_settings import EMAIL

def create_topic(topic_name):
  """
  @param topic_name: Name of topic that will be created
  
  @return: Topic Arn
  """
  sns = boto3.client('sns')
  topic = sns.create_topic(Name=topic_name)
  topic = topic['TopicArn']
  return topic

def create_subscription(topic_arn, email):
  """
  @param topic_arn: Arn of Topic to subscribe to
  @param email: Email endpoint to subscribe with

  subscribes given email to topic if not already subscribed
  """
  sns = boto3.client('sns')
  subscriptions = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
  already_subscribed = False
  for sub in subscriptions['Subscriptions']:
    if sub['Endpoint'] == email:
      already_subscribed = True
      break
  if not already_subscribed:
    sns.subscribe(
      TopicArn=topic_arn,
      Protocol='email',
      Endpoint=email,
    )

def publish_message(topic_arn, subject, message):
  """
  @param topic_arn: Topic to publish to
  @param subject: Subject of message
  @param message: Message
  """
  sns = boto3.resource('sns')
  topic = sns.Topic(topic_arn)
  topic.publish(
    Subject=subject,
    Message=message,
  )
