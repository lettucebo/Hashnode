---
title: "[IT 鐵人賽] ASP.NET Core 與 Log 紀錄和追蹤的愛恨交織 - Day 02 - ASP.NET Core 內建之 Logger 01"
datePublished: Mon Apr 13 2026 04:56:30 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzzip000d02l1cjv05csz
slug: it-aspnet-core-log-day-02-aspnet-core-logger-01
canonical: https://medium.com/@abc12207/it-%E9%90%B5%E4%BA%BA%E8%B3%BD-asp-net-core-%E8%88%87-log-%E7%B4%80%E9%8C%84%E5%92%8C%E8%BF%BD%E8%B9%A4%E7%9A%84%E6%84%9B%E6%81%A8%E4%BA%A4%E7%B9%94-day-02-asp-net-core-%E5%85%A7%E5%BB%BA%E4%B9%8B-logger-01-9d2313bd3a43
cover: https://cdn-images-1.medium.com/max/800/1*htcRECG4Z7-6zC9zI6mjNA.png

---

---

#### .NET Core Logging- Logging in ASP.NET Core 01

![](https://cdn-images-1.medium.com/max/800/1*htcRECG4Z7-6zC9zI6mjNA.png)

ASP.NET Core 其實本身已經內建了一套 Log 工具，透過 DI 的方式注入，就可以直接取得並使用 Log 的物件實體，而且也可以外掛第三方的 Log 架構

方便的是 ASP.NET Core 預設就已經將 Logger 物件放入 DI 容器中了，所以不需要再額外進行設定，只要直接透過 DI 的方式取得 Logger 物件實體

---

Logger 物件提供了不同層級的 Log，共分為六種，定義在 [LogLevel](https://docs.microsoft.com/zh-tw/dotnet/api/microsoft.extensions.logging.loglevel?view=aspnetcore-2.1) 列舉中

* Trace = 0
  通常是用來輸出在開發或是偵錯過程中想要看到的資訊。 這些訊息可能包含敏感資訊，因此不應該在正式環境中啟用。
  **預設為不輸出**。
  例如：`Credentials: {"User":"User", "Password":"P@ssw0rd"}`
* Debug = 1
  通常是用來在正式環境中記錄一些除錯資訊。 由於此層級的 Log 數量可能很可觀，所以平常是不會開啟的，直到有需要時再開啟。
  **預設為不輸出**。
  例如：`Emergency flag set to true.`
* Information = 2
  通常是用來追蹤應用程式的操作或是運作流程。
  例如：`Request received for order id: 201809191111`
* Warning = 3
  在應用程式流程中發生異常或意外事件。 這些記錄可能包含不會造成應用程式停止，但可能需要進行調查的錯誤或其他狀況。 已處理的例外狀況即為使用 `Warning` 記錄層級的常見位置。
  例如：`FileNotFoundException for file quotes.txt.`
* Error = 4
  發生無法處理的錯誤和例外狀況。 這些訊息會指出目前的活動或作業 (例如目前的 HTTP 要求） 中的失敗，而不是整個應用程式的失敗。
  例如：`Cannot insert record due to duplicate key violation.`
* Critical = 5
  發生需要立即注意的失敗。
  例如：資料庫連線失敗、磁碟空間不足等情況。

---

如以下範例程式碼，直接宣告 Logger 物件，並透過 DI 容器注入，注意要引用 `using Microsoft.Extensions.Logging;` 命名空間，且 Logger 物件為泛型，所以要指定 Class 名稱，以此為例就是： `ILogger<HomeController>`

寫完程式碼後，就可以執行來看看，先在 `terminal`中輸入 `dotnet run` 指令來進行編譯並把應用程式跑起來，跑起來後就可以直接呼叫網頁，最後在 `terminal` 中就可以看到 Log 的輸出結果

![](https://cdn-images-1.medium.com/max/800/1*Xv7aDnzDHF8W9rOgHb2m_g.png)

在上圖的第二步驟紅框中，就可以看到 Log 輸出的結果，針對不同層級也會有不同的顯示樣式

而在第二步驟的綠框中則是**事件代碼**，通常在系統中都會定義事件代碼
例如說：資料庫無法連線的錯誤代碼設定為 001

因此在寫入 Log 時也可以傳入事件代碼以供事後快速辨別

---

還有一小部分要提到的是預設格式化訊息的方式，假設有 Log 事件如下

因其格式化的方式是依照參數的先後順序，而非於字串中的變數名稱而定
所以其輸出結果會為：name1 not match with: name2

---

也可以將例外傳入到 Log 裡

![](https://cdn-images-1.medium.com/max/800/1*cmjRh04zBdglMQAozvuMmw.png)

---

下一篇來介紹ASP.NET Core 內建之 Logger的組態設定、如何設定要記錄的 Log 層級以及如何輸出 Log 到不同的地方，而不是只是寫到 Console