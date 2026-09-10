---
title: "讓 LLM 自動化你的 N8N 工作流程：n8n-mcp-server 安裝指南"
datePublished: 2025-05-28T04:51:37.991Z
cuid: cmb7gx47b000b09l1c7pw32bo
slug: llm-n8n-mcp-server
ogImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748407343549/8deb1cc0-3a5e-47fa-8576-c12c67ae3861.png
tags: n8n, llm, generative-ai, mcp

---

## 前言

網路上一大堆都是在介紹如何在 N8N 裡面用 MCP 來呼叫其他工具，但是更多時候我希望 LLM 能直接幫我寫好或是修改 N8N 的工作流程

所以這篇就來介紹如何設定與使用 [**n8n-mcp-server**](https://github.com/leonardsellem/n8n-mcp-server) 來讓 LLM 幫忙操控 N8N

在 GitHub 上有不少的 n8n-mcp-server，經過一下下的簡單搜索，我決定使用這個專案: [**n8n-mcp-server**](https://github.com/leonardsellem/n8n-mcp-server)

原因在於說這個專案的實作提供了基本上所有需要編輯工作流程的功能，以下就來記錄安裝過程

---

## MCP Server 設定

首先當然要先有 Node.JS 的環境，這邊就不多作介紹了

我這邊使用的是 Local 的 MCP Server 模式

先透過以下指令將 Repo 複製到本地

```bash
# Clone the repository
git clone https://github.com/leonardsellem/n8n-mcp-server.git
cd n8n-mcp-server
```

接下來就要透過 NPM 來安裝相依的套件，但是在這邊有一個要注意的地方

這個專案在 package.json 裡面有一個指令是只支援 Unix 環境，若直接在 Windows 環境下執行會掛掉

若你是 Windows 作業系統需要打開在根目錄下的 package.json，編輯 scripts/build 的段落，移除 `&& chmod +x build/index.js` 後存檔

```json
{
  "name": "n8n-mcp-server",
  "version": "0.1.0",
  "description": "Model Context Protocol (MCP) server for n8n workflow automation",
  "main": "build/index.js",
  "type": "module",
  "scripts": {
    // 編輯這一行，移除 '&& chmod +x build/index.js'，變成如下樣子
    "build": "tsc",
    "start": "node build/index.js",
    "dev": "tsc -w",
    "lint": "eslint --ext .ts src/",
    "test": "node --experimental-vm-modules run-tests.js",
    "test:watch": "node --experimental-vm-modules run-tests.js --watch",
    "test:coverage": "node --experimental-vm-modules run-tests.js --coverage",
    "prepare": "npm run build"
  }
}
```

編輯完後就可以執行以下指令

```bash
# Install dependencies
npm install

# Build the project
npm run build
```

最終應該會得到類似以下畫面

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748405705321/080e8661-cf81-4497-8e47-7b2216c98e61.png align="center")

到此為止，我們就將地端的 n8n-mcp-server 設定完成，接下來我們就要來設定 MCP Client 端

---

## MCP Client 設定

我這邊使用 Claude Desktop 作為範例，但是可以應用到所有的 MCP Client 端，如: VSCode、Cline 等等

這邊打開 Claude 的 MCP 設定 JSON

加入以下相關設定

```json
{
  "mcpServers": {
    // Give your server a unique name
    "n8n-local": {
      // Use 'node' to execute the built JavaScript file
      "command": "node",
      // Provide the *absolute path* to the built index.js file
      "args": [
        "/path/to/your/cloned/n8n-mcp-server/build/index.js"
        // On Windows, use double backslashes:
        // "C:\\path\\to\\your\\cloned\\n8n-mcp-server\\build\\index.js"
      ],
      // Environment variables needed by the server
      "env": {
        "N8N_API_URL": "http://your-n8n-instance:5678/api/v1", // Replace with your n8n URL
        "N8N_API_KEY": "YOUR_N8N_API_KEY", // Replace with your key
        // Add webhook credentials only if you plan to use webhook tools
        "N8N_WEBHOOK_USERNAME": "your_webhook_user",
        "N8N_WEBHOOK_PASSWORD": "your_webhook_password"
      },
      // Ensure the server is enabled
      "disabled": false,
      // Default autoApprove settings
      "autoApprove": []
    }
    // ... other servers might be configured here
  }
}
```

這邊需要注意一個地方，就是即使你沒有使用 N8N Webhook 相關功能，也請保留對應的設定，因為目前有 BUG，若找不到對應設定會直接出錯: `Failed to start n8n MCP Server: McpError: MCP error 1000: Missing required environment variable: N8N_WEBHOOK_USERNAME`，可參考對應 issue: [Issue connecting to n8n-mcp-server · Issue #1 · leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server/issues/1)、[N8N\_WEBHOOK\_USERNAME 和N8N\_WEBHOOK\_PASSWORD 必填要求 · Issue #13 · leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server/issues/13)

---

## 開始使用

完成後我們就可以實際來操作看看

1. 幫我整理有哪些 Workflow
    

```markdown
User:
幫我看看 n8n 現在有哪些 workflow

Claude: 
我來幫您查看 n8n 中現有的工作流程。您的 n8n 實例中目前有 **2 個工作流程**：

## 工作流程清單

### 1. 📍 Raindrop Knowledge Management
- **狀態**：已啟用 ✅
- **工作流程 ID**：E1OK2GVGla40YBIp
- **最後更新**：2025年5月27日 17:53

### 2. 📋 Raindrop 知識自動整理 copy
- **狀態**：未啟用 ⏸️
- **工作流程 ID**：NRyh6e2T1Qanz5xX
- **最後更新**：2025年5月27日 17:51

## 觀察

看起來您有兩個相關的 Raindrop 知識管理工作流程，其中一個是另一個的副本。目前只有原始的 "Raindrop Knowledge Management" 工作流程正在運行。

如果您想要查看某個特定工作流程的詳細配置，或者需要啟用/停用某個工作流程，請告訴我！
```

2. 刪除對應 Workflow
    

```markdown
User:
幫我刪除 工作流程 ID：NRyh6e2T1Qanz5xX flow

Claude: 
我來幫您刪除工作流程 ID 為 `NRyh6e2T1Qanz5xX` 的 "Raindrop 知識自動整理 copy" 工作流程。✅ **工作流程刪除成功**

工作流程 "Raindrop 知識自動整理 copy" (ID: NRyh6e2T1Qanz5xX) 已成功刪除。

現在您的 n8n 實例中只剩下一個工作流程：
- **Raindrop Knowledge Management** (已啟用)
```

---

### 可用功能

以下是所有 LLM 可以用的功能，可參考 [**Available Tools**](https://github.com/leonardsellem/n8n-mcp-server?tab=readme-ov-file#available-tools)

**工作流程管理**

* `workflow_list`: 列出所有工作流程
    
* `workflow_get`: 獲取特定工作流程的詳細資訊
    
* `workflow_create`: 建立新的工作流程
    
* `workflow_update`: 更新現有的工作流程
    
* `workflow_delete`: 刪除工作流程
    
* `workflow_activate`: 啟用工作流程
    
* `workflow_deactivate`: 停用工作流程
    

**執行管理**

* `execution_run`: 透過 API 執行工作流程
    
* `run_webhook`: 透過 webhook 執行工作流程
    
* `execution_get`: 獲取特定執行的詳細資訊
    
* `execution_list`: 列出工作流程的執行記錄
    
* `execution_stop`: 停止正在運行的執行