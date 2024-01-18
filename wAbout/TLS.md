---
title: Interject TLS for HTTPS
filename: "TLS.md"
layout: custom
keywords: [Security, Privacy, Data Governance]
headings: []
links: []
description: Overview of Interject security measures and protocols.
---
* * *

For Interject v2.3.34.0 and earlier, the default is TLS 1.1. This can be changed to TLS 1.2 by using the following method:

- Reconfigure TLS via Settings
 - In the Interject ribbon menu click 'Advanced Menu' if the Online Admin section is not displayed.
 - Click 'System' and in the dropdown select 'Configure Install'
 - Enter the following code in the form field: TLS1.2
 - Click 'Continue'
 - Restart Excel (make sure all instances are closed)
 - TLS 1.2 should now work
- Use Interject v2.4.0.0+ (TLS 1.2 is the default for all version here forward)