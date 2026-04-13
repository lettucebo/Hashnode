---
title: "Windows MySQL 備份與排程備份（透過指令列方式）"
datePublished: Mon Feb 27 2017 03:53:59 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpxsgi000002lk6vftbmaa
slug: windows-mysql
canonical: https://medium.com/@abc12207/windows-mysql-%E5%82%99%E4%BB%BD%E8%88%87%E6%8E%92%E7%A8%8B%E5%82%99%E4%BB%BD-%E9%80%8F%E9%81%8E%E6%8C%87%E4%BB%A4%E5%88%97%E6%96%B9%E5%BC%8F-8dfec04ce0f7
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070047900/5d8e9810-224d-4b73-9520-55ed22a3e186.png

---

---

windows-mysql-backups-and-scheduled-backups-command-line

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070047900/5d8e9810-224d-4b73-9520-55ed22a3e186.png)

MySQL 不如 SQL Server 有著 SQL Server Agent 來幫忙處理排程等事項，因此若要針對 MySQL 進行排程備份不外乎兩種方法：

1. 安裝第三方備份排程程式
2. 自行撰寫 Script 透過 Windows 排程定期執行

第一種方法需要安裝額外程式，優點是十分簡單，且通常都有已經撰寫好的 GUI 介面，但我比較不喜歡的一點是通常此類程式都為常駐程式，且要求授權（經費拮据）；目前 MySQL Administrator 免費版也已不支援自動備份排程功能(新版又已支援排程備份)，因此為了解救此問題，只好自己土炮 MySQL 自動備份排程了

`20160710 更新：現在官方所出的管理軟體已有免費支援備份`

大概的步驟為：先透過指令的方式進行備份，再將這指令透過 Windows 排程進行定期執行，這樣就達到我們所想要的效果了

1. 手動備份指令碼

可透過命令提示視窗執行

示範畫面：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070049786/2382c7c4-0c18-49ef-883f-440f704ae6c9.png)

示範畫面

2. 自動排程備份

(1) 備份指令碼

因為排程備份的關係，要避免檔案名稱重複而導致覆蓋檔案問題，所以檔案名稱一定要透過變數產生，才不會發生檔案名稱相同，導致新的備份檔案蓋掉舊的備份檔案

(2) 設定排程執行

設定排程執行 Windows 就有內建非常方便的`工作排程器`，只要透過滑鼠點一點設定一下，即可方便完成排成設定

首先先開啟工作排程器：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070051773/8d7b98b5-9209-4758-8afc-6ee008ee7159.png)

開啟工作排程器

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070053763/fa1a3261-18c0-40df-adfd-8426732c5916.png)

開啟工作排程器

新增一基本工作：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070055763/c04f5bb6-3d8d-4a41-a827-6de42ad234cf.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070057767/e58d0014-b893-4b61-a494-9286705f37d1.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070059759/4d785483-bef4-4cbf-9344-fc48cf81d86c.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070061764/9d48dbd3-50ed-4d40-9c79-593346e1fc2e.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070063776/18ae5f64-7e6d-4075-a09f-171c36b671e7.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070065902/cc7cf810-3914-40ae-bba7-42e5c2d58f83.png)

新增一基本工作

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070067764/b19f7352-bc07-4065-af59-f9b921e14e74.png)

新增一基本工作

通過以上步驟，即可完成透過 Windows 工作排程器來定時啟動備份指令

完成畫面如下：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070069763/eb878080-d3e3-44f8-9e3c-b60079da9112.png)

完成畫面