---
title: "Azure Bot Service - 聊天機器人教學 - Node.js - 02"
datePublished: Tue Feb 20 2018 07:42:46 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpz0gj000302lk61u2gsqb
slug: azure-bot-service-nodejs-02
canonical: https://medium.com/@abc12207/%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%95%99%E5%AD%B8-node-js-02-f6584eec7145
cover: https://cdn-images-1.medium.com/max/800/1*5ZqvM-9_p98Z7LUBcERaIg.png

---

---

#### 透過模擬器測試聊天機器人

#### 1. 程式

接續『[聊天機器人教學 — Node.js — 01](https://blog.developer.money/%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%95%99%E5%AD%B8-node-js-01-5fdfef99d766)』的內容，上一篇只能在 console 中測試，一點都不像聊天機器人，所以這一邊要介紹的是如何在 Bot 模擬器中進行測試

首先為了要提供 web 服務，這邊使用 [restify](http://restify.com/) 作為 web server，輸入以下指令進行安裝

```
npm install --save restify
```

安裝完畢後，先宣告相關服務

然後進行 restify 的相關組態設定，這邊使用 3978 port

設定完 restify 後換設定 connector

> appId 與 appPassword 留到後續再行解釋

再設定 bot 收到訊息後的行為

最後設定監聽要求

這樣就完成了程式碼部分

完整程式碼點此：[app.js](https://gist.github.com/lettucebo/3569f4baad1b47dd485545ad5c1b6124)

#### 2. Bot Framework Emulator

微軟為了聊天機器人開發者提供了一個桌面應用程式，用來測試與開發聊天機器人，除了可以直接在本機看到結果外，也可以直接看到所發出訊息的格式與內容

![](https://cdn-images-1.medium.com/max/800/1*5ZqvM-9_p98Z7LUBcERaIg.png)

Bot Framework Emulator

在這邊我們就直接進行安裝，下載位置在：[BotFramework-Emulator-release](https://github.com/Microsoft/BotFramework-Emulator/releases)，依照作業系統選擇檔案下來安裝

安裝完畢開啟後會看到以下畫面

![](https://cdn-images-1.medium.com/max/800/1*y3uyNU6SnQOh7gFsJrGQEg.png)

Bot Framework Emulator

在『Enter your endpoint URL』處輸入剛剛的 bots 網址，並加上 **/api/messages**，其餘均先暫時不填，按下 CONNECT 按扭

![](https://cdn-images-1.medium.com/max/800/1*oPFJ0z8Is0tv8FhZ3xFKVg.png)

輸入網址

連結成功會在右下角 Log 視窗看到以下畫面（POST 202 … 訊息）

![](https://cdn-images-1.medium.com/max/800/1*rxRaH6rqQcHvr0NnDhdGRw.png)

連結成功

連結成功後即可進行測試與觀看結果

![](https://cdn-images-1.medium.com/max/800/1*gq1mPWMUNlKJH-ToyxPu2w.png)

結果畫面