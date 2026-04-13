---
title: "在分開的 Class Library 專案中使用 Entity Framework Core 進行 Migrations"
datePublished: Wed Dec 27 2017 12:10:41 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpyx83000802jmbvrc0mal
slug: class-library-entity-framework-core-migrations
canonical: https://medium.com/@abc12207/%E5%9C%A8%E5%88%86%E9%96%8B%E7%9A%84-class-library-%E5%B0%88%E6%A1%88%E4%B8%AD%E4%BD%BF%E7%94%A8-entity-framework-core-code-first-%E9%80%B2%E8%A1%8C-migrations-a621aa6fc2e5
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070201858/60d1fdbf-0bc8-4629-99ee-006336b1d83b.png

---

---

#### Entity Framework Core Migrations at separate class library project Implement IDesignTimeDbContextFactory

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070201858/60d1fdbf-0bc8-4629-99ee-006336b1d83b.png)

Entity Framework Core Database First 根據官方資料目前尚未正式支援 Many-to-Many ([GitHub issue 1368](https://github.com/aspnet/EntityFrameworkCore/issues/1368))，有 Workround 但是不漂亮，所以就乾脆放棄 Database First 方式，改回來用 Code First，那遇到的問題又重頭了，怎麼在分開的 Class Library 專案中使用 Entity Framework Core Code First，這邊就簡單紀錄一下

Code First 的方式當然是一模一樣，所以這邊就不多介紹了，可以參考，但是在 Add Migration 或是 Update Database 時就會出現以下錯誤訊息

> Unable to create an object of type ‘MmsFactoryCoreContext’. Add an implementation of ‘IDesignTimeDbContextFactory’ to the project, or see <https://go.microsoft.com/fwlink/?linkid=851728> for additional patterns supported at design time.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070204154/97e5bf40-be76-46ae-b17d-fd2bd01a6cb1.png)

IDesignTimeDbContextFactory

#### 解決方法

簡單來說，我們要假裝這支 Class Library 是 .NetCore App

首先我們先如同 Console App 一樣，新增 Program.cs 檔案於根目錄下

我們需要先指定資料庫連線字串，當然直接寫死在程式裡也可以，但是身為有素質的程式人，怎麼可以把東西寫死，還是於根目錄新增 appsettings.json，裏面包含了資料庫連線字串

然後然後我們就可以開始實作 IDesignTimeDbContextFactory 介面，用途就是用來建立 DbContext，這邊就取巧不再開新檔案，而是直接放在 Program.cs 裡

其中用到 Configration 相關組件，所以需要安裝以下 Nuget

* Microsoft.Extensions.Configuration
* Microsoft.Extensions.Configuration.FileExtensions
* Microsoft.Extensions.Configuration.Json

到此就完成了所有前置步驟，可以開始下指令了

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070205996/27ec0b2e-3976-47b0-9227-7d1ec3b89c29.png)

Complete

參考

[**CodingBlast**
*Solution to the EntityFramework Core issue - Add an implementation of 'IDesignTimeDbContextFactory' to the project.*codingblast.com](https://codingblast.com/entityframework-core-idesigntimedbcontextfactory/ "https://codingblast.com/entityframework-core-idesigntimedbcontextfactory/")

[**Entity Framework Core Migrations for Class Library Projects**
*Entity Framework Core 1.0.0 RTM still does not support migrations for class library projects. If you're like me and…*benjii.me](http://benjii.me/2016/06/entity-framework-core-migrations-for-class-library-projects/ "http://benjii.me/2016/06/entity-framework-core-migrations-for-class-library-projects/")