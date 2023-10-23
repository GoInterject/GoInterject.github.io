---
layout: custom
title:  Java API Setup
keywords: [data api, java, setup, spring framework]
description: Shows how to setup an INTERJECT Java data api.
---

## Overview

Interject allows data flow from custom sources through a web API. The Interject Java API is built upon Java and the [Spring Framework](https://spring.io/projects/spring-framework){:target="_blank"}{:rel="noopener noreferrer"}.

### Requirements


* [Java](https://www.oracle.com/java/technologies/downloads/){:target="_blank"}{:rel="noopener noreferrer"}
* [Maven](https://maven.apache.org/download.cgi){:target="_blank"}{:rel="noopener noreferrer"}

###  **Get the Code**

With Git, you can clone the repository directly to your system:

```git
git clone https://github.com/GoInterject/ids-java-api.git
```

**Note:** If this repo is private and you need access, please [contact us](mailto:help@gointerject.com). It will be public soon.

Alternatively you can download the zip file and unpack manually:

![](/images/API/JavaDownloadZip.png)
<br>

### Setup

Open a terminal and navigate to the "ids-java-api" directory where the repo was installed. Then navigate to the "interject-webapp" directory.

Download dependencies:

```bash
mvn dependency:copy-dependencies
```

Create a clean build of the Rest API:

```bash
mvn clean package
```

### Run API

To run with Maven:

```bash
mvn spring-boot:run
```

To run with Java:

```bash
java -jar "./target/interject-webbapp-1.0.0-SNAPSHOT.jar"
```

**Note:** For more information, view the Readme in the parent directory or the doc files in the docs folder of the repo.