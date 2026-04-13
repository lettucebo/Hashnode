---
title: "SSMS 設定黑色佈景主題"
datePublished: Wed Dec 13 2017 08:17:10 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpysvs000102l16lep72hx
slug: ssms
canonical: https://medium.com/@abc12207/ssms-%E8%A8%AD%E5%AE%9A%E9%BB%91%E8%89%B2%E4%BD%88%E6%99%AF%E4%B8%BB%E9%A1%8C-d3219e0970b7
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070173802/9be021d1-faef-4b5c-8b1f-15592d91295b.png

---

---

#### SSMS Set Dark Theme

20230223 更新

我在 Reddit 上看到其實已經有人寫了程式來處理這件事，且包含了側邊欄與結果視窗都有黑化，雖然說還是不盡完美，但是至少已經到了可以接收的地步

連結：[SQL Shades | Dark mode for SSMS](https://www.sqlshades.com/)

*Reference: https://www.reddit.com/r/SQLServer/comments/10ml7j6/comment/j63t7pc/?utm\_source=share&utm\_medium=web2x&context=3*

---

對我來說，開發工具使用黑色佈景主題比較不會刺激眼睛，畢竟要盯著螢幕這麼久，能少一點刺激總是好的

開發工具 Visual Studio 中的佈景主題已經有黑色好一陣子了，資料庫管理工具 SSMS (SQL Server Management Studio) 從 2016 開始就有佈景主題可以選擇，但是一直都沒有相對應的黑色佈景主題

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070173802/9be021d1-faef-4b5c-8b1f-15592d91295b.png)

Original Color Theme

其實 SSMS 已經內建了黑色佈景主題，但是被藏了起來，這一篇就來說明與紀錄如何開啟 SSMS 中隱藏的黑色佈景主題

---

在 SSMS 安裝資料夾中，有一檔案名為：***ssms.pkgundef***

依據不同的 SSMS 版本，所在路徑會有些許不同，主要是因為版本號的關係

#### SSMS 2016

C:\Program Files (x86)\Microsoft SQL Server\130\Tools\Bin\ManagementStudio/ssms.pkgundef

#### SSMS 17.x

C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio/ssms.pkgundef

使用**具有管理員權限**的文字編輯器開啟

找到 Remove Dark theme 段落，將其全部註解掉

完成後，存檔並關閉

打開 SSMS 的設定視窗就會看到黑色佈景主題的選項

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070176042/dbc16410-059a-487f-a34e-832921ea6f28.png)

Dark Theme

選擇黑色佈景主題並確定後，即會立刻套用黑色佈景主題

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070178088/27c2531e-aef9-4232-97fc-a32f2ca68385.png)
> 不過看起來目前黑色佈景主題還沒全部完成，很多視窗都還是白底，也難怪微軟會把他藏起來，不過總是聊勝於無？

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070180224/4deb6899-a07c-427e-8326-5c3d14ec36ed.png)