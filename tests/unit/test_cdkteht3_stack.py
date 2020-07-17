import json
import pytest

from aws_cdk import core
from cdkteht3.cdkteht3_stack import Cdkteht3Stack


def get_template():
    app = core.App()
    Cdkteht3Stack(app, "cdkteht3")
    return json.dumps(app.synth().get_stack("cdkteht3").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
