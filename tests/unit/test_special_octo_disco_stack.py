import aws_cdk as core
import aws_cdk.assertions as assertions

from special_octo_disco.special_octo_disco_stack import SpecialOctoDiscoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in special_octo_disco/special_octo_disco_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SpecialOctoDiscoStack(app, "special-octo-disco")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
