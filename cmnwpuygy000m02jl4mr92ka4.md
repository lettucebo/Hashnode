---
title: "ASP.NET JavaScript 上傳圖片預覽"
datePublished: Mon Feb 27 2017 03:43:56 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpuygy000m02jl4mr92ka4
slug: aspnet-javascript
canonical: https://medium.com/@abc12207/asp-net-javascript-%E4%B8%8A%E5%82%B3%E5%9C%96%E7%89%87%E9%A0%90%E8%A6%BD-67baa86f5b2f

---

---

### 緣由

網頁上傳圖片可以預覽一直是個大多數客戶會要求一定要有的功能

我之前的 Solution 都是要求圖片先上傳到 Server 端再透過處理顯示於瀏覽器上，但是這樣就要求至少要 POST 一次以上(如透過：SWFUpload 或是將圖片寫入暫存)，這不僅是沒有效率，且複雜的做法

因此後來想說透過 JavaScript 來達成這件事情是最好的做法

### 方法

如下 JavaScript 所示，即可達成目標