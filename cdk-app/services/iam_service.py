"""Contains iam resources"""
from aws_cdk import (
    Stack,
    aws_sqs as sqs
)
from aws_cdk import aws_iam as iam
from config import app_config


def create_lambda_role(stack: Stack) -> iam.Role:
    """Creatin a iam role
    that will be assigned to lambda"""
    app_config_obj = app_config.Config()
    l_role = iam.Role(
        stack,
        app_config_obj.generate_resource_id("lambdaRole"),
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name=app_config_obj.generate_resource_name(
                "lambda_role"
            )
    )
    return l_role


def create_sqs_policies(
            stack: Stack,
            queue: sqs.Queue,
            queue_label: str
        ) -> iam.Policy:
    """Generate policies for sqs,
    can be attached to any other Principal
    """
    app_config_obj = app_config.Config()
    sqs_consume_policy = iam.Policy(
        stack,
        app_config_obj.generate_resource_id(queue_label),
        policy_name=app_config_obj.generate_resource_name(
                queue_label
            )
    )
    queue.grant_consume_messages(sqs_consume_policy)
    return sqs_consume_policy
