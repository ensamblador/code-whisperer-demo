from aws_cdk import (
    # Duration,
    Stack,
    # Import Function
    aws_iam as iam,
    # aws_sqs as sqs,
)
from aws_cdk.aws_lambda import Code, Function, Runtime

from constructs import Construct

class CodeWhispererDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # CDK Lambda function construct within python 3.10
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda_python/Function.html
        demo_function = Function(self, "demoFunction",
            runtime=Runtime.PYTHON_3_10,
            handler="demo_function.lambda_handler",
            code=Code.from_asset("lambda"),
            environment={
                "DEMO_ENV_VARIABLE": "demo_env_value"
            }
        )

        # give demo_function permissions to send emails with ses
        demo_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ses:SendEmail"],
                resources=["*"]
            )
        )
        