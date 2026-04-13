---
title: "Microsoft Library Manager - ASP.NET Core 管理前端套件的新好工具"
datePublished: Mon Apr 13 2026 04:56:14 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzn3y000a02lk5iwxb4s1
slug: microsoft-library-manager-aspnet-core
canonical: https://medium.com/@abc12207/asp-net-core-%E7%AE%A1%E7%90%86%E5%89%8D%E7%AB%AF%E5%A5%97%E4%BB%B6%E7%9A%84%E6%96%B0%E5%A5%BD%E5%B7%A5%E5%85%B7-microsoft-library-manager-a0acbd4be058
cover: https://cdn-images-1.medium.com/max/800/1*q0E4mqYwEJ6Uk9wn-u2f2A.png

---

---

#### Microsoft Library Manager - A new good tool to manage client-side library for ASP.NET Core

之前為了 Bower 半生不死寫了一篇替代文章：[ASP.NET Core 將 NPM Package 檔案複製到 wwwroot/lib 底下](https://blog.developer.money/asp-net-core-%E5%B0%87-npm-package-%E6%AA%94%E6%A1%88%E8%A4%87%E8%A3%BD%E5%88%B0-wwwroot-lib-%E5%BA%95%E4%B8%8B-810ff6e47387)，但是總決還是有點不方便，每透過 npm 安裝新的套件都還要手動改一下設定檔，要做兩次動作

後來發現了一個尚未正式釋出的新專案：[Microsoft Library Manager](https://github.com/aspnet/LibraryManager)，初步使用覺得還不錯，解決了大部分後端開發者需要管理前端套件的需求且也不會太複雜；而且前一篇文章竟然被認識的人發現，只好來補一下功課

首先，[Microsoft Library Manager](https://github.com/aspnet/LibraryManager) 因為尚未正式釋出，所以沒有內建在 Visual Studio 內，也沒有在 Visual Studio Marketplace 內；必須自己下載專案回來 Build 或是使用 [CI 自動 Build 完的 Vsix](https://ci.appveyor.com/project/aspnetci/librarymanager/branch/master/artifacts)，但是要注意，目前專案設定是針對 VS 15.8 Preview 做建置(15.8 以後應該就內建了)，導致無法於 VS 15.7 上安裝，需要額外調整個設定，這邊請看下一篇文章：[針對 Visual Studio 15.7 以下之版本建置 Microsoft Library Manager.vsix](https://blog.developer.money/%E9%87%9D%E5%B0%8D-visual-studio-15-7-%E4%BB%A5%E4%B8%8B%E4%B9%8B%E7%89%88%E6%9C%AC%E5%BB%BA%E7%BD%AE-microsoft-library-manager-vsix-d057ef5a5bf2)

> 備註：LibMan 不是用來取代 npm/yarn 的，我覺得主要是針對後端開發者只是需要用到些微管理前端相關 library，而非重度前端開發者

![](https://cdn-images-1.medium.com/max/800/1*q0E4mqYwEJ6Uk9wn-u2f2A.png)

進入正題，安裝完 [Microsoft Library Manager.vsix](https://blog.developer.money/%E9%87%9D%E5%B0%8D-visual-studio-15-7-%E4%BB%A5%E4%B8%8B%E4%B9%8B%E7%89%88%E6%9C%AC%E5%BB%BA%E7%BD%AE-microsoft-library-manager-vsix-d057ef5a5bf2) 後，於專案上點選右鍵即可看到 **Manage Client-Side Libraries** 選項，點選後即可看到於專案上會新增一檔案 `libman.json`，並已自動開啟

![](https://cdn-images-1.medium.com/max/800/1*oqriBc462WkDCjdcryyLWA.png)![](https://cdn-images-1.medium.com/max/800/1*3_zVC6A8WgaPwgPjTO47kQ.png)

此檔案結構為 json，預設有三個屬性，以下說明一下

#### version (可選): String

用來指定 `libman.json` 之語法版本，目前只有 1.0 可用 (擷至 2018/08/15)

#### defaultProvider (可選): String

用來指定前端套件預設來源，雖然說是可以選，但是因為通常我們套件來源都是固定的，因此推薦一定要有，預設是從 cdnjs 讀取資料，還有 File System 可以用

#### libraries(必填): Object Array

前端套件列表，用來列出所有受管理的套件與其設定，物件內容詳細說明請參照下說

首先我們先來看一下範例 `libman.json`

其中可以看到多了 defaultDestination，這是套件預設安裝目錄，**但是在現階段蠻雞肋的，他會將所有的套件檔案直接都放在此指定目錄裡**，而不會分不同的套件名稱，所以暫時不太用裡他，取而代之目前會使用的是在每個套件描述裡指定目錄

libraries 底下的物件常用的屬性有三個：

#### library: String

代表cdnjs上套件之名稱與版本，使用 `@`分隔，套件名稱沒有 IntelliSense 支援，但是版本就有，輸入完套件名稱後打上 `@` 就會出現版本的選單

![](https://cdn-images-1.medium.com/max/800/1*lhqreuZRhynz210Ywn818g.png)

#### files(選填): String Array

預設是不需要填此屬性，沒有此屬性時 LibMan 會自動下載所有相關資料夾結構與檔案，若是有指定只要某些檔案，可以在此新增，如：

```
"files": [ "jquery.min.js" ]
```

代表只需要取得 jquery.min.js 即可，結果如下

![](https://cdn-images-1.medium.com/max/800/1*rx8odCl8VPwIvcXaH--37A.png)

#### destination(必選填): string

這邊代表要將此套件檔案放在哪裡，若有設定 defaultDestination 就不用必填，但是反過來說，沒有 defaultDestination 就需要填寫此屬性，已現在來說我推薦都使用此屬性來管理套件的擺放位置

完成以上填寫並存檔後，LibMan 就會自動還原套件檔案，您也可以透過手動觸發或是清除受管理之套件資料夾

![](https://cdn-images-1.medium.com/max/800/1*8diItDuu7tWxKacGsAZWwQ.png)

使用上述範例存檔後，從方案總管上來看會長成這樣

![](https://cdn-images-1.medium.com/max/800/1*Hh4RlwdXyDo1w3UH7I7d1Q.png)

我個人認為這是一個對於後端開發者來說算是挺友善的前端套件管理套件，自從 Nuget 再也無法拿來管理前端套件後，尋尋覓覓應該到此就差不多終結了，希望他不要再死掉了

> 發完文後發現 LibMan 已正式內建於 VS 15.8 且 Release 了，可以去嘗試看看

#### 參考

[**aspnet/LibraryManager**
*GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over…*github.com](https://github.com/aspnet/LibraryManager "https://github.com/aspnet/LibraryManager")