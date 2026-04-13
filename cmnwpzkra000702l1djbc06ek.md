---
title: "針對 Visual Studio 15.7 以下之版本建置 Microsoft Library Manager.vsix"
datePublished: Mon Apr 13 2026 04:56:11 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzkra000702l1djbc06ek
slug: visual-studio-157-microsoft-library-managervsix
canonical: https://medium.com/@abc12207/%E9%87%9D%E5%B0%8D-visual-studio-15-7-%E4%BB%A5%E4%B8%8B%E4%B9%8B%E7%89%88%E6%9C%AC%E5%BB%BA%E7%BD%AE-microsoft-library-manager-vsix-d057ef5a5bf2
cover: https://cdn-images-1.medium.com/max/800/1*LxJU-f_gqgoEK96IahRGgw.png

---

---

#### Build Microsoft Library Manager.vsix for VS15.7 or below

如果是從 GitHub 上直接取得的 Vsix，在 Visual Studio 15.7 以下之版本安裝會得到以下錯誤

```
Install Error : System.InvalidOperationException: A value for 'Component' needs to be specified in the catalog.
```

這邊簡單介紹一下如何為 VS 15.7 或以下之版本建置出可用之 Vsix 安裝檔

首先先從[專案 GitHub](https://github.com/aspnet/LibraryManager/) 下載完整原始碼，先不要打開方案

編輯 [LibraryManager/src/LibraryManager.Vsix/Microsoft.Web.LibraryManager.Vsix.csproj](https://github.com/aspnet/LibraryManager/blob/72bf21f2c5fc56447e27f0ed1b866154d0fb520c/src/LibraryManager.Vsix/Microsoft.Web.LibraryManager.Vsix.csproj#L30) 檔案

其中有一行程式碼為

```
<IsProductComponent>true</IsProductComponent>
```

將其修改為 false

```
<IsProductComponent>false</IsProductComponent>
```

> 當設為 false 時，就可於沒有 Library Manager 之 Visual Studio 版本上安裝 (15.7 或以下)；然而此 vsix 無法更新於已經有 Library Manager 之 Visual Studio 版本 (15.8 Preview 或以上)

修改完後就可以開啟方案，並調整 Configuration 為 Release 後進行建置

![](https://cdn-images-1.medium.com/max/800/1*LxJU-f_gqgoEK96IahRGgw.png)

建置完後打開相對應之資料夾即可看到產生的 Vsix 檔案，點選進行安裝即可

![](https://cdn-images-1.medium.com/max/800/1*qN4IVkuMIka4bPaLI5gYcA.png)