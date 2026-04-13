---
title: "Chatbot 02 — 使用 Microsoft Bot Framework 建立 Bot Connector"
datePublished: Fri Jun 02 2017 14:11:30 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpypui000502jmfmcw9sqk
slug: chatbot-02-microsoft-bot-framework-bot-connector
canonical: https://medium.com/@abc12207/chatbot-02-%E4%BD%BF%E7%94%A8-microsoft-bot-framework-%E5%BB%BA%E7%AB%8B-bot-connector-9d98a8d2f04e
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070136101/a3bef7c5-d61f-4657-87e8-04d14f07a671.png

---

---

在這邊簡單記錄一下如何使用 Microsoft Bot Framework 建立 Bot Connector

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070136101/a3bef7c5-d61f-4657-87e8-04d14f07a671.png)

Microsoft Bot Framework

#### Step 1. 開啟網站

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070138099/697b125a-c983-4bce-b020-7722011ec3f6.png)

開啟網站並登入

1. 先使用微軟帳號進行登入的動作
2. 點選 “My bots” 按鈕可以進入到 Bot 列表畫面，此列表會列出目前所擁有的 Bot，如下

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070140050/64a68a0f-3e56-4b10-a814-61a3df7457f0.png)

Bot 列表

點選 “Create a bot” 按鈕來建立一個新的 Bot

#### Step 2. 建立新的 Bot

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070142064/ceadffd2-8b1b-4fb2-a950-f36d08de5eaf.png)

歡迎畫面

首先會看到的是歡迎畫面，直接點選 “Register” 來繼續

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070144048/f2f1fa27-9a91-4326-8742-f8f25575e024.png)

第一區段 - Bot Profile

第一區段會要求填入一些基本資料，說明如下

Icon 可以上傳自訂的 Icon

Display name：給 Bot Connector 一個名稱，最多只能 35 個字元，暫時不支援中文，可以使用英文大小寫、數字與 “-”，盡量不要使用特殊符號，目前特殊符號支援度不是很好

Bot handle：這是**這個 Bot Connector 的唯一代號**，使用在 Bot Connector 未來的連結 URL 上，所以不能跟其他的 Bot 重複（不只是自己的），如：https://facebook.botframework.com/api/v1/bots/{bot handle}

Long description：可以描述此 Bot Connector 的功能與用途

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070146083/44bd4b72-f075-4cac-888b-e786e4de8c67.png)

第二區段 - Configuration

第二區段為 Bot 的相關設定，說明如下

Message endpoint：使用 Bot Builder SDK 或 REST API 所寫出來之 Bot 的溝通介面，將其 URL 貼上來，必須使用 **HTTPS** 協定，例如：https://ubike.azurewebsites.net/api/messages

Create Microsoft App ID and password：這邊會向 Microsoft 註冊一組 Bot 使用的帳號（App ID）與密碼（Password），用意是避免隨意人知道了網址就可以使用你的 Bot，如同登入服務的帳號密碼一般

點選 “Create Microsoft App ID and password” 按鈕後會開一新視窗，如下圖

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070148021/04b9005e-6a8f-4b57-8c49-cf3b2364d022.png)

Create Microsoft App ID and password

這邊會列出 Bot Connector 的名稱，以及將產生給他的應用程式識別碼（App ID），直接點選 “產生應用程式密碼以繼續” 按鈕來進行下一步動作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070149958/89a2b051-f7f2-4cf6-942b-7c3e15055ccb.png)

產生應用程式密碼以繼續

點選 “產生應用程式密碼以繼續” 按鈕後，會看到如下圖密碼提示視窗，這邊密碼只顯示一次，務必在此步驟就先把密碼記到別處，若忘記可以透過管理再產生一組新的密碼

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070152151/55a3f256-dbf4-4ca7-81f5-18c30c37c6dd.png)

記下後即可按下 “按鈕” 以及 “完成，返回 Bot Framework” 按鈕，回到 Bot Connector 設定頁面

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070153950/da7a87ef-9e82-435e-a8c3-f9814d2aa290.png)

完成，返回 Bot Framework

可以看到 App ID 欄位已經被自動填入了

到此設定區段已經設定完畢，到這邊主要的設定都已經完成，接下來是一些選擇性的設定，如分析功能等

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070155990/cd8e758e-8db6-4f86-bc93-a7b820262fef.png)

Analytics

此區段為分析設定，可以透過 Azure 的 App Insight 來分析 Bot 的相關資料

若要使用此分析功能，必須先前往 Azure 設定好 App Insight 來取得相關金鑰，然後填入此區段

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070157972/7a77712f-5116-4e51-8c49-ea8c6e98491c.png)

Admin

最後就是填寫管理者的 Mail，預設會自動帶入登入帳號的 Mail，但是還是可以修改成別的 Mail

點選 “I agree ..” 來同意使用者條約，最後按下 “Register” 按鈕進行註冊

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070159946/a6c11ac8-e0a4-4f93-ad6e-3cced1ac9144.png)

成功建立

看到此畫面即代表 Bot Connector 已經成功建立

皆下來就是設定相關 Channel 的部分