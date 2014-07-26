---
title: Requirements
layout: default
---

These are the resources required for each course. Some of them may be acquired through ADLC if you request them.

Errors here may result when curriculum is changed. Please be dilligent about checking that items are *required*.

The materials listed are for *one student*. Multiply as needed.

{% for course in site.courses %}
### {{ course.course }}
{% for r in course.requirements %}- {{ r }}
{% endfor %}
{% endfor %}
