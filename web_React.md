---
title:前端開發學習筆記-React
vlook-doc-lib:
- [筆記網站跳轉](index.html?target=_self "快速挑轉到想要的網頁")
- [前端開發學習筆記★HTML](web_HTML.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★CSS](web_CSS.html?target=_self "網頁開發學習筆記★CSS")
- [前端開發學習筆記★JS](web_JS.html?target=_self "網頁開發學習筆記★JS")
- [前端開發學習筆記★React](web_React.html?target=_self "網頁開發學習筆記★React")
---

######  ~VLOOK™~ *[<kbd>![](icon/vlook-hollow-dark.svg) VLOOK ![](icon/icon-more.svg)</kbd>](https://github.com/MadMaxChow/VLOOK)*<br>前端開發學習筆記-React──<br><u>簡介</u><br>*本篇筆記是使用[<kbd>![](icon/Typora.svg) Typora</kbd>](https://typora.io/)及[<kbd>![](icon/markdown.svg) Markdown</kbd>](https://markdown.tw/)<br>結合GitHub開源模版撰寫而成並導出成HTML*<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`* *版本日期`2025年6月1日`*

[TOC]

# 什麼是React

React 是一個由 **Facebook (現在的 Meta)** 開發的 **JavaScript 框架**，專門用來建構使用者介面 (UI)

**傳統網頁開發的痛點**

- **DOM 操作複雜** - 手動管理網頁元素變化很繁瑣
- **狀態管理混亂** - 資料變化時，很難追蹤哪些地方需要更新
- **程式碼重複** - 相似的功能需要重複寫很多次
- **維護困難** - 專案變大後，程式碼變得難以理解和修改

**React 的解決方案**

React 引入了「**元件化**」的開發方式，把複雜的介面拆解成一個個獨立的「元件」，還有**豐富的第三方套件** - 幾乎任何功能都有現成的解決方案

> [!note]
>
> **元件化開發**
>
> - 每個元件負責自己的功能，可以重複使用
> - 容易測試和維護

## 快速搭建開發環境

*^tab^*

