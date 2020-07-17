from aws_cdk import (
    aws_s3 as _s3,
    aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    core
)


class Cdkteht3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3 = _s3.Bucket(self, "Mervis3bucket")

        queue = sqs.Queue(self, "MerviSQSQueue")

        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        sg_ec2 = ec2.SecurityGroup(self, id="sg_ec2",
                                   vpc=vpc,
                                   security_group_name="sg_ec2"
        )
        # sg_ec2.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))

        instance = ec2.Instance(self, "Instance",
                                instance_type=ec2.InstanceType("t2.micro"),
                                machine_image=amzn_linux,
                                vpc=vpc,
                                security_group=sg_ec2
        )

        sg_alb = ec2.SecurityGroup(self, id="sg_alb",
                                   vpc=vpc,
                                   security_group_name="sg_alb"
        )
        sg_alb.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))

        sg_ec2.connections.allow_from(
            sg_alb, ec2.Port.tcp(80), "Ingress")

        lb = elbv2.ApplicationLoadBalancer(self, "ALB",
                                           vpc=vpc,
                                           security_group=sg_alb,
                                           internet_facing=True
        )



