---
title: "Azure Bot Service - 聊天機器人教學 - 04"
datePublished: Mon Feb 26 2018 13:02:14 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpz7hl000502lk57vv27ig
slug: azure-bot-service-04
canonical: https://medium.com/@abc12207/azure-bot-service-%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%95%99%E5%AD%B8-04-bdeb073cbff3
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070245835/92009e02-673f-40fb-976c-bf8efee1c759.png

---

---

#### 將聊天機器人放到 Facebook Messenger 上

上一篇已經讓聊天機器人可以在網際網路上被存取，那接下來就把它放到 Facebook Messenger 上

Facebook Messenger 不論是在歐美或是亞洲都是極其流行的聊天軟體（中國除外），Bot Framework 已經直接支援 Facebook Messenger，不過還是需要設定一下

#### 1. 粉絲專頁

Facebook Messenger 的聊天機器人是建立在粉絲專頁的基礎上，所以需要先有一個粉絲專頁，粉絲專頁的建立過程網路上有很多教學，這邊就不多著墨

#### 2. Azure Bot Service 新增 Facebook Channel

先到 Azure Bot Service 的 Portal 中選擇『Channels』，再於視窗下方選擇『Facebook Messenger』

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070245835/92009e02-673f-40fb-976c-bf8efee1c759.png)

Azure Bot Service Channels

點選後，會看到要求填入相關資訊的欄位，這邊先跳過，晚點回來填，往下拉到『Callback URL and Verify Token for Facebook』區域

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070248262/58a1a797-5c57-4ac3-961e-214ace472faa.png)

New Facebook Channel

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070250309/e2abda28-c969-40af-86cd-c8e7157af2a6.png)

Callback URL and Verify Token for Facebook

走了此資訊，先去設定 Facebook App

#### 3. 新增 Facebook App

有了粉絲專頁後，還需要有一個 Facebook App

前往：[facebook for developers](https://developers.facebook.com/)，登入 facebook 帳號

於右上角『我的應用程式』點選『新增應用程式』，並輸入應用程式名稱建立

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070252552/2b4043aa-f99a-412b-9efa-1f59c8c9a0bd.png)

facebook for developers

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070254087/ff4ac4e4-aafe-4a12-ba03-d759d9cbdf78.png)

新增應用程式

點選設定 Messenger

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070255970/4044e850-d36e-44f0-8dfa-fe39d713dbaa.png)

設定 Messenger

首先先選擇要關連的粉絲專頁，產生粉絲專頁存取權杖

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070267157/5005ad9d-487a-4075-9036-80f90c948324.png)

粉絲專頁存取權杖

設定 Webhook

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070268435/ca834dbf-369f-46d9-8ae0-4982aaa0c5b8.png)

設定 Webhook

點選『設定 Webhooks』，將步驟 2 拿到的 Callback Url 與 Verify Token 填入此處，『Subscription Field』中將：messages、messaging\_postbacks、messaging\_optins、message\_deliveries，四個 Checkbox 勾選起來

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070270471/f980e01e-d848-48a3-aa49-69e2bc16a6c7.png)

設定 Webhooks

到此 Facebook App 就已設定完畢

接下來要將 Facebook App 相關資訊填入 Azure Bot Service 的 Facebook Channel 中

#### 4. 填入 Facebook Channel 資訊

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070272306/7708777d-ed6a-438b-bf30-efd9c67ea002.png)

Facebook App Id & Secert

Facebook Page ID 填入粉絲專頁的編號，可使用此工具查詢：[Find my Facebook ID](https://findmyfbid.com/)

Facebook App Id 對應到『應用程式編號』

Facebook App Secret 對應到『應用程式密鑰』

Page Access Token 填入於上一步驟產生的『粉絲專頁存取權杖』

完成後按下『儲存』就完成了，就可以開始進行測試

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070274731/74711ae0-6b92-489f-bef3-5fbb62b60483.png)

bots-nodejs