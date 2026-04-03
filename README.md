# Knowledge Parser

A tool for parsing websites. 
- Goes through the address graph of the site. 
- During the crawl, it can go deeper relative to the initial route or bypass all links of the same domain.

---
## Stack

#### Architecture

- MVVM

#### Technology

- *Platform*: .NET 10
- *DOM Analysis*: AngleSharp
- *Test*: xUnit

---
## Quick start

Dependency recovery:
```bash
dotnet restore
```

Building a solution:
```bash
dotnet build --configuration Release --project KnowParser/KnowParser.csproj
```

`KnowParser\bin\Release` - the compiled application will be here.

---
## Screenshots

<center><image src="assets/main_window.png"/></center>
