---
title: "ASP.NET Core 將 NPM Package 檔案複製到 wwwroot/lib 底下"
datePublished: Fri Dec 15 2017 08:40:54 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpyvnn000702jm8a2n1qjw
slug: aspnet-core-npm-package-wwwrootlib
canonical: https://medium.com/@abc12207/asp-net-core-%E5%B0%87-npm-package-%E6%AA%94%E6%A1%88%E8%A4%87%E8%A3%BD%E5%88%B0-wwwroot-lib-%E5%BA%95%E4%B8%8B-810ff6e47387
cover: https://cdn-images-1.medium.com/max/800/1*sMSyzk0vise9SfJ0lmyYfg.png

---

---

#### ASP.NET Core automatic copy npm lib to wwwroot/lib

首先要說的是，在 ASP.NET Core 的專案結構底下，Nuget 已經被設為純後端的套件管理工具了，不能在像以前不論前後端都使用 Nuget 來進行套件管理

![](https://cdn-images-1.medium.com/max/800/1*sMSyzk0vise9SfJ0lmyYfg.png)

Incompatible Nuget

請使用 Bower 作為替代方案，但是很不幸的，Bower 已死？ ([Drop Bower support](https://github.com/twbs/bootstrap/pull/23568)、[Consider deprecating Bower](https://github.com/bower/bower/issues/2298))，舉例來說，這次本來想安裝 Bootstrap 4.0.0-beta.2，結果不管怎麼裝都裝不起來，出現 ***EMALFORMED Failed to read bower.json*** 錯誤訊息，才查到在 Github 上面的 [Issue](https://github.com/twbs/bootstrap/issues/24479)，說明 Bootstrap 之後新版都不支援 Bower 安裝了，之後只會有越來越多的前端專案不支援 Bower

現在前端最流行的套件管理工具就是：npm，使用方法網路上都有，但是他的行為跟預設的 ASP.NET Core 行為不太一樣，導致下載或更新 package 的檔案變更並不會同步到 wwwroot/lib 底下，我個人比較習慣使用原來的方法，所以找了一下如何讓 npm 可以把檔案同步到 wwwroot/lib 方法，簡單來說：可以辦到，但是沒有直接的方法，解法是透過 Gulp 來進行檔案的操作

首先需要先安裝 npm，因為需要透過 npm 安裝 gulp

安裝完 npm 後透過命令提示字元執行以下指令

> `npm install --global gulp-cli`

要不然到時候執行 glup 時有可能會出現： *no command 'gulp' found* 錯誤，因為在全域找不到 gulp

執行完畢可以輸入gulp 來確認一下安裝是否有成功

![](https://cdn-images-1.medium.com/max/800/1*5XNS9iCRyKjeGbfnafMTIw.png)

Gulp Check

接下來在專案的根目錄新增：***gulpfile.js***

![](https://cdn-images-1.medium.com/max/800/1*k648WBhtA0oPXhTr5CWJCw.png)

new gulpfile.js

其中我專案有以下的 NPM Package

打開 gulpfile.js 並加入以下程式碼

其中 libs 是要複製到 wwwroot/lib 底下的 package，必須手動指定，所以當之後有新增的 package，就必須在這邊加入的 package 名稱與路徑

此指令新增了三個 Task

一個是 *clean:libs*，用來清除原有 wwwroot/libs 底下的檔案，避免因為有相同檔案而無法覆蓋過去的問題一個

一個是 *copy:libs*，用來複製指定的 package 從 node\_modules 到 wwwroot/lib 底下

最後一個 copy-asset，是將上述兩個 Task 依據順序組合起來一起執行，先清除檔案再複製檔案

完成後，打開 Task Runner Explorer 視窗，可以看到列出了三個 Task，若沒有可以按左邊的重新整理按鈕即會出現

![](https://cdn-images-1.medium.com/max/800/1*Eg6YOCz61M7DxwEkiDy6hQ.png)

Task Runner Explorer

我們先手動確認 Task 可以正確執行，在 copy-asset 上面按右鍵並選擇執行

![](https://cdn-images-1.medium.com/max/800/1*HlRAtvUmcHb0vFvNYPiS9w.png)

Run Gulp

可以看到右邊的輸出視窗會顯示結果

![](https://cdn-images-1.medium.com/max/800/1*8plRdSMf4Ywr6olGqR9iCA.png)

gulp output

確認沒問題後，可以把它設為每次建置必執行的工作步驟之一

在欲加入的 Task 上按右鍵，移到 Binding 選項上，並選擇欲加入的階段，例如說我希望在建置前就執行此項 Task，所以我就選擇 Before Build 選項

![](https://cdn-images-1.medium.com/max/800/1*EMa4ovTynMEL4EKobH9oHA.png)

Binding Before Build

到此就設定完所有的步驟，可以在每次建置前都執行此 Task

![](https://cdn-images-1.medium.com/max/800/1*BmxClvA8HJCmc25fNStawQ.png)

wwwroot/lib

參考

[**Building an Angular2 SPA with ASP.NET Core 1.0, MVC 6, Web API 2, and TypeScript 1.7.5**
*Overview The purpose of this post is to establish ourselves with a working environment geared towards development on…*ievangelistblog.wordpress.com](https://ievangelistblog.wordpress.com/2016/01/13/building-an-angular2-spa-with-asp-net-5-mvc-6-web-api-2-and-typescript-1-7-5/ "https://ievangelistblog.wordpress.com/2016/01/13/building-an-angular2-spa-with-asp-net-5-mvc-6-web-api-2-and-typescript-1-7-5/")