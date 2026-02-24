# Week 2 – Public EC2 Deployment Architecture

## Overview
This conceptual architecture illustrates a **public EC2 deployment** with minimal attack surface, security boundaries, and Zero-Trust principles. It is designed for **Free Tier testing** while following best practices.

---

## Components

### 1. VPC
- Isolated network boundary for all resources  
- CIDR: `10.0.0.0/16`  

### 2. Public Subnet
- Hosts EC2 instances accessible via the Internet  
- CIDR: `10.0.1.0/24`  
- Associated with a **public route table**  

### 3. Internet Gateway (IGW)
- Enables inbound/outbound internet connectivity for the public subnet  

### 4. Route Table
- Public route table points `0.0.0.0/0` to the Internet Gateway  
- Ensures internet reachability only for public resources  

### 5. Security Group
- Acts as a virtual firewall attached to EC2 instance  
- Example rules:
  - SSH (22) → Source: **My IP only**  
  - HTTP (80) → Source: **My IP only**  
- Restricts access to reduce exposure  

### 6. EC2 Instance
- Type: `t2.micro` (Free Tier)  
- AMI: Amazon Linux 2  
- Public IP assigned via subnet auto-assignment  
- Deployed inside public subnet  
- Protected by security group

---

## ASCII Diagram

+-------------------------------+
|          VPC: 10.0.0.0/16     |
|                               |
|  +-------------------------+  |
|  | Public Subnet 10.0.1.0/24| |
|  | +---------------------+ |  |
|  | | EC2 Instance t2.micro| | |
|  | | Security Group: SSH  | | |
|  | | 22 from My IP only   | | |
|  | +---------------------+ |  |
|  +-------------------------+  |
|        |                         |
|        v                         |
|   Internet Gateway (IGW)         |
+-------------------------------+

## Traffic Flow
- **Inbound:** Only SSH/HTTP from My IP  
- **Outbound:** All traffic allowed (default)  
- **Zero-Trust Principle:** Assume all network traffic is untrusted; enforce strict access rules  

---

## Security Boundaries
- VPC isolates resources from other AWS tenants  
- Security group enforces host-level access controls  
- Public subnet allows minimal exposure for testing purposes  
- IAM user access limited by least privilege  

---

## Zero-Trust Notes
- Never use root account for EC2 management  
- Enable MFA for all IAM users  
- Limit security group access to known IPs  
- Monitor CloudTrail and CloudWatch logs for anomalies  

---

**End of Architecture Documentation**
