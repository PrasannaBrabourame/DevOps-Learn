## # **Elastic Load Balancing (ELB)**
Distribute traffic between computing resources.

- comes in four different flavours

- Classic (CLB): oldest types, works on both layer 4 and layer 7 - no longer featured on AWS exams

- Application (ALB): works on layer 7 and routes content based on the content of the request

- Network (NLB): works on layer 4 and routes based on IP data

- Gateway (GLB): works on layer 3 and 4 - mostly used in front of firewalls

- load balancing enhances fault-tolerance as automatically distributes traffic to healthy targets which can also reside in different availability zones

- ELB can be either internet facing (has public IP, needs a public VPC) or internal-only (private VPC, no public IP, can only route to private IP addresses)

- EC2 instances or Fargate tasks can be registered to ELB's target groups