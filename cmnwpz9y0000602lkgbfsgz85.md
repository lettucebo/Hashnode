---
title: "Azure Bot Service - 聊天機器人教學 - Node.js - 03"
datePublished: Mon Feb 26 2018 03:37:02 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpz9y0000602lkgbfsgz85
slug: azure-bot-service-nodejs-03
canonical: https://medium.com/@abc12207/azure-bot-service-%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%95%99%E5%AD%B8-node-js-03-87e784e56613
cover: https://cdn-images-1.medium.com/max/800/1*P_1wcrNxAQz_KmOyr5kKPA.png

---

---

#### 將聊天機器人發行到遠端並透過模擬器測試

在上一篇可以在本地端測試寫好的聊天機器人，不過可以在本地端測試 OK，不代表在 Server 上就會活的好好的，有可能因為組態的不同而導致應用程式出現錯誤，所以我們還是需要發行到遠端後進行測試

#### 1 - 1. 設定 Azure Bot Service 連線資訊

在遠端的聊天機器人為了安全，必需要設定 **Microsoft App ID** 與 **Microsoft App Password** 才能進行連線

首先先打開 Portal 到已經建立完成的 Azure Bot Service 並到 Setting 視窗

![](https://cdn-images-1.medium.com/max/800/1*P_1wcrNxAQz_KmOyr5kKPA.png)

Azure Bot Service Portal

點選『Microsoft App ID』旁的『Manage』連結，會連結到管理 Microsoft App ID 與 Microsoft App Password 頁面

![](https://cdn-images-1.medium.com/max/800/1*cTSq71sLsiis-4oAZXqySw.png)

Azure Bot Service 登錄

點選『產生新密碼』得到新的應用程式密碼，**應用程式密碼只會顯示一次**，務必保存下來，忘記就只能產生新的

![](https://cdn-images-1.medium.com/max/800/1*0zOF6WUDNeoWCEymu_e3-g.png)

產生新密碼

#### 1 - 2. 將連線資訊填入程式

設定完帳號密碼後，要將此資訊填入程式的設定內

這邊我們使用 [**dotenv-extended**](https://www.npmjs.com/package/dotenv-extended)作為讀取設定檔的工具，執行以下指令來安裝 npm 套件

```
npm install dotenv-extended
```

安裝完畢後，新增一檔案：.env，並填入相關資訊如下

然後於程式中引用 dotenv-extended，並在需要設定資訊的地方讀取相關資訊

到這邊程式部分就已完成，將其發行到遠端

#### 2. 發行應用程式

現在要將已經寫好的聊天機器人應用程式發行到遠端以便跟聊天平台溝通，Azure Bot Service 需要以 https 作為開頭的網址為端點，所以這邊使用 Azure Web App 作為承載平台，假設已經完成建立 Web App，可以透過 ZipDeploy 的方式來部署，可參考：[Azure Web App 使用 Zip 進行部署](https://blog.developer.money/azure-web-app-%E4%BD%BF%E7%94%A8-zip-%E9%80%B2%E8%A1%8C%E9%83%A8%E7%BD%B2-36552b4a17f9)

![](https://cdn-images-1.medium.com/max/800/1*BSyXeKMPu837yYhEfa7mPw.png)

Deploy

#### 3. 使用模擬器進行測試

因為我們已將聊天機器人部署到遠端，本機電腦通常都擁有防火牆保護，在此況下無法從外界接收 ad-hoc 要求，所以需要用 Tunneling 透過橋接的方式繞過防火牆將 ad-hoc 要求從外網傳到本機

BotFramework-Emulator 以與 ngrok 整合，不過並沒有直接包含ngrok，所以需要先下載 [ngrok](https://ngrok.com/)，下載完畢後會得到一執行檔（Windows 與 Mac 均是）

![](https://cdn-images-1.medium.com/max/800/1*bOWlE07iPByV71JJ0Zk8Zg.png)

ngrok 執行檔

打開 BotFramework-Emulator 點選『右上方』直線三點打開選單並選擇設定，於 『path to ngrok』中設定 ngrok 執行檔的路徑，按下『Save』

![](https://cdn-images-1.medium.com/max/800/1*UeTcpG259ee9-jqtKgkrXw.png)

設定 ngrok 路徑

這樣就設定完畢，皆下來就是連線到遠端的聊天機器人

![](https://cdn-images-1.medium.com/max/800/1*ngS1SXgQ37uzVm7VsyP-kw.png)

輸入連線資訊

輸入完畢後按下『CONNECT』，這樣就可以開始測試遠端的聊天機器人

![](https://cdn-images-1.medium.com/max/800/1*-A0lCf-7DEvj2v97BaF4zA.png)

Connect