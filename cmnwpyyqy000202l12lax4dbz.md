---
title: "Azure Bot Service - 聊天機器人教學 - Node.js - 01"
datePublished: Tue Feb 20 2018 05:17:21 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpyyqy000202l12lax4dbz
slug: azure-bot-service-nodejs-01
canonical: https://medium.com/@abc12207/%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%95%99%E5%AD%B8-node-js-01-5fdfef99d766
cover: https://cdn-images-1.medium.com/max/800/1*LqK8azsFPOqfha-eNPxphQ.png

---

---

#### 環境設定

#### 0. 前置準備

1. 安裝 [Node.js](https://nodejs.org/)
2. 建立一個資料夾用來存放聊天機器人的檔案
3. 透過命令提示字元或是終端機，並切換到聊天機器人目錄
4. 執行以下指令，並跟著螢幕指示輸入資訊並往下執行

```
npm init
```

#### 1. 安裝 SDK

專案初始化完成後，我們首先要先安裝 bot builder SDK，一樣透過命令提示字元或是終端機輸入以下指令

```
npm install --save botbuilder
```

#### 2. 最簡單的聊天機器人

於專案目錄下新增 **app.js** 並開啟編輯，輸入以下程式碼

上面的範例程式碼使用了 botbuilder 中的 ConsoleConnector 來直接對 console 中的輸入做反應

我們可以直接透過 console 來測試剛剛寫好的 bot

透過以下指令把這之 bot 跑起來

```
node app.js
```

就可以得到以下結果，你也可以修改訊息內容看看輸出會不會改變

![](https://cdn-images-1.medium.com/max/800/1*LqK8azsFPOqfha-eNPxphQ.png)

console bot