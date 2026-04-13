---
title: "Windows MySQL 備份與排程備份（透過指令列方式）"
datePublished: Mon Feb 27 2017 03:53:59 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpxsgi000002lk6vftbmaa
slug: windows-mysql
canonical: https://medium.com/@abc12207/windows-mysql-%E5%82%99%E4%BB%BD%E8%88%87%E6%8E%92%E7%A8%8B%E5%82%99%E4%BB%BD-%E9%80%8F%E9%81%8E%E6%8C%87%E4%BB%A4%E5%88%97%E6%96%B9%E5%BC%8F-8dfec04ce0f7
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776058176836/45ef703b-ca9e-4775-b51f-9e656e990224.png

---

---

windows-mysql-backups-and-scheduled-backups-command-line

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058176836/45ef703b-ca9e-4775-b51f-9e656e990224.png)

MySQL 不如 SQL Server 有著 SQL Server Agent 來幫忙處理排程等事項，因此若要針對 MySQL 進行排程備份不外乎兩種方法：

1. 安裝第三方備份排程程式
2. 自行撰寫 Script 透過 Windows 排程定期執行

第一種方法需要安裝額外程式，優點是十分簡單，且通常都有已經撰寫好的 GUI 介面，但我比較不喜歡的一點是通常此類程式都為常駐程式，且要求授權（經費拮据）；目前 MySQL Administrator 免費版也已不支援自動備份排程功能(新版又已支援排程備份)，因此為了解救此問題，只好自己土炮 MySQL 自動備份排程了

`20160710 更新：現在官方所出的管理軟體已有免費支援備份`

大概的步驟為：先透過指令的方式進行備份，再將這指令透過 Windows 排程進行定期執行，這樣就達到我們所想要的效果了

1. 手動備份指令碼

可透過命令提示視窗執行

示範畫面：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058178833/f66cc38f-13de-4c78-b045-d9d75cf268d2.png)

示範畫面

2. 自動排程備份

(1) 備份指令碼

因為排程備份的關係，要避免檔案名稱重複而導致覆蓋檔案問題，所以檔案名稱一定要透過變數產生，才不會發生檔案名稱相同，導致新的備份檔案蓋掉舊的備份檔案

(2) 設定排程執行

設定排程執行 Windows 就有內建非常方便的`工作排程器`，只要透過滑鼠點一點設定一下，即可方便完成排成設定

首先先開啟工作排程器：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058180819/22734dbf-aba6-4454-920b-537ae4ef390e.png)

開啟工作排程器

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058182818/cb20130f-d56f-4986-90ed-4cdaef0be00b.png)

開啟工作排程器

新增一基本工作：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058184847/83bc1af4-4ae0-44b7-a2f9-913cbf33718e.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058186831/9b349b1b-34df-4a9d-81ef-5dcaf948189a.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058189363/6534c981-def4-4cb2-8859-477c2e9f60f1.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058190805/5f0d7956-7f85-45bd-ad0a-c542fd77120f.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058192846/4e9e9c2b-981d-491b-9764-48d22720bd1f.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058194871/c2cdcebe-37be-46d3-80b3-e3b361827527.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058196808/50d622d7-9b69-4a7f-8df6-683ca1d72c2c.png)

新增一基本工作

通過以上步驟，即可完成透過 Windows 工作排程器來定時啟動備份指令

完成畫面如下：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058199081/cc09158f-2eb4-45ce-a360-96f2ae9fd57c.png)

完成畫面