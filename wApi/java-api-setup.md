---
layout: custom
title:  Java API Setup
filename: "java-api-setup.md"
keywords: [data api, web api, java, setup, spring framework]
headings: ["Overview", "Requirements", "Get the Code", "Setup", "Run API", "Change Host and Port", "Development Docs", "Interject Docs"]
links: ["https://spring.io/projects/spring-framework", "https://www.oracle.com/java/technologies/downloads/", "https://maven.apache.org/download.cgi", "https://github.com/GoInterject/ids-java-api.git", "mailto:help@gointerject.com", "https://github.com/GoInterject/ids-java-api/archive/refs/heads/main.zip", "/wFunctions/jColumnDef.html", "/wPortal/Data-Portals.html#overview-of-parameters", "/wFunctions/ReportFixed.html", "/wFunctions/ReportRange.html", "/wFunctions/ReportSave.html", "/wFunctions/ReportVariable.html", "/wDeveloper/L-Dev-Error-Handling.html"]
image_dir: "API"
images: [
	{file: "JavaDownloadZip", type: "png", site: "Github", cat: "ids-java-api", sub: "", report: "", ribbon: "", config: ""}
	]
description: Shows how to setup an INTERJECT Java data api.
---

## Overview

Interject allows data flow from custom sources through a web API. The Interject Java API is built upon Java and the [Spring Framework](https://spring.io/projects/spring-framework){:target="_blank"}{:rel="noopener noreferrer"}.

### Requirements

* [Java](https://www.oracle.com/java/technologies/downloads/){:target="_blank"}{:rel="noopener noreferrer"}
* [Maven](https://maven.apache.org/download.cgi){:target="_blank"}{:rel="noopener noreferrer"}

###  Get the Code

With Git, you can clone the repository directly to your system. Navigate to the desired directory and run the following command:

```git
git clone https://github.com/GoInterject/ids-java-api.git
```

<br>
<blockquote class=highlight_note>
<b>Note:</b> If this repo is private and you need access, please <a href="mailto:help@gointerject.com">contact us</a>. It will be public soon.
</blockquote>
<br>

Alternatively you can download the [zip file](https://github.com/GoInterject/ids-java-api/archive/refs/heads/main.zip){:target="_blank"}{:rel="noopener noreferrer"} and unpack manually:

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

<blockquote class=highlight_note>
<b>Note:</b> For more information, view the Readme in the parent directory or the doc files in the docs folder of the repo.
</blockquote>
<br>

### Making an API Call
Once the API is running, you can test it with a simple health check request. Open a terminal and use curl:

```bash
curl http://127.0.0.1:8080/api/health
```

A successful response confirms the API is working:
```json
{
  "status": "OK"
}
```
> **Alternative 1: Using PowerShell**
>
> In PowerShell, `curl` is an alias for `Invoke-WebRequest`, which returns a detailed object. For testing REST APIs, it's better to use the `Invoke-RestMethod` cmdlet, which automatically handles JSON.
>
> ```powershell
> Invoke-RestMethod http://127.0.0.1:8080/api/health
> ```
>
> This returns a PowerShell object. To use the literal curl application, specify `curl.exe`.

---

> **Alternative 2: Using Postman**
>
> 1. Open a new request tab (click the **+** icon).
> 2. Ensure the HTTP method is set to **GET**.
> 3. In the URL bar, enter: `http://127.0.0.1:8080/api/health`
> 4. Click the blue **Send** button.
> 5. In the response pane below, you will see a green **Status: 200 OK** and the JSON body.

### Change Host and Port

To change the host and port number, simply change the values in the `application.yaml` file:

```yaml
server:
      port: 8080
      address: 127.0.0.1
```


### Development Docs

There are docs in the repo pertaining to development. They are found in the `asciidoc` directory:

| File | Description |
|---|---|
| add-new-endpoint | How to add a new endpoint |
|local-development | Setting up a local development environment |
|local-test | How to run and create new test cases |
| sql-request-example | An example body of a SQL request |
| swagger-ui| Information about the Swagger UI |

### Interject Docs

There are docs in the repo pertaining to setting up Interject reports and functions. They are found in the `examples` directory:

| File | Description |
|---|---|
| example.xlsx | An example Excel workbook that interacts with the API endpoints |
| formula_jcolumndef | How to set up the [jColumnDef](/wFunctions/jColumnDef.html) formula |
| portal_parameters | How to set up Interject [parameters](/wPortal/Data-Portals.html#overview-of-parameters) |
| report_fixed | How to set up an Interject [ReportFixed](/wFunctions/ReportFixed.html) |
| report_range | How to set up an Interject [ReportRange](/wFunctions/ReportRange.html) |
| report_save | How to set up an Interject [ReportSave](/wFunctions/ReportSave.html) |
| report_variable | How to set up an Interject [ReportVariable](/wFunctions/ReportVariable.html) |
| sql_data_connection | How to work with the `SqlDataConnection` interface to set up a SQL data connection and controller |
| user_message | How to send [messages](/wDeveloper/L-Dev-Error-Handling.html) back to the Interject from the API |
