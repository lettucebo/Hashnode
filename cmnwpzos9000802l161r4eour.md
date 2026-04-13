---
title: "Microsoft Library Manager - VS 15.8 版本新樣貌"
datePublished: Mon Apr 13 2026 04:56:16 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzos9000802l161r4eour
slug: microsoft-library-manager-vs-158
canonical: https://medium.com/@abc12207/microsoft-library-manager-15-8-%E7%89%88%E6%9C%AC%E6%96%B0%E6%A8%A3%E8%B2%8C-8a1b28d58c9a
cover: https://cdn-images-1.medium.com/max/800/1*N9z5CPuM--sIr2xjcSYZAw.png

---

---

#### Microsoft Library Manager — VS 15.8 New Look

Microsoft Library Manager 隨著 Visual Studio 15.8 一起正式發布了，之前也撰寫了一篇完整的[介紹文](https://blog.developer.money/asp-net-core-%E7%AE%A1%E7%90%86%E5%89%8D%E7%AB%AF%E5%A5%97%E4%BB%B6%E7%9A%84%E6%96%B0%E5%A5%BD%E5%B7%A5%E5%85%B7-microsoft-library-manager-a0acbd4be058)，然而隨著新版的發布，也增加了一些功能，所以這邊再來介紹一下新增加的功能

首先最明顯的是新增了 GUI 介面，在資料夾上按右鍵 -> 新增 -> Client-Side Library，就會出現 GUI 視窗

![](https://cdn-images-1.medium.com/max/800/1*N9z5CPuM--sIr2xjcSYZAw.png)

Add Client Side Library Menu

你可以在此視窗選擇 Provider，與輸入 Library 名稱，Library 名稱現在也支援自動完成了，選擇完 Library 名稱後，輸入 `@` 也會出現版本的選擇提示

![](https://cdn-images-1.medium.com/max/800/1*7xSqImS1uKaeqB3XWtSXcg.png)

Enter Library Name

可以透過此視窗選擇要下載哪些檔案，預設是會自動下載所有檔案，也可以勾選要下載的檔案

![](https://cdn-images-1.medium.com/max/800/1*-Do335lq8NF9gdj-aUG3WA.png)

Include File

最後是 Target Location，他預設已經幫你選好檔案路徑，當然也可以修改想要的名稱

第二個新功能是提供了新的 Provider: UnPkg，讓你有新的選擇，UnPkg 是建立在 NPM 基礎上，所以有更多 Library 可以選擇使用

最後一個是新增了 CLI 介面，可以透過 Nuget 或是 Package Manager Console安裝 `Microsoft.Web.LibraryManager.Cli`

![](https://cdn-images-1.medium.com/max/800/1*aQsD6Mav9I-a4Bv1dx1grg.png)

```
dotnet tool install -g Microsoft.Web.LibraryManager.Cli
```

安裝完後就可以用 Command Line 來進行 LibMan 的管理了，這邊偷懶用官方的圖

![](https://cdn-images-1.medium.com/max/800/0*G1JglNyqYLQbrtoK.png)

#### 參考

[**Library Manager Released in 15.8**
*NET web development and tools at Microsoft*blogs.msdn.microsoft.com](https://blogs.msdn.microsoft.com/webdev/2018/08/31/library-manager-release-in-15-8/ "https://blogs.msdn.microsoft.com/webdev/2018/08/31/library-manager-release-in-15-8/")