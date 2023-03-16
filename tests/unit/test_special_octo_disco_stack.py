import aws_cdk as core
import aws_cdk.assertions as assertions

from special_octo_disco.special_octo_disco_stack import SpecialOctoDiscoStack


def test_oidc_provider_created():
    app = core.App()
    stack = SpecialOctoDiscoStack(app, "special-octo-disco")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("Custom::AWSCDKOpenIDConnectProvider", {
        "Url" : "https://token.actions.githubusercontent.com"
    })

def test_oidc_role_created():
    app = core.App()
    stack = SpecialOctoDiscoStack(app, "special-octo-disco")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::IAM::Role", {
        "AssumeRolePolicy": {
        "Statement": [{
            "Action": "sts:AssumeRola",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            }
        }]
        }
    })