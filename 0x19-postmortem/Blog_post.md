![Postmortem Image](../../Pictures/Screenshots/postmortem.png)


Postmortem: E-commerce Platform Outage
Issue Summary

Duration: June 8, 2024, 1:00 PM UTC - 4:00 PM UTC
Impact: Our checkout service was completely down for three hours. Users couldn't complete their purchases, affecting about 75% of our active users at the time.
Root Cause: The issue stemmed from a misconfigured database index that caused performance degradation under heavy load, ultimately making the database unresponsive.
Timeline

    12:45 PM UTC: We received an alert from our monitoring system about high response times on the checkout service.
    12:50 PM UTC: Our engineers began investigating, initially suspecting a load balancer issue.
    1:00 PM UTC: It became clear that the checkout service was fully down, with users unable to complete any purchases.
    1:10 PM UTC: The issue was escalated to the database team when it appeared that database queries were timing out.
    1:30 PM UTC: We initially thought recent changes in the checkout microservice deployment might be the cause, but this was a false lead.
    2:00 PM UTC: Deeper analysis of the database logs showed increased query times and lock contention.
    2:30 PM UTC: We identified that a new index on the orders table was causing the issue under high load.
    3:00 PM UTC: The database team began rolling back the index changes.
    3:30 PM UTC: Database performance started to improve, and services began to recover.
    4:00 PM UTC: Full functionality was restored, and we continued to monitor for stability.

Root Cause and Resolution

Root Cause: The new database index, meant to optimize read queries for reporting, caused severe lock contention during peak transaction loads. This slowed down write operations to the point where the database became unresponsive.

Resolution: To fix the issue, we:

    Rolled back the problematic index on the orders table.
    Reviewed our indexing strategy to ensure it was suitable for high transaction loads.
    Conducted load testing to confirm the stability of the changes.

Corrective and Preventative Measures

Improvements:

    We need better management of database indexes, ensuring they are properly tested under load before deployment.
    Enhanced monitoring to catch query performance issues earlier.
    Revised deployment processes to include rigorous performance testing for any database schema changes.

Tasks:

    Patch Database Server: Apply the latest updates to ensure optimal performance.
    Add Query Performance Monitoring: Set up detailed monitoring and alerts for database query performance.
    Review and Optimize Indexes: Conduct a thorough review and optimization of our current database indexes.
    Load Testing: Develop and implement a load testing framework for database changes.
    Team Training: Provide training for our engineers on database indexing and performance tuning.
    Incident Response Plan: Update and rehearse our incident response plan to improve our reaction time and coordination in future incidents.

This incident was a tough lesson for us, but we've learned from it and are taking steps to ensure it doesn't happen again. Our goal is to provide a reliable and seamless experience for our users, and we're committed to making that happen.
