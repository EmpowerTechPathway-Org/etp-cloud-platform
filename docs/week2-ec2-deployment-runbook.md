Week2: Add EC2 deployment runbook

## Purpose and Scope
Deploy a single AWS EC2 instance using the AWS Management Console with strong security controls and AWS Free Tier cost protections. This runbook ensures least privilege access, minimal exposure to the public internet, and cost-awareness throughout the deployment lifecycle.

---

## Preconditions
- MFA enabled on IAM user account  
- Logged in as IAM user (NOT root)  
- AWS Budget alarm configured  
- Correct AWS region selected (top-right of console)  
- Access to your public IP address (for secure security group configuration)

---

## Console Navigation Steps
1. Log in to the AWS Console  
2. Navigate to **EC2 Dashboard**  
3. Click **Instances** → **Launch instances**  
4. Name your instance (e.g., `week2-ec2-lab`)  
5. Choose AMI  
6. Choose Instance Type  
7. Configure Key Pair  
8. Configure Network Settings  
9. Review Summary  
10. Click **Launch Instance**

---

## AMI Reasoning (Amazon Linux 2)
**Selected AMI:** Amazon Linux 2  

**Why:**
- Free Tier eligible  
- Officially supported by AWS  
- Optimized for EC2 performance  
- Secure and lightweight  
- Long-term support and frequent security updates  

Amazon Linux 2 provides a stable, secure baseline for testing web workloads.

---

## Instance Type Reasoning (t2.micro)
**Selected Type:** t2.micro  

**Why:**
- Eligible under AWS Free Tier (750 hours/month)  
- 1 vCPU, 1 GiB RAM (sufficient for lightweight web server testing)  
- Low-cost burstable performance model  

This instance size prevents unnecessary compute spend.

---

## Key Pair Guidance
- Create a new key pair (RSA, .pem format)  
- Download and securely store the private key  
- Do NOT commit key files to GitHub  
- Restrict file permissions locally:  
```bash
chmod 400 your-key.pem
