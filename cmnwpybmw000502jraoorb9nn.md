---
title: "ASP.NET Identity Ouath 登入 null 問題"
datePublished: Tue Feb 28 2017 05:22:21 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpybmw000502jraoorb9nn
slug: aspnet-identity-ouath-null
canonical: https://medium.com/@abc12207/asp-net-identity-ouath-%E7%99%BB%E5%85%A5-null-%E5%95%8F%E9%A1%8C-9c4022e7a8e6
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070108084/8fd55a36-961b-4323-a94e-1f46ea908aa9.png

---

---

aspnet-identity-null-reference-logininfo-is-null

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070108084/8fd55a36-961b-4323-a94e-1f46ea908aa9.png)

最近有幾個案子要辦 Facebook 行銷活動，因為都是小案子，所以就直接用了 Visual Studio 2015 內建的範本，其中就包含了 ASP.NET Identity 功能

在開發與測試時都非常順利，然後就上線了

於上線運作階段偶爾會接到使用者反映使用 Facebook 登入時，點選登入後經過 Facebook 驗證成功，可是又回到了登入頁面

於初期完全無法根據特定條件重現問題，偶爾會發現此問題但是下一次嘗試時登入卻又成功

### 原因

根據多方 GOOGLE 後，使用關鍵字：asp.net identity, login, owin, null 在 StackOverflow 查到了 [ASP.NET MVC 5 (VS2013 final): Facebook login with OWIN fails (loginInfo is null)](http://stackoverflow.com/a/21439834)

在此篇文章中有一個連結 [ASP.NET\_SessionId + OWIN Cookies do not send to browser](http://stackoverflow.com/a/21234614) (此篇講解為什麼會出問題，並附上落落長的分析，但等等會提供佛心大大提供非常直接的解決方案)

### 一些背景知識

以下說明根據的 Assembly Versions 為：

* Microsoft.Owin, Version=2.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
* Microsoft.Owin.Host.SystemWeb, Version=2.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
* System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a

OWIN 使用自己的抽象化方式來實作 Cookie (Microsoft.Owin.ResponseCookieCollection)，它實作的方式是直接將 Response Header 集合包起來並從而更新 Set-Cookie Header OWIN ASP.NET Host (Microsoft.Owin.Host.SystemWeb) 直接將 System.Web.HttpResponse 與 Header 集合整個包起來 因此當 OWIN 建立新 Cookie 時，Response 的 Set-Cookie Header 直接被OWIN改成OWIN自己的格式

但 ASP.NET 針對 Response Cookies 也有自己的抽象化方式，可以透過 sealed class System.Web.HttpCookieCollection 中之 System.Web.HttpResponse.Cookies 屬性與實作略為窺知 它的實作方法並不會直接改變 Set-Cookie Header，而是使用了少數最佳化過的 Internal Notifications 來將狀態的變更寫入 Response 物件

在 Requert 的生命週期的特定時間點中，當 HttpCookieCollection 狀態變更完畢 (System.Web.HttpResponse.GenerateResponseHeadersForCookies()) 且 Cookies 已經序列化到 Set-Cookie Header 中 假如這個集合正好處於某些特殊狀態下時，整個 Set-Cookie Header 會先被整個清空後，才根據集合中的 Cookies 重新建立

ASP.NET Session 的實作是使用 System.Web.HttpResponse.Cookies 屬性來儲存 ASP.NET\_SessionId Cookie，且在 ASP.NET Session 的模組 (System.Web.SessionState.SessionStateModule) 中有做了一些最佳化，透過一個靜態屬性名為：s\_sessionEverSet，根據這個名字就可以大概一窺它的功用；假設你有將任何資料存入至 Session State 中，那麼這個模組就會自動幫你在每個 Request 中多做一點額外的處理

### 回到問題

透過以上的一些知識就可以來解釋這些靈異現象

#### Case 1. 從沒使用過Session

System.Web.SessionState.SessionStateModule, s\_sessionEverSet 屬性為 false 沒有任何 session id 被 session state 模組產生且 System.Web.HttpResponse.Cookies 集合狀態沒有偵測到任何變更 在這情況下，OWIN Cookies被正確送出給瀏覽器並成功登入

#### Case 2. Session 在應用程式某處被使用過, 但使用者尚未嘗試登入過

System.Web.SessionState.SessionStateModule 與 s\_sessionEverSet 屬性為 true Session Id 由 SessionStateModule 產生，並將 ASP.NET\_SessionId 加入至 System.Web.HttpResponse.Cookies 集合中，但在稍後將因 Session 是空的所以被清除掉 在這狀況下 System.Web.HttpResponse.Cookies 集合狀態被偵測到改變，因此 Set-Cookie Header 先被清除後再次將 Cookies 重新序列化到 Header， 因此這樣可以得知 OWIN Response Cookies 其實已經不見了，使用者被判斷為沒有登入並重新導向到登入頁面

#### Case 3. 再登入之前已經使用過 Session

System.Web.SessionState.SessionStateModule 與 s\_sessionEverSet 屬性為 true Session Id 由 SessionStateModule 產生，並將 ASP.NET\_SessionId 加入至 System.Web.HttpResponse.Cookies 集合中 因為 System.Web.HttpCookieCollection 內部的最佳化機制，System.Web.HttpResponse.GenerateResponseHeadersForCookies() Set-Cookie Header 並沒有立刻被清除，而只有被更新 在這狀況下 OWIN authentication cookies 與 ASP.NET\_SessionId cookie 都被正確送出，因此登入成功

`看到這邊你就會突然知道為什麼之前的搜尋結果都說先用 Session 再登入就會成功，這真的是知其然而不知所以然阿！`

#### 更普通的說

從上面的說明可以看出這問題不只發生在 ASP.NET session 上，只要你是透過 Microsoft.Owin.Host.SystemWeb 來 Hosting OWIN ，你的 System.Web.HttpResponse.Cookies 都會有機會發生問題

舉例來說 以下為正常運作範例

正常運作

但以下範例就不會正常運作且 OwinCookie 也會遺失

不會正常運作

`以上範例使用 VS2013, IISExpress and 預設 MVC project 範本進行驗證`

### 解決方法

在這邊有個大神直接寫了nuget package出來：<http://stackoverflow.com/a/26978166>

nuget package

安裝nuget套件後，直接在ConfigureAuth方法上設定

```
app.UseKentorOwinCookieSaver();
```

如此乾淨俐落的解決，問題再也沒出現過