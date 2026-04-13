---
title: "Windows 10 如何完整移除 OneDrive"
datePublished: Mon Feb 27 2017 14:25:40 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpw9dz000302jre39w4ipe
slug: windows-10-onedrive
canonical: https://medium.com/@abc12207/windows-10-%E5%A6%82%E4%BD%95%E5%AE%8C%E6%95%B4%E7%A7%BB%E9%99%A4-onedrive-db5c85c42a40
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070037787/71918c9c-5a20-48d5-90a1-07e983c23a38.png

---

---

how-to-uninstall-onedrive-completely-in-windows-10

我在一開始就入門了雲端儲存，那時只有 Dropbox，所以就一直用到現在了，所以**時機真的很重要**阿 Windows 10 內建的 OneDrive 對我來說就是完全沒用，但是又沒有內建方法可以完整移除（包括檔案總管側邊欄） 所以在這邊介紹如何完整移除 OneDrive

### 方法

`我的操作系統為英文，所以畫面都是英文`

● 使用管理員權限打開命令提示字元（在 Windows 鍵上點擊滑鼠右鍵，點選命令提示字元(系統管理員)）

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070037787/71918c9c-5a20-48d5-90a1-07e983c23a38.png)

● 於命令提示字元中輸入以下指令，來終止 OneDrive processes

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070039776/4eca069a-c514-4c05-a38d-f108419907ce.png)

● 再來依據作業系統版本輸入以下指令來移除 OneDrive

32 bit 作業系統

64 bit 作業系統

`20170227 微軟在新的更新中已可以透過控制台解除安裝 OneDrive`

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070041921/b77fc1f8-5f9b-46d2-a593-602c149ee207.png)

此時不會跳出任何提示視窗，再次看到輸入介面後代表已經完成解除安裝 OneDrive

● 使用 Registry Hack 方式來移除檔案總管側邊欄 OneDrive 選項 下載以下壓縮檔解壓縮後，根據系統版本執行相對應檔案，即可達到目標 下載：[Hide-OneDrive-From-File-Explorer.zip](http://1drv.ms/1NQN8b8)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070043790/444786b6-0a9b-4e18-9ba4-7f607d628433.png)

### 重新安裝

假設你突然後悔想要重新安裝 OneDrive 的話，可以到以下資料夾 `%SystemRoot%\SysWOW64\` 執行 `OneDriveSetup.exe` 即可重新安裝

### 恢復檔案總管側邊欄

下載以下壓縮檔解壓縮後，根據系統版本執行相對應檔案，即可達到目標 下載：[Hide-OneDrive-From-File-Explorer.zip](http://1drv.ms/1NdrEj3)