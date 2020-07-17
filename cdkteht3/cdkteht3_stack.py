from aws_cdk import (
    aws_s3 as _s3,
    aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)


class Cdkteht3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3 = _s3.Bucket(self, "Mervis3bucket")

        queue = sqs.Queue(self, "MerviSQSQueue")

        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        # AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        # Instance
        instance = ec2.Instance(self, "Instance",
                                instance_type=ec2.InstanceType("t2.micro"),
                                machine_image=amzn_linux,
                                vpc=vpc
                                )

