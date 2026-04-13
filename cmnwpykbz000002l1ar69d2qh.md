---
title: "Dapper 使用 Microsoft.SqlServer.Types 找不到正確版本問題"
datePublished: Thu Mar 02 2017 13:06:46 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpykbz000002l1ar69d2qh
slug: dapper-microsoftsqlservertypes
canonical: https://medium.com/@abc12207/dapper-%E4%BD%BF%E7%94%A8-microsoft-sqlserver-types-%E6%89%BE%E4%B8%8D%E5%88%B0%E6%AD%A3%E7%A2%BA%E7%89%88%E6%9C%AC%E5%95%8F%E9%A1%8C-a7848b95b6e5
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070131774/5ef517cd-dd19-488d-9488-abddb1c0f981.png

---

---

Microsoft.SqlServer.Types-could-not-load-file-or-assembly-correct-version

```
Could not load file or assembly 'Microsoft.SqlServer.Types, Version=10.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070131774/5ef517cd-dd19-488d-9488-abddb1c0f981.png)

### 緣由

最近因為工作緣故一直都有在處理地理資料，那最常用的 SQL Server 也有提供地理資料型態，SQL Server 提供了兩種關於地理資料型態，分別為： gepgraphy 與 geometry，這兩種的差別我當初也好奇了很久，之後再寫一篇文章來說明，後來採用的 geography 作為儲存的型態

使用 Dapper 作為存取資料庫的方法，因為使用到 geography 的關係，所以裝了 [Microsoft.SqlServer.Types](http://www.nuget.org/packages/Microsoft.SqlServer.Types/)，這又是一段故事，容後再說

使用的 SQL Server 是 **2012**，所以安裝的版本就選了 **11.0.2**

開發測試一切都沒問題，結果一部署上去，有用到地理資料的部分就爆了 Exception，錯誤訊息節錄如下

```
Could not load file or assembly 'Microsoft.SqlServer.Types, Version=10.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
```

到這邊就令人百思不解，我明明就安裝的是 SQL Server 2012，Nuget 版本也都選 11.0.2，怎麼會突然爆出一個找不到 Microsoft.SqlServer.Types, Version=10.0.0.0 的錯誤，想了一陣子確定沒用到關於 SQL Server 2008 系列的東西，於是就上網找了找

找到了這篇：[Could not load file or assembly ‘Microsoft.SqlServer.Types](http://stackoverflow.com/questions/1625768/could-not-load-file-or-assembly-microsoft-sqlserver-types)

### 原因與解法

深入了看一下，因為使用了 SQL Server Spatial Types，應用程式在伺服器上找不到相對應的 Dll，所以就出錯了

解決方法很簡單，微軟有提供 SQL Server System CLR Types 安裝檔，[最佳回答](http://stackoverflow.com/a/1625779/1799047)的連結已經更換了，微軟直接把他切成一個一個的安裝檔，這樣就不用只為了一個功能還要安裝所有檔案

我在後面的[回答](http://stackoverflow.com/a/42522338/1799047)整理了連結

Microsoft® System CLR Types for SQL Server® 2008 R2:

[X86 Package(SQLSysClrTypes.msi)](http://go.microsoft.com/fwlink/?LinkID=188391&clcid=0x409)

[X64 Package (SQLSysClrTypes.msi)](http://go.microsoft.com/fwlink/?LinkID=188392&clcid=0x409)

安裝完畢後應該就可以生效，若是沒生效重開機即可

### 備註

根據不同的版本，需要下載相對應的 System CLR Types

版本對照表：[如何判斷 SQL Server 及其元件的版本、版次及更新層級](https://support.microsoft.com/zh-tw/help/321185/how-to-determine-the-version--edition-and-update-level-of-sql-server-a)