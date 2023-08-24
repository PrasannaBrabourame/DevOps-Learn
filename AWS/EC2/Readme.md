## # **EC2 (Elastic Compute 2)**
Your basic compute resources in AWS and one of the first services that were released.

**Amazon Machine Image (AMI)**
- predefined image, e.g. for Linux or Windows

- you can create your own AMI by launching it with an instance and then extending or modifying it and then saving it as a custom AMI

- contains one or more EBS snapshots or for instance-store-backed AMIs a template for the root volume (operating system, app server, applications, …)

- contains launch permissions for the volumes to attach to the instance after launch

- can be either **EBS-backed** or **Instance Store-backed**

**Purchase Types**
- **On-Demand** — no long-term commitment and a fixed price per second. Use this for short-term, irregular workloads that can’t be interrupted

- **Reserved** — long-term commitment (1 to 3 years). Use for high-uptime requirements at core-infrastructure

- **Spot** — auction-based bidding for unused EC2 resources — very cheap, but workload can be interrupted if your offer falls below market levels

- **Dedicated Host **— entire rack/server dedicated to your account, so no shared hardware — only for very high-security requirements because it’s very expensive

- **Dedicated Instance** — physically isolated at the host level, but may share some hardware with other instances from your AWS account