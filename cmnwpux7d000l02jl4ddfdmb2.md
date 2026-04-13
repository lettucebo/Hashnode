---
title: "變更 Windows 遠端桌面的連接埠 (Port)"
datePublished: Mon Feb 27 2017 07:26:11 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpux7d000l02jl4ddfdmb2
slug: windows-port
canonical: https://medium.com/@abc12207/%E8%AE%8A%E6%9B%B4-windows-%E9%81%A0%E7%AB%AF%E6%A1%8C%E9%9D%A2%E7%9A%84%E9%80%A3%E6%8E%A5%E5%9F%A0-port-33423479ebcd
cover: https://cdn-images-1.medium.com/max/800/1*5LOBPspy6liIIHJCnkDEQg.png

---

---

modifying-the-windows-remote-desktop-port

### 緣由

我本身所在公司大部分都是政府專案，他們對於遠端桌面有個很不好的迷思，他們覺得遠端桌面這麼流行，那 3389 port 肯定也是廣為流傳，那麼最好改個隨機 port 比較不會受攻擊

當然這根本是**錯誤的思想**，畢竟現在到處都是掃描工具，隨便掃一下就可以知道遠端 port 是多少

可惜在這產業，客戶永遠是對的，只好在這邊記錄一下如何修改遠端桌面 port

### 方法

遠端桌面所使用的 port 預設為 3389，其設定寫在登錄檔裡，因此要修改就要編輯登錄檔

1. 開啟登錄檔編輯器

![](https://cdn-images-1.medium.com/max/800/1*5LOBPspy6liIIHJCnkDEQg.png)

開啟登錄檔編輯器

2. 尋找登錄檔所在位置

根據以下資料夾結構即可找到正確登錄檔所在位置

> HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Control\TerminalServer\WinStations\**RDP**[**–**](http://briian.com/?p=7129)**Tcp**\**PortNumber**

![](https://cdn-images-1.medium.com/max/800/1*v4tOoADJG9O1SXikj9ev4A.png)

3. 修改 Port 號

點擊兩下即可編輯，要注意編輯時是十進位還是十六進位，通常點選十進位即可

修改成想要的 port 號即可，舉例來說這邊改成 9938，完成後按下 OK

![](https://cdn-images-1.medium.com/max/800/1*EM0rHDgZFO8hZLJBWqEG6A.png)

4. 重新開機

這設定需要重開機才會生效，重開機完畢後即大功告成