---
title: "Visual Studio 無法啟動 IIS Express Server 問題"
datePublished: Mon Apr 13 2026 04:56:20 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzrva000a02l17ok8eibu
slug: visual-studio-iis-express-server
canonical: https://medium.com/@abc12207/visual-studio-%E7%84%A1%E6%B3%95%E5%95%9F%E5%8B%95-iis-express-server-%E5%95%8F%E9%A1%8C-1f0d134ceea1
cover: https://cdn-images-1.medium.com/max/800/1*bbMvDuuL4852a-V0Z-M2MA.png

---

---

#### Visual Studio Unable to launch the IIS Express Web server

最近時常在兩台電腦間交互辦公，一台在家裡一台是筆電，檔案用 OneDrive 自動同步，所以我每次打開電腦就可以立刻接上另外一台電腦的進度立刻開始辦公

最近開始遇到一個奇怪的問題就是偶爾 Visual Studio 無法啟動 IIS Express Server 開始進行偵錯，都會出現以下錯誤畫面

![](https://cdn-images-1.medium.com/max/800/1*bbMvDuuL4852a-V0Z-M2MA.png)

首先最快也最簡單的方式就是先把 Visual Studio 重開看看

不型的話則先透過 netstat 來判斷是否網站要使用的 port 已被占用

![](https://cdn-images-1.medium.com/max/800/1*awvMMKgdJdWJAdTFq50O9A.png)

netstat

透過 netstat 指令查詢後，可以發現指定的 port 並沒有被占用，所以不會是 port 的問題

```
# 也可以透過以下指令只看特定 port 的清單
netstat -ao | findstr <port_number_to_search_for>
```

再來的話，也是我這情況的原因就是 applicationhost.config 被鎖住了

先到 `{ProjectSource}\.vs\config` 資料夾中，將 `applicationhost.config` 此檔案刪除掉

最後再打開 Visual Studio 開始執行，就可以正常工作了

> 備註：若刪除此檔案還不行，可以嘗試刪除 `Users/<username>/Documents/IISExpress/config` 下的 `applicationhost.config`

> 若是專案放置於 One Drive 目錄下，可以先試試將 One Drive 關閉，然後砍掉 `applicationhost.config` *在開啟 Visual Studio 方式，有時會是 One Drive 導致的問題*

#### 參考

[**How to solve IIS issue in visual studio?**
*This site uses cookies to deliver our services and to show you relevant ads and job listings. By using our site, you…*stackoverflow.com](https://stackoverflow.com/questions/29116292/how-to-solve-iis-issue-in-visual-studio "https://stackoverflow.com/questions/29116292/how-to-solve-iis-issue-in-visual-studio")