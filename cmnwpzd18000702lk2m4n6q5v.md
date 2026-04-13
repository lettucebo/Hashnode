---
title: "ASP.NET Core 如何設定 ASPNETCORE_ENVIRONMENT 變數"
datePublished: Fri Mar 23 2018 10:22:09 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzd18000702lk2m4n6q5v
slug: aspnet-core-aspnetcoreenvironment
canonical: https://medium.com/@abc12207/asp-net-core-%E5%A6%82%E4%BD%95%E8%A8%AD%E5%AE%9A-aspnetcore-environment-%E8%AE%8A%E6%95%B8-b0e17e87c3e
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070304111/1af19266-4d6c-4d8a-98ab-6b1c626da871.png

---

---

#### ASP.NET Core How To Set ASPNETCORE\_ENVIRONMENT Variable

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070304111/1af19266-4d6c-4d8a-98ab-6b1c626da871.png)

asp.net core

在我將我寫完的 ASP.NET Core 網站佈署到正式環境 (Production Environment) 後，發生了在我的測試環境中沒有發生過的 Exception，想要看錯誤訊息，但是又不像以前 ASP.NET 時代加上 `CustomErrors` 就能解決掉，這篇就紀錄一下如何透過設定 `ASPNETCORE_ENVIRONMENT` 來觀看錯誤訊息

其實簡單來說就是將 ASP.NET Core 的 Environment 改成 `Development` 來達到此目標

直接開啟 web.config 於 aspNetCore 之 environemntVariable 區段中，加入以下參數即可

```
<environmentVariable name="ASPNETCORE_ENVIRONMENT" value="Development" />
```

完整範例 web.config 如下

參考

[**how to set ASPNETCORE\_ENVIRONMENT to be considered for publishing an asp.net core application?**
*when i publish my asp.net core web application to my local file system, it always takes the production-config and the…*stackoverflow.com](https://stackoverflow.com/a/41551429/1799047 "https://stackoverflow.com/a/41551429/1799047")