---
title: "版本控制從 TFS 轉為 GIT 並保留所有變更集"
datePublished: Tue Feb 28 2017 05:49:13 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpy5kr000102lkd4yjaa8b
slug: tfs-git
canonical: https://medium.com/@abc12207/%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E5%BE%9E-tfs-%E8%BD%89%E7%82%BA-git-%E4%B8%A6%E4%BF%9D%E7%95%99%E6%89%80%E6%9C%89%E8%AE%8A%E6%9B%B4%E9%9B%86-4dbadedf0f66
cover: https://cdn-images-1.medium.com/max/800/0*zkK4OIfcB54AJDSL.png

---

---

migrate-an-existing-project-from-tfs-to-git-with-changeset-history-intact

一直以來公司都有在使用原始碼版本控制，只是隨著時間的遷移，工具就著變化；從一開始的SVN到TFS到現在的GIT，在轉移機制的過程中，都會遇到一個問題就是變更集要怎麼保留，從 SVN 到 TFS 因為那時數量很少，所以那時也就算了，但是到了從TFS轉到GIT的時候，因為專案與版本都開始龐大起來，不太可能直接忽略它，所以就 Google 了一下如何轉移

找到了一個非常好用的工具[Git-TF](https://gittf.codeplex.com/)，這套工具提供了幾乎所有會用到的功能，從 TFS 複製專案到變成 GIT Repository 直接`一行指令碼解決`

在這邊紀錄一下，避免以後還是要用到又忘了

### Step 1. 相關工具安裝

在 Windows 上安裝 git-tf 最好的方式是透過 [Chocolatey](https://chocolatey.org/) 來進行安裝動作，因為它會自動幫你寫入 PATH 變數。

當然也可以手動安裝 git-tf，其專案在 [git-tf](https://gittf.codeplex.com/) 上，可自行去下載與看如何安裝

#### 安裝 Chocolatey

官網上提供了幾種方式來進行安裝：Cmd.exe, PowerShell.exe, PowerShell v3+，我這邊使用 `Cmd.exe` 來安裝，在 CMD 中執行以下指令

*安裝 Chocolatey*

![](https://cdn-images-1.medium.com/max/800/0*zkK4OIfcB54AJDSL.png)

*Chocolatey 安裝完畢*

![](https://cdn-images-1.medium.com/max/800/0*rgN2rcQSMmv4bHSA.png)

*確認 Chocolatey 安裝成功*

![](https://cdn-images-1.medium.com/max/800/0*3_SyVtaV8gcsgd47.png)

`若沒有出現指令，可以重開 CMD 視窗`

#### 安裝 git-tf

在 `Cmd.exe` 底下鍵入以下指令即可安裝 `git-tf`

*安裝 git-tf*

![](https://cdn-images-1.medium.com/max/800/0*kAYRbi_vbbl2ZCp1.png)

*git-tf 安裝完畢*

![](https://cdn-images-1.medium.com/max/800/0*ndGgr8Jh0g5kjjkq.png)

*確認 git-tf 安裝成功*

![](https://cdn-images-1.medium.com/max/800/0*X0N-ZysLMDiGgsX-.png)

### Step 2 — 複製專案

透過指令從 TFS 或 visualstudio.com 複製 TFS 專案到本機指定的目錄下

*複製 TFS 專案*

![](https://cdn-images-1.medium.com/max/800/0*hZCjhAMZvuwyAw0i.png)

*複製 TFS 專案完畢*

![](https://cdn-images-1.medium.com/max/800/0*89IrDJGjNDiXODF5.png)

*複製完後之資料夾列表*

![](https://cdn-images-1.medium.com/max/800/0*mq_731D3h-04GI-F.png)

*複製完後之 CHANGELOG*

![](https://cdn-images-1.medium.com/max/800/0*a_TZ3rwQI-U6fFxd.png)

開始執行後，將會需要輸入驗證資訊(如果是使用 visualstudio.com，則需要使用**替代驗證方式**)，一旦輸入完畢且驗證成功後，就會開始複製階段，其花費的時間會依據變更集的數量與 repository 的大小而定

### Step 3. 環境整理與設定

複製完畢後，其版本控制就已經變成一個本地的 git repository，接下來就是要把 TFS 版控的一些檔案與設定給刪除，並加上 GIT 的一些設定檔

### Step 4 . Commit & Push

![](https://cdn-images-1.medium.com/max/800/0*sX5luelR7VajqvFm.png)

完成以上步驟後，就已建立包含變更集完整的 GIT repository，接下來就看要把這個 repository 發行到哪裡去，例如說 GitHub、Bitbucket 或 visualstudio.com

那發行這部分就不再介紹了~

### 參考資料

* [Migrate an existing project from TFS to Git with changeset history intact](http://chriskirby.net/blog/migrate-an-existing-project-from-tfs-to-github-with-changeset-history-intact)
* [Chocolatey](https://chocolatey.org/)
* [git-tf](https://gittf.codeplex.com/)