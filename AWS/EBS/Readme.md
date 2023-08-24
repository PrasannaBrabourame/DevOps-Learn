## # **Elastic Block Storage (EBS)**

- Virtual file system drive

- can’t be used simultaneously at several instances: only one per time (not a network drive)

- you can take snapshots of it

- if the EBS volume is the root volume, by default it will be deleted when the instance gets terminated

- non-root volumes will not be terminated after the instance gets terminated

- created in a single region

- for high availability/disaster recovery you need snapshots saved to S3

- Pricing is only for defined storage capacity, not per transferred data

- has several types

- **Cold HDD** — lowest-cost designed for less frequently accessed workloads

- SC1 — up to 250 IOPS (250 MiB/s), 99.8–99.9% Durability

- **Throughput Optimised HDD** — low-cost designed for frequently accessed workloads

- ST1 — up to 500 IOPS (500 MiB/s), 99.8–99.9% Durability

- **General Purpose SSD** — the balance of price and performance

- GP2/GP3 — up to 16.000 IOPS (250–1000MiB/s), 99.8–99.9% Durability

- **Provisioned IOPS** (Input/Output Operations Per Second) — high performance for mission-critical, low-latency, or high-throughput workloads

- IO1/IO2 — up to 64.000 IOPS (1000MiB/s), 99.8–99.9% Durability

- IO2 Block Express — up to 256.000 IOPS (4000MiB/s), 99.999% Durability

- Provisioned IOPS can be attached to multiple EC2 instances — other types do not support this

- most convenient way of creating backups is using the Data Lifecycle Manager to create automated, regular backups