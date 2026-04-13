---
title: "[IT 鐵人賽] ASP.NET Core 與 Log 紀錄和追蹤的愛恨交織 - Day 05 - Elmah - 02"
datePublished: Mon Apr 13 2026 04:56:48 GMT+0000 (Coordinated Universal Time)
cuid: cmnwq0d0s000802jr6gyl3ml0
slug: it-aspnet-core-log-day-05-elmah-02
canonical: https://medium.com/@abc12207/it-%E9%90%B5%E4%BA%BA%E8%B3%BD-asp-net-core-%E8%88%87-log-%E7%B4%80%E9%8C%84%E5%92%8C%E8%BF%BD%E8%B9%A4%E7%9A%84%E6%84%9B%E6%81%A8%E4%BA%A4%E7%B9%94-day-05-elmah-02-42e9b8810419
cover: https://cdn-images-1.medium.com/max/800/1*B9NNmAzguvhwfMncQs7ybg.png

---

---

#### .NET Core Logging- Elmah 02

![](https://cdn-images-1.medium.com/max/800/1*B9NNmAzguvhwfMncQs7ybg.png)

上一篇我們提到了基本的使用方式，接下來的這一篇我們就來講講要怎麼把 Log 放到不同的儲存體上，以及如何過濾 Log

---

#### Log 儲存方式

我們先來看這些 Log 倒底存在哪裡，目前共有三種儲存方式，如下：

* MemoryErrorLog — store errors in memory
  預設為使用此方式，簡單來說就是將錯誤 Log 都存在記憶體裡，所以只要應用程式一重新啟動，Log 就沒了；但是也是最方便的方式，只是要注意如果 Log 太多的話，記憶體的使用狀況，避免記憶體不足的情況。
* XmlFileErrorLog — store errors in XML files
  將 Log 存成 Xml 格式之檔案，並儲存於檔案系統上。
* SqlErrorLog — store errors in MS SQL
  將 Log 存到 SQL Server 上。

> <https://github.com/funky81/ElmahCore> 有額外提供 Redis 當作儲存體

---

如果要使用除了 `MemoryErrorLog` 以外的方式，下面一一介紹如何設定

#### XmlFileErrorLog

於 `Startup.cs` 之 `ConfigureServices` 中加入 `service.AddElmah();` 時，使用泛型來指定要儲存的方式，並指定儲存路徑

這樣就會將錯誤 Log 存成 Xml 格式，並放在指定目錄；以此為例就是在應用程式根目錄底下的 `logs` 資料夾，也可以直接指定絕對路徑，例如：`D:\ErrorLogs`

![](https://cdn-images-1.medium.com/max/800/1*EY1i7nhIEFuKSzwCgiM55w.png)

要注意的是每一個錯誤 Log 就是一個 Xml 檔案，所以有可能會塞爆檔案系統，或是檔案數量過多，導致系統效能低下

#### SqlErrorLog

於 `Startup.cs` 之 `ConfigureServices` 中加入 `service.AddElmah();` 時，使用泛型來指定要儲存的方式，並指定連線字串

```
"ConnectionStrings": {
    "ElmahConnectionString": "Server=(localdb)\\mssqllocaldb;Database=Elmah;Trusted_Connection=True;MultipleActiveResultSets=true"
}
```

> 需要先根據 <https://bitbucket.org/project-elmah/main/downloads/ELMAH-1.2-db-SQLServer.sql> 建立資料表

這樣即可建立並使用資料庫收集錯誤 Log

![](https://cdn-images-1.medium.com/max/800/1*1HmzOFkwqxuyvpfuzsj5Rw.png)

---

#### 使用 Filter

Elmah 預設會記錄所有例外錯誤，但是有些可能是很常見或是不需要理會的 Log，例如 HTTP 404 找不到資源錯誤，而且這種情況可能很多，導致產生大量無用 Log；因此可以透過 Filter 的方式過濾

這部分基本上與 Elmah 差不多相同，有兩種方式可以進行設定：

1. 透過程式動態設定

透過實作 `IErrorFilter` 介面，當 `Filtering` 事件發生時，它會去看說是不是有任何的 `Filter`呼叫 `Dismiss` 方法，呼叫 `Dismiss` 方法代表 Elmah 會略過此 Log

以下面程式碼為例：實作當遇到 `NotImplementedException` 時就不會記錄 Log，並於 `Startup.cs` 之 `ConfigureServices` 加入 `service.AddElmah();` 時，加入相關設定

2. 透過 XML 設定檔

Elmah 可以讀取 XML 設定檔來進行 Filter 設定，這樣就不用每當需要修改不同條件時還需要修改程式

以下面為例，於設定檔中設定不要紀錄 HTTP 404 的 Log ，並於 `Startup.cs` 之 `ConfigureServices` 加入 `service.AddElmah();` 時，加入相關設定

上面的 `elmah.xml` 需要實作 `errorFilter` 區段

`test` 代表的是要判斷是否相符，若相符則略過，底下有不同的運算子： `equal` 、 `lesser` 、 `greater` 、 `and` 、 `or` 等等

```
<test>
  <and>
      <greater binding="HttpStatusCode" value="399" type="Int32" />
      <lesser binding="HttpStatusCode" value="500" type="Int32" />
  </and>
</test>
```

以上面為例，就是要略過 HTTP 狀態碼大於 399 且小於 500 的所有錯誤 Log

詳細設定說明請參考：<https://elmah.github.io/a/error-filtering/>

---

#### 傳送通知

在正式環境發生嚴重例外時，除了記錄下來以外，最好也要可以及時通知相關人員，Elmah 也透過寄送 Email 的方式提供了基本的通知功能

直接在 `Startup.cs` 之 `ConfigureServices` 加入 `service.AddElmah();` 時，加入相關設定

每個 `ErrorMailNotifier` 實體都**必須要有唯一的名字**，`EmailOptions` 就是一些關於 Mail Server 與寄送相關資訊的設定，所以這邊就不再多詳談

---

下一篇來介紹 Elmah 的雲端變種：Elmah.io