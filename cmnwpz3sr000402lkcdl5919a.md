---
title: "Azure Web App 使用 Zip 進行部署"
datePublished: Fri Feb 23 2018 12:47:34 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpz3sr000402lkcdl5919a
slug: azure-web-app-zip
canonical: https://medium.com/@abc12207/azure-web-app-%E4%BD%BF%E7%94%A8-zip-%E9%80%B2%E8%A1%8C%E9%83%A8%E7%BD%B2-36552b4a17f9
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070225811/2eed2052-69b9-41da-a104-7fe6fd05fb3c.png

---

---

#### Azure Web App Deploy Zip

Azure Web App 是個好東西，提供了很多功能卻又很簡單使用，在部署的部分也提供了多種方式，最簡單的方式就是直接利用 Visual Studio 發行，或是用 Git 來進行部署，也可以用 FTP 上傳，等等方式

一般最容易使用的應該就是 FTP 方式了，不過當檔案大小不大且數量很多時，因為 FTP 的特性會導致速度很慢，現在 Azure 推出了一個新的部署方法叫做：Zip Deploy

#### 1. 使用 FTP 軟體

如同字面上的意思，就是把應用程式壓縮成 zip 檔案後上傳，它會自動解壓縮並部署，透過包成 zip 檔可以大量減少上傳時間，下面就來介紹一下怎麼用

首先當然要有已經建好的 Azure Web App，然後開啟以下網址，注意 **app\_name** 要改成自己的 app\_name，開啟時有可能會要求登入，再用 Azure 帳號進行登入

```
https://<app_name>.scm.azurewebsites.net/ZipDeploy
```

打開後會看到以下 Kudu 畫面

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070225811/2eed2052-69b9-41da-a104-7fe6fd05fb3c.png)

Kudu

將壓縮好的檔案直接拖移到視窗上放開即會開始上傳與部署

> ZipDeploy 會自動依照壓縮檔的目錄結構擺放資料夾與檔案位置

左上角會有進度條顯示進度，下面也會有文字進度說明

這樣就部署完畢，很方便吧

> 如果使用 Visual Studio Code，下面還有更方便的方式

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070228153/df19f9e4-4cab-42b3-b355-c5278c15074c.png)

Finish

---

#### 2. 使用 Visual Studio Code 透過擴充功能自動壓縮與部署

Visual Studio Code 提供了一個擴充功能：[Azure App Service](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice)，使擴充功能目前還在 Preview 階段，主要提供了關於 Azure App Service 的管理，其中包含了透過 ZipDeploy 的方式上傳目前的專案

安裝完 Azure App Service 擴充功能後，首先我們要先登入 Azure 帳號，點選『Sign in to Azure』進行登入動作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070230074/68ce685c-f5f1-4218-a25f-7cab414bbc8d.png)

登入

登入完畢會列出目前此帳號底下的所有訂閱，到此登入就確認成功完成了

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070231998/1dd3d3f2-9396-4f37-a5c0-1bfeb93b0bc4.png)

列出訂閱

接下來點選『中間向上箭頭符號(↑)』，開始部署動作，點選後中間上方會出現詢問要部署那個資料夾，這邊選擇想要上傳的資料夾，可以透過打字或者方向鍵進行選擇

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070234120/2a7b5ef2-aa6c-48d5-8c74-96251e7e1c4e.png)

選擇資料夾

選擇完欲上傳之資料夾後，就會要求選擇要放的訂閱

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070236075/a0178239-2eb8-4ace-b744-27ac1cefaade.png)

選擇訂閱

選擇要使用的 Web App

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070238051/75e22f62-2dbd-44b4-89ea-c4150de4f3f4.png)

Web App

最後會要求再確認一次，避免上傳到錯誤的 Web App，蓋掉原本正確的檔案

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070239974/e1ee5b65-77cd-411e-9e00-2c7a2ea53974.png)

Confirm

按下確定後即會開始部署，在輸出視窗會顯示狀態，看到『Deployment to “app-name” completed.』代表部署完畢

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070242101/320c5db2-8eb0-4589-a33a-3f5c798953e3.png)

Complete