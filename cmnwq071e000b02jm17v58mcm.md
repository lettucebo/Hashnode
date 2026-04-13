---
title: "[IT 鐵人賽] ASP.NET Core 與 Log 紀錄和追蹤的愛恨交織 - Day 04 - Elmah - 01"
datePublished: Fri Oct 19 2018 15:04:16 GMT+0000 (Coordinated Universal Time)
cuid: cmnwq071e000b02jm17v58mcm
slug: it-aspnet-core-log-day-04-elmah-01
canonical: https://medium.com/@abc12207/it-%E9%90%B5%E4%BA%BA%E8%B3%BD-asp-net-core-%E8%88%87-log-%E7%B4%80%E9%8C%84%E5%92%8C%E8%BF%BD%E8%B9%A4%E7%9A%84%E6%84%9B%E6%81%A8%E4%BA%A4%E7%B9%94-day-04-elmah-01-c1546628b1c
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070454149/a0702417-5357-4217-a572-7ba53ea36735.png

---

---

#### .NET Core Logging- Elmah 01

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070454149/a0702417-5357-4217-a572-7ba53ea36735.png)

Elmah 是我最一開始使用的 Log 工具，基本上它的功能就是將應用程式所有發生的錯誤記錄下來，不需要改變程式架構，而且又有介面可以觀看，十分的方便；它從 WebForm 時代就有了，到了 MVC 也是運作的很好，那這邊就來介紹一下 Elmah 要如何在 ASP.NET Core 中使用 (.NET Core 也可使用)。

不過很可惜的，目前並沒有釋出官方的 Elmah for .NET Core，不過有一個新專案： [ElmahCore](https://github.com/ElmahCore/ElmahCore) By [@barestan](https://github.com/barestan)，到目前為止最後更新時間是 2017–12–08，希望還會繼續維護。

> 有一網友 Fork 了專案持續維護：<https://github.com/funky81/ElmahCore>，推薦可以使用此版

---

#### 設定與使用

首先先從 [Nuget](https://www.nuget.org/) 安裝 [ElmahCore](https://www.nuget.org/packages/ElmahCore/)

> 因為 Nuget 原作者已經沒有再更新了，所以推薦使用 <https://github.com/funky81/ElmahCore> 自己 Build 一版出來

```
Package Explorer: Install-Package ElmahCore
DotNet CLI: dotnet add package ElmahCore
```

安裝完畢後，於 `Startup.cs` 分別於 `ConfigureServices` 中加入 `service.AddElmah();` 與 `Configure` 中加入 `app.UseElamh();`

這樣就設定完成了，夠簡單吧

---

接下來我們就來直接測試一下，在 HomeController 中的 Index 裡，故意產生 Exception

執行後，並故意瀏覽錯誤頁面，就已經開始記錄例外了

預設的查看的介面網址為：**https://{url}:{port}/elmah**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070456486/36bc8ee7-adcc-47a9-ae38-f1d92cbf2b9b.png)

---

#### 介面介紹

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070458444/5b70b732-6641-440f-b81f-c089df1c1049.png)

1. RSS Feed: 讓你可以使用 RSS 來訂閱錯誤訊息，透過 RSS Reader 來接收每一筆最新例外資訊。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070464122/ea0be9d9-3f44-4c1b-ae96-057c5d062630.png)

2. RSS Digest: 同樣也是提供 RSS 訂閱，但是此 RSS 所提供的資訊為每日的例外狀態統整資訊。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070465479/43f221bf-55c3-430e-8623-c5218491c4a9.png)

3. Download log: 可以所有的 Log 匯出成 .csv 檔案，供使用別的軟體或工具進行分析，或是提供給開發人員處理。

4. Host: 發生例外錯誤的主機，如果系統是同時 RUN 在多台時，就可以快速分辨是哪一台主機產生了例外。

5. Code: 錯誤代碼。

6. Type: 例外類型。

7. User: 已登入的使用者，若發生的例外是在使用者已經登入的情況之下，它還可以把登入的使用者名稱列出來，以供日後追蹤。

8. Error: 例外詳細資訊，點 `Details` 可以看更多，甚至還有 Call Stack 以及相關變數，完全可以知道到底是哪個 Function 產生了例外

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070468151/f0b9fdcc-4394-446e-a32d-7e2f5bdca39b.png)

---

#### 確保 Elmah 頁面安全

在上面的範例中，Elmah 是可以公開被存取的，這肯定不合資訊安全，所以 Elmah 有提供了一點點的資訊安全

修改 Elmah 介面路徑
只需要在`Startup.cs` 之 `ConfigureServices` 加入 `service.AddElmah();` 時，加入相關設定即可完成

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070469498/062f5da5-62f0-4b76-a3c2-55ae222caa2d.png)

不過很可惜的，現在看起來還沒登入驗證的支援，如果有興趣的或許可以去貢獻看看

---

下一篇來介紹把 Log 放到不同的儲存體上，以及如何過濾 Log