---
title: "[IT 鐵人賽] ASP.NET Core 與 Log 紀錄和追蹤的愛恨交織 - Day 01   - 前言"
datePublished: Mon Oct 15 2018 16:08:18 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzu7v000b02l10i1p2alw
slug: it-aspnet-core-log-day-01
canonical: https://medium.com/@abc12207/it-%E9%90%B5%E4%BA%BA%E8%B3%BD-asp-net-core-%E8%88%87-log-%E7%B4%80%E9%8C%84%E5%92%8C%E8%BF%BD%E8%B9%A4%E7%9A%84%E6%84%9B%E6%81%A8%E4%BA%A4%E7%B9%94-day-01-%E5%89%8D%E8%A8%80-ea9ef736d95c
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070380125/cd45a645-dd46-4dc3-a005-1fdafd5ca919.png

---

---

#### .NET Core Logging - Intro

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070380125/cd45a645-dd46-4dc3-a005-1fdafd5ca919.png)

.NET Core

我想大部分的程式開發者都有遇到過一種情況，別人所開發撰寫的程式，平時運行的好好的，突然就在某一刻出現了 Bug，很不幸的維護的責任剛好落在自己身上，到處求助無門，連系統架構都還不太明瞭，無法知道問題到底會出在哪，測試環境也無法重現問題，這時突然發現在記錄檔中有紀錄使用者於正式環境中的操作與錯誤紀錄，終於知道問題出在哪並順利的修復了 Bug；透過此情境大家都可以了解 Log 的重要性，他平常或許不重要，但是到了需要用到時，絕對是超級重要的一件事。

Log 是甚麼？

簡單來說 Log 就是系統在操作時所產生的記錄。有可能是一般的操作紀錄或是發生錯誤的紀錄；俗話說：「凡走過必留下痕跡」，收集並分析 Log ，可讓維運或是開發人員監控系統的運作狀態，並判斷即將發生之事件，或是當發生錯誤時，可以立即通知相關人員。

---

寫 Log 有那些好處呢

* 快速偵錯
  當發生問題時，可以透過 Log 知道到底是哪裡錯誤，若有紀錄 CallStack 的話還可以得知是哪個 Function 在哪一行發生例外
* 重現錯誤步驟
  要修正問題前有一個必要步驟就是重現問題，但是有時候要發生某種例外需要特定的步驟或條件，若有 Log 紀錄使用者操作紀錄，就可以按照 Log 紀錄重現問題
* 效能調教
  當有效能問題時，Log 通常都會有時間戳記，因此可以先觀看每項工作運行所花費時間，再從耗費最久部分開始處理

---

這 30 天會針對以下的 Log 工具進行介紹與使用方式說明

* [ASP.NET Core 內建之紀錄工具](https://docs.microsoft.com/zh-tw/aspnet/core/fundamentals/logging/?view=aspnetcore-2.1)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070382146/2114d364-34c0-4fd0-9c4e-a75718dd403a.png)

* [Elmah](https://elmah.github.io/)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070384385/0ceb072e-c897-46f6-a609-f7910f83514a.png)

* [log4net](https://logging.apache.org/log4net/)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070386325/8e98dd7f-d270-4582-abd0-90612d6726fb.jpeg)

* [NLog](https://nlog-project.org/)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070388249/5d389cbd-de87-4b45-b622-7b1ce5f397a7.png)

* [Application Insight](https://docs.microsoft.com/zh-tw/azure/application-insights/app-insights-overview)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070390232/067b807f-443d-4615-b655-a3e5aeab3910.png)

* [SeriLog](https://serilog.net/)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070392351/4d3b3448-9553-44b2-a8ad-ce19f975815d.png)

---

下一篇會介紹 ASP.NET Core 內建之紀錄工具