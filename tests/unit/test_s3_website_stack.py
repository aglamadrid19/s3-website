import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_website.s3_website_stack import S3WebsiteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_website/s3_website_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3WebsiteStack(app, "s3-website")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
