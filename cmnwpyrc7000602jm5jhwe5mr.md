---
title: "在分開的 Class Library 專案中使用 Entity Framework Core Database First"
datePublished: Wed Dec 13 2017 16:01:01 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpyrc7000602jm5jhwe5mr
slug: class-library-entity-framework-core-database-first
canonical: https://medium.com/@abc12207/entity-framework-core-database-first-%E5%9C%A8%E5%88%86%E9%96%8B%E7%9A%84-class-library-%E5%B0%88%E6%A1%88%E4%B8%AD-6856652daebd
cover: https://cdn-images-1.medium.com/max/800/1*7NmnGr4WwZNfC13lCnFHGw.png

---

---

#### Entity Framework Core Database First at separate class library project

公司有一個新的專案，不大也不小，想說剛好用來上手一下 ASP.NET Core，結果還沒開始就已經撞得滿頭腦，差點就要放棄了，幸好在堅持一下就嘗試出來了，這件事花了我一整天搜尋與嘗試，特地紀錄一下

首先必須要說的是 Entity Framework Core Database First 的方式，工具對其之支援真是有夠差，完全必須手動新增某些關鍵設定才有辦法成功執行

> 環境：Visual Studio 2017 Update 5.1、 .Net Framework 4.7.1 與 .NetCore 2.0

首先當然是新增一個 .NetCore Class Library 專案

![](https://cdn-images-1.medium.com/max/800/1*7NmnGr4WwZNfC13lCnFHGw.png)

新增 .NetCore Class Library 專案

專案新增完畢後，先進行必要的 nuget package 安裝，安裝以下四個 nuget package，**安裝版本請務必選擇相同版本**，我這邊安裝的都是 2.0.1

安裝完後，接下來還有一個 nuget package 需要安裝，但其特殊性必須額外拿出來說

> Install-Package Microsoft.EntityFrameworkCore.Tools.DotNet

先來看一下安裝需求，2.0.1 版本所需求之 Microsoft.NETCore.App 為大於等於 2.0.3，但是一開始新增 Class Library 專案之 Microsoft.NETCore.App 版本為 2.0.0，所以無法安裝

> 20171213 實驗時，.NetCore 2.1.0-preview2-25624-02 連空專案都 Build 不過，直接放棄

![](https://cdn-images-1.medium.com/max/800/1*MJOhwUNS7balUL8cBtZnug.png)

Microsoft.EntityFrameworkCore.Tools.DotNet

想要使用 Nuget Package 管理工具升級時，發現 Microsoft.NETCore.App 被鎖住無法升級或是降級

![](https://cdn-images-1.medium.com/max/800/1*0NRgkRl8GABNLVchZl1Hjg.png)

Microsoft.NETCore.App

只能用文字編輯器打開 ClassLibrary1.csproj 直接編輯，將其版本修改為 2.0.3，如下並存檔

修改完畢後，就可以安裝 Microsoft.EntityFrameworkCore.Tools.DotNet Package 了

安裝完畢後，再次用文字編輯器打開 ClassLibrary1.csproj 進行編輯，這次要加的是關係到 Entity Framework Core 是否能正確動作的關鍵設定：**DotNetCliToolReference**

加入兩行 **DotNetCliToolReference** 後，Entity Framework Core 就可以正確動作了

![](https://cdn-images-1.medium.com/max/800/1*JT-sKe-Qqdso5z7asRyH0Q.png)

Complete

如果還有問題的話，可以去安裝 .NET Core CLI，有時會是工具連組態都沒有設定好

> 就因為 Visual Studio 不會自動幫你加入 DotNetCliToolReference 就花費了一整天的時間..

在 Visual Studio 內使用 Package Manager Console 之指令

```
Scaffold-DbContext "Connection String" Microsoft.EntityFrameworkCore.SqlServer -outputdir Models
```

在 CMD 視窗之指令

```
dotnet ef dbcontext scaffold "Connection String" Microsoft.EntityFrameworkCore.SqlSe rver --output-dir Models
```

參考：

[**No executable found matching command "dotnet-ef" even after adding CLI · Issue #8996 · aspnet…**
*I want to Migrate my Database with Models. I am using EF Core 2.0 Preview. dotnet ef migrations add InitialCreate…*github.com](https://github.com/aspnet/EntityFrameworkCore/issues/8996 "https://github.com/aspnet/EntityFrameworkCore/issues/8996")

[**Getting Started on ASP.NET Core - Existing Database - EF Core**
*In this walkthrough, you will build an ASP.NET Core MVC application that performs basic data access using Entity…*docs.microsoft.com](https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/existing-db "https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/existing-db")