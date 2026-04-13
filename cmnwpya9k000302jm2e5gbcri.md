---
title: "在IIS執行Java JSP — SERVER 2012R2"
datePublished: Tue Feb 28 2017 05:33:42 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpya9k000302jm2e5gbcri
slug: iisjava-jsp-server-2012r2
canonical: https://medium.com/@abc12207/%E5%9C%A8iis%E5%9F%B7%E8%A1%8Cjava-jsp-server-2012r2-671896f20c00
cover: https://cdn-images-1.medium.com/max/800/0*UfLydBduQG9hBmlj.png

---

---

iis-java-jsp-with-server-2012-r2

今天看到一篇文微軟之前發布的文章：[Announcing the Release of the HttpPlatformHandler Module for IIS 8+](https://azure.microsoft.com/en-us/blog/announcing-the-release-of-the-httpplatformhandler-module-for-iis-8/)，大意是關於如何在IIS上運行JAVA網頁應用程式，雖然說是蠻久之前的文章，但是看到之後立刻讓我回想起帶大一年半前的努力嘗試如何用IIS架JAVA網頁應用程式。

後來其實一直失敗，就是沒試出來，所以現在來趕快試試看，彌補之前的失敗心情！

`我的測試平台都是架構在AZURE上，非常方便，測完即丟呀！`

IIS透過HttpPlatformHandler來達到在IIS上執行JAVA網頁應用程式的目的，Microsoft Azure Web Apps就是用此種方法來實作的，看起來是微軟終於釋出了此模組。

HttpPlatformHandler的功能有兩個(節錄自[保哥部落格](http://blog.miniasp.com/post/2015/10/23/Introducing-HttpPlatformHandler-module-for-IIS-8-and-ASPNET-5-Beta8.aspx))：[

* Process Management of http listeners — 任意第三方程序原本需要監聽 (listen) 可接受 HTTP 要求的通訊埠 (Port)，都改交由 IIS 來接受要求。 例如 Tomcat, Jetty, Node.exe, Ruby 等等，當然 ASP.NET Core 的 Kestrel 也是屬於這個類型的程序。
* Proxy requests to the process that it manages — 將那些交由 IIS 代理監聽的 HTTP 要求轉發到被管理的第三方程序。

簡單來說，原本你可能可以直接用 Node.js 或 Ruby 來執行網站，Node.js 或 Ruby 原本就能監聽 (listen) 通訊埠 (Port)，但如果 Node.js 或 Ruby 掛掉的話，網站也就死了。不過若想透過 IIS + HttpPlatformHandler 來管理者些程序，優點就是所有接聽 HTTP 要求的任務都改由 IIS 負責，並且由 IIS 啟動第三方程序 (例如 Node.js 或 Ruby)，然後由 IIS 將這些 HTTP 要求轉發到第三方程序中。如果第三方程序掛掉了，IIS 就會視同沒有執行這個程序，自動重新啟動第三方程序。

我個人的腦補是反正所有 Http Request 都交給 IIS 負責接受，若需要第三方來執行那再由 IIS 進行呼叫第三方執行。

HttpPlatformHandler 透過以下 config 中之 configuration 區段來定義啟動，下面之設定檔為全部之設定參數，再不同的環境下會有不同的設定(可參考[介紹 IIS 8 全新的 HttpPlatformHandler 模組與 ASP.NET 5 Beta8 重大變更](http://blog.miniasp.com/post/2015/10/23/Introducing-HttpPlatformHandler-module-for-IIS-8-and-ASPNET-5-Beta8.aspx))

可參考：

* Configuration Reference [Article](http://www.iis.net/learn/extensions/httpplatformhandler/httpplatformhandler-configuration-reference)
* Download the [HttpPlatformHandler](http://www.iis.net/learn/extensions/httpplatformhandler/httpplatformhandler-configuration-reference)

說了一些話，接下來終於輪到實作啦

(我這邊使用[TOMCAT 8](http://tomcat.apache.org/download-80.cgi)作為JAVA網頁伺服器，並用[Pebble blogging](http://tomcat.apache.org/download-80.cgi)當作我的網頁)

1. 安裝 HttpPlatformHandler

可以透過 [WebPI](http://www.microsoft.com/web/gallery/install.aspx?appid=HttpPlatformHandlerv1_0) 來安裝，或是直接下載安裝檔來安裝 [x86](http://download.microsoft.com/download/8/B/1/8B1DDE49-503D-4159-9418-76C4A365B70B/httpPlatformHandler_x86.msi)/[x64](http://download.microsoft.com/download/0/2/C/02CF3C6A-2ED8-43D3-9779-6376EBB80E8A/httpPlatformHandler_amd64.msi)

當然還是要推薦使用 [WebPI](http://www.microsoft.com/web/gallery/install.aspx?appid=HttpPlatformHandlerv1_0) 來安裝，因為 [WebPI](http://www.microsoft.com/web/gallery/install.aspx?appid=HttpPlatformHandlerv1_0) 來安裝會自動替你決定最適合的安裝檔，不用擔心是否會抓到錯的平台版本檔案

2. 下載 [TOMCAT 8](http://tomcat.apache.org/download-80.cgi)

這邊要注意的是記得要抓zip檔案，而非執行檔

然後至特定目錄，這邊我全部解壓縮到C:\JavaTest

![](https://cdn-images-1.medium.com/max/800/0*UfLydBduQG9hBmlj.png)

3. 編輯 Tomcat 的 server.xml (位於 conf 資料夾)

![](https://cdn-images-1.medium.com/max/800/0*_PzavdVd79JKUvCO.png)

將 HTTP connector port 修正為 ${port.http}

要注意一個地方，除了 HTTP 監聽程式連接埠之外的所有監聽程式連接埠都必須停用。在 Tomcat 中，這包括關機、HTTPS 及 AJP 連接埠

4. 取得 JAVA 網頁應用程式

這邊使用 [Pebble blogging](http://tomcat.apache.org/download-80.cgi) 作為範例 下載後解壓縮了至相對應資料夾，這邊範例為：C:\JavaTest\apache-tomcat-8.0.28\webapps

![](https://cdn-images-1.medium.com/max/800/0*u9bRV4TCiDC41J8I.png)

5. 設定 IIS

這邊新增網站都與過相往一樣，就是新增一個網站

![](https://cdn-images-1.medium.com/max/800/0*aQ1HjcSFcb7s4QrV.png)

6. 設定 web.config

最後將相關JAVA參數設定至web.config

* rocessPath — Tomcat啟動程序startup.bat所在位置
* stdoutLogEnabled — 若為True則啟動logging功能
* stoutLogFile — 設定Log檔案寫入位置

#### EnvironmentVariables

* JRE Home — JRE所安裝之所安裝資料夾位置
* CATALINA\_HOME — Tomcat所在目錄

7. 完成

這樣就可以透過 IIS 來處理 JSP 網頁的要求

### 參考資料：

* [Announcing the Release of the HttpPlatformHandler Module for IIS 8+](https://azure.microsoft.com/en-us/blog/announcing-the-release-of-the-httpplatformhandler-module-for-iis-8/)
* [介紹 IIS 8 全新的 HttpPlatformHandler 模組與 ASP.NET 5 Beta8 重大變更](http://blog.miniasp.com/post/2015/10/23/Introducing-HttpPlatformHandler-module-for-IIS-8-and-ASPNET-5-Beta8.aspx)