> **Node.js安裝**
>
> *[<kbd>![](icon/logo.svg) Node.js  ![](icon/icon-more.svg?fill=text)</kbd>](https://nodejs.org/zh-tw/download)*
>
> **Windows：**
>
> 1. 按 `Win + R`
> 2. 輸入 `cmd`，按 Enter
> 3. 在黑色視窗中輸入：`node --version`
> 4. 應該會顯示版本號（例如：v18.17.0）
>
> **Mac：**
>
> 1. 按 `Cmd + 空白鍵`
> 2. 輸入 `terminal`，按 Enter
> 3. 輸入：`node --version`
> 4. 應該會顯示版本號
>
> 能顯示版本號，代表Node.js已經安裝成功

> **建立React專案**
>
> 1. 選擇專案位置
>
>    建議在桌面或是資料夾建立一個叫 `my-react-projects` 的專案
>
> 2. 開啟終端機
>
>    cd 進入`my-react-projects` 專案資料夾
>
> 3. 建立React專案
>
>    ```bash
>    npx create-react-app my-first-app
>    ```
>
>    > [!note]
>    >
>    > * **npx**：Node.js工具命令，尋找並執行後續的包命令
>    > * **create-react-app**：核心包（固定寫法），用於建立React項目
>    > * **my-first-app**：React項目的名稱（可以自訂）
>
>    ![ClShot 2025-09-10 at 22.26.03@2x](web_React.assets/ClShot 2025-09-10 at 22.26.03@2x.png)
>
> 4. 啟動專案
>    ```bash
>    npm start
>    ```

> **調整專案檔案結構**
>
> 因為目前學習可以先把不需要的檔案暫時移除，src資料夾中只保留
>
> * App.js
>
>   ```jsx
>   function App() {
>     return (
>       <div className="App">
>         this is app
>       </div>
>     );
>   }
>   
>   export default App;
>   ```
>
> * index.js
>
>   ```jsx
>   import React from 'react';
>   import ReactDOM from 'react-dom/client';
>   import App from './App';
>   
>   const root = ReactDOM.createRoot(document.getElementById('root'));
>   root.render(<App />);
>   ```

**index.js程式的入口**

告訴瀏覽器「React 要在哪裡顯示」

* 引入 React核心套件

  ```jsx
  import React from 'react';
  import ReactDOM from 'react-dom/client';
  ```

  - 就像「引入工具箱」

  - 讓你可以使用 React 的功能

* 引入專案根套件

  ```jsx
  import App from './App';
  ```

  - 引入 App.js 這個檔案

  - App 就是你的主要元件

* 選染網頁

  ```jsx
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(<App />);
  ```

  - `document.getElementById('root')` = 找到 public/index.html 中 id 為 'root' 的元素
  - `render(<App />)` = 把 App 元件顯示在那個位置

**App.js專案的根套件**

定義你的網頁長什麼樣子

* 被引入到index.js中，選染到public/index.html(root)中

  ```jsx
  function App() {
    return (
      <div className="App">
        this is app
      </div>
    );
  }
  
  export default App;
  ```

# JSX概念

==**JSX = JavaScript + XML**==

JavaScript 中寫 HTML，他是React中編寫UI模版的方式，JSX並不是標準的JS語法，它是**JS的語法擴展**，瀏覽器本身不能識別，需要通過**解析工具做解析**之後才能在瀏覽器中運行

JSX優勢：

- 看起來像 HTML
- 可以嵌入 JavaScript
- 讓程式碼更易讀
- 支援所有 HTML 標籤

*[<kbd>![](icon/logo.svg) Babel解析工具  ![](icon/icon-more.svg?fill=text)</kbd>](https://babeljs.io/repl)*

![ClShot 2025-09-10 at 22.58.34@2x](web_React.assets/ClShot 2025-09-10 at 22.58.34@2x.png)

---

> **傳統寫法**
>
> ```javascript
> // 用 JavaScript 建立 HTML 元素
> const element = document.createElement('div');
> element.className = 'container';
> element.innerHTML = '<h1>Hello World</h1>';
> document.body.appendChild(element);
> ```

>**JSX方式**
>
>```jsx
>// 直接寫 HTML！
>const element = <div className="container"><h1>Hello World</h1></div>;
>```

## 使用JS表示式

在JSX中可以通過 **大括號語法{}** 識別 JavaScript中的表示式，比如常見的變數、函數呼叫、方法呼叫等等

1. 使用引號傳遞字串
2. 使用JavaScript變數
3. 函數呼叫和方法呼叫
4. 使用JavaScript對象

> [!caution]
>
> if語句、switch語句、變數聲明屬於語句，不是表示式，不能出現在{}中

```jsx
const count = 100

function getName() {
  return "James"
}

function App() {
  return (
    <div className="App">
      {/*傳遞字符串*/}
      {"this is app"}

      {/*使用JavaScript變量*/}
      {count}

      {/*調用JavaScript函數*/}
      {getName()}

      {/*使用JavaScript對象*/}
      <div style={{ color: "red"}}>This is red text</div>
    </div>
  );
}

export default App;
```

## 列表渲染

==在 JSX 中渲染列表，主要用 **`.map()`** 方法==

```jsx
const list = [
  { id: 1, name: "John" },
  { id: 2, name: "Jane" },
  { id: 3, name: "Doe" }
]

function App() {
  return (
    <div className="App">
      <ul>
        {/*兩種寫法都可以*/}
        {list.map(function(item) {
          return <li key={item.id}>{item.name}</li>;
        })}

        {list.map(item => <li key={item.id}>{item.name}</li>)}
      </ul>
    </div>
  );
}

export default App;
```

> [!note]
>
> **為什麼需要 key？**
>
> - React 需要知道哪個項目是哪個
> - 幫助 React 高效更新列表
> - 沒有 key 會有警告訊息，並且key需要**獨一無二**
>
> ```jsx
> // ✅ 正確：每個項目都有唯一的 key
> {items.map(item => <li key={item.id}>{item.name}</li>)}
> 
> // ❌ 錯誤：沒有 key
> {items.map(item => <li>{item.name}</li>)}
> 
> // ⚠️  不推薦：用索引當 key（除非沒有其他選擇）
> {items.map((item, index) => <li key={index}>{item.name}</li>)}
> ```

> [!note]
>
> **箭頭函數的語法規則**
>
> 它是 JavaScript ES6 新增的**寫函數的簡短方式**
>
> ```javascript
> 函數名 = (參數) => { 函數內容 }
> 
> // 傳統寫法
> function sayHello(name) {
>   return "Hello, " + name;
> }
> 
> // 箭頭函數寫法
> const sayHello = name => "Hello, " + name;
> ```

## 條件渲染

![ClShot 2025-09-10 at 23.52.59@2x](web_React.assets/ClShot 2025-09-10 at 23.52.59@2x.png)

在React中，可以通過**邏輯與運算子&&**、**三元表示式（?:）**實現基礎的條件渲染

* **邏輯與運算子&&**

  ```jsx
  let login = true
  
  function App() {
    return (
      <div className="App">
        {login && <span>James</span>}
      </div>
    );
  }
  
  export default App;
  ```

  > [!note]
  >
  > 當login為true時才顯示James，如果為false

* **三元表示式（?:）**

  ```jsx
  let login = true
  
  function App() {
    return (
      <div className="App">
        {login ? <span>James</span> : <span>Error</span>}
      </div>
    );
  }
  
  export default App;
  
  ```

  

# The End<br>*Written by JamesZhan*<br><sub>若是內容有錯誤歡迎糾正 *[<kbd>![](icon/gmail.svg?fill=text) Email</kbd>](mailto:henry16801@gmail.com?subject="內容錯誤糾正(非錯誤糾正可自行更改標題)")*</sub>
