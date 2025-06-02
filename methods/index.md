---
layout: page
title: HCI Evaluation Methods
permalink: /methods/
---

# HCI Evaluation Methods

This section contains our comprehensive collection of Human-Computer Interaction evaluation methods, organized by category and approach.

## Categories

### 🔬 [Quantitative Methods](quantitative/)
Data-driven approaches that provide measurable, statistical insights into user behavior and system performance.

### 🎭 [Qualitative Methods](qualitative/)
User-centered approaches that provide deep insights into user experiences, motivations, and contexts.

### 📱 [Wearable-Specific Methods](wearable/)
Specialized evaluation techniques designed for wearable devices and ubiquitous computing systems.

### 🏢 [Field Studies](field/)
Methods for evaluating HCI systems in real-world, naturalistic environments.

### 🧪 [Laboratory Studies](laboratory/)
Controlled evaluation methods conducted in laboratory settings for precise measurement and comparison.

## All Methods

{% for method in site.methods %}
- [{{ method.title }}]({{ method.url | relative_url }}) - {{ method.description }}
{% endfor %}

## Contributing

This collection is based on research from:
- **ACM Digital Library** - Primary source for HCI research
- **IEEE Xplore** - Additional technical and engineering perspectives
- **CHI Conference Proceedings** - Latest developments in HCI evaluation
- **UIST, UbiComp, and other top-tier venues** - Specialized evaluation methods

---

*Methods are continuously updated to reflect current best practices in HCI evaluation.*