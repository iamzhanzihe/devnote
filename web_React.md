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

## index.js程式的入口

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

## App.js專案的根套件

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
  

# React事件綁定

**事件綁定** = 讓你的網頁元素可以「回應」用戶的操作

比如：

- 按鈕被點擊 → 執行某個動作
- 輸入框內容改變 → 更新資料
- 滑鼠移入 → 顯示提示

```jsx
<元素 on事件名={處理函數}>內容</元素>
```

>[!note]
>
>處理函數整體上遵循駝峰命名法，例如： clickHandler、moveHandler

進行事件綁定前，需要先建立一個事件函數，在綁定到事件上：

```jsx
function App() {
  const clickHandler = () => {
    console.log("按鍵被點擊");
  }

  return (
    <div className="App">
      <button onClick={clickHandler}>click me</button>
    </div>
  );
}

export default App;
```

> [!important]
>
> 這裡 `<button onClick={clickHandler}>click me</button>` 裡面的 `clickHandler` 他是一個**回調函數**等待被執行，並**不是函數執行完的結果**，當點擊事件觸發了才會執行回調函數

## 獲取事件對象參數



**事件參數 `e`**（通常叫做 `event`）是瀏覽器自動傳給事件處理函數的**事件對象**

它包含了關於這個事件的**所有資訊**

```jsx
function App() {
  const clickHandler = (e) =>{
    console.log("按鍵被點擊", e);
  }

  return (
    <div className="App">
      <button onClick={clickHandler}>click me</button>
    </div>
  );
}

export default App;
```

> [!note]
>
> 為什麼 `<button onClick={clickHandler}>click me</button>` 沒有傳入參數，卻可以獲得事件參數e？
>
> 因為當你寫 `onClick={handleClick}` 時，**React 會自動把事件對象當作第一個參數傳給你的函數**！
>
> ```jsx
> // React 內部大概是這樣處理的
> const button = document.createElement('button');
> button.addEventListener('click', (event) => {
>   handleClick(event); // React 自動傳入 event！
> });
> ```
>

## 傳遞自定義參數

當你需要在事件觸發時傳遞自定義參數時，需要在事件綁定的位置**使用箭頭函數來包裝你的處理函數**，這樣就可以在調用時傳入實際參數

1. 事件函數中放入形式參數
2. 改造成箭頭函數，並傳入實際參數

```jsx 
function App() {
  const clickHandler = (name) =>{
    console.log("按鍵被點擊", name);
  }

  return (
    <div className="App">
      <button onClick={() => clickHandler("James")}>click me</button>
      
      {/*<button onClick={function () {clickHandler("James")}}>*/}
      {/*  click me*/}
      {/*</button>*/}
    </div>
  );
}

export default App;
```

> **為什麼要使用箭頭函數？**
>
> React 的事件處理基於**回調函數**模式：
>
> - React 期望你提供一個**函數**，不是函數的執行結果
> - 當事件發生時，React 會**調用**你提供的函數
> - 這就是經典的「稍後調用」回調機制
>
> ---
>
> > **錯誤寫法**
> >
> > ```jsx
> > function WrongExample() {
> >     const handleClick = (param) => {
> >        console.log('處理參數：', param);
> >        return '執行結果';
> >     };
> > 
> >     return (
> >        // ❌ 這會在渲染時立即執行函數
> >        <button onClick={handleClick('我的參數')}>
> >          錯誤按鈕
> >        </button>
> >     );
> > }
> > ```
> > 
> > * handleClick('我的參數') 在渲染時立即執行
> >* onClick 得到的是返回值 '執行結果'，不是函數
> > * React 無法調用一個字符串作為回調函數
> > * 點擊時會報錯或無反應
> > 
> > _~Rd~_
>
> > **正確寫法**
> >
> > ```jsx
> > function CorrectExample() {
> >   const handleClick = (param) => {
> >     console.log('處理參數：', param);
> >   };
> > 
> >   return (
> >     // ✅ 提供一個回調函數給 React
> >     <button onClick={() => handleClick('我的參數')}>
> >       正確按鈕
> >     </button>
> >   );
> > }
> > ```
> >
> > * 渲染時：創建箭頭函數 (e) => handleClick('我的參數', e)
> > * onClick 得到這個箭頭函數
> > * 點擊時：React 調用箭頭函數，傳入事件對象
> > * 箭頭函數內部調用 handleClick，傳入自定義參數和事件對象
> >
> > _~Gn~_

## 同時傳遞事件對象和自定義參數

```jsx
function App() {
  const clickHandler = (name, e) =>{
    console.log("按鍵被點擊", name, e);
  }

  return (
    <div className="App">
      <button onClick={(e) => clickHandler("James", e)}>click me</button>
    </div>
  );
}

export default App;
```

> [!note]
>
> `(e) => clickHandler("James", e)` 作為回調函數傳遞給 onClick，當點擊發生時，這個回調函數接收事件對象 e，然後將 "James" 和 e 傳遞給 clickHandler 函數

> [!caution]
>
> 實際參數的位置要和形式參數對應上

# React組件

一個組件就是使用者介面的一部分，它可以有自己的邏輯和外觀，組件之間可以互相嵌套，也可以重複使用多次

在React中，一個組件就是**首字母大寫的函數**，內部存放了組件的邏輯和UI，渲染組件只需要把組件**當成標籤書寫**即可

![ClShot 2025-09-11 at 23.49.07@2x](web_React.assets/ClShot 2025-09-11 at 23.49.07@2x.png)

1. 定義組件

   ```jsx
   function Button() {
     return (
       <button>Click me</button>
     );
   }
   
   // const Button = () => {
   //   return (
   //     <button>Click me</button>
   //   );
   // }
   ```

2. 使用組件

   ```jsx
   function Button() {
     return (
       <button>Click me</button>
     );
   }
   
   // const Button = () => {
   //   return (
   //     <button>Click me</button>
   //   );
   // }
   
   function App() {
   
     return (
       <div className="App">
         {/*單標籤*/}
         <Button/>
         {/*雙標籤*/}
         <Button></Button>
       </div>
     );
   }
   
   export default App;
   ```

## 基礎樣式控制

React組件基礎的樣式控制有兩種方式：

1. **行內樣式（不推薦）**

   ```jsx
   function App() {
   
     return (
       <div className="App">
         <span style={{color: "red", fontSize: "32px"}}>這是span文字</span>
       </div>
     );
   }
   
   export default App;
   ```

2. **class類名控制**

   建議獨立建立一個控制樣式的css檔案，再引入app.js中做使用

   ```css
   .test {
       color: blue;
       font-size: 24px;
   }
   ```

   ```jsx
   import './index.css'
   
   function App() {
   
     return (
       <div className="App">
         <span style={{color: "red", fontSize: "32px"}}>這是span文字</span>
         <span className="test">這是span文字</span>
       </div>
     );
   }
   
   export default App;
   ```

   >[!note]
   >
   >導入CSS樣式必須使用 `className=` ，這是React JSX的規定，因為 `class` 是 JavaScript 的**保留字**（用於定義類）




# useState管理狀態

**useState** 是 React 的一個 **Hook**，讓你在**函數組件**中添加和管理**狀態（state）**，和普通JS變數不同的是，狀態變數一旦發生變化，組件的UI也會跟著變化（**資料驅動視圖**）

![ClShot 2025-09-12 at 00.03.08@2x](web_React.assets/ClShot 2025-09-12 at 00.03.08@2x.png)

```jsx
const [狀態變數, 設定函數] = useState(初始值);
//     ^^^^^^   ^^^^^^        ^^^^
//     當前值   更新狀態的函數   初始狀態值
```

1. 調用useState添加一個狀態變量(**需要導入**)

   ```jsx
   import {useState} from 'react'
   ```
2. 建立點擊事件回調，並更新狀態值

   ```jsx
   function App() {
     // 1. 使用useState添加一個狀態
     const [count, setCount] = useState(0)
   
     // 2. 點擊按鈕回調，更新狀態
     const clickHandler = () => {
       setCount(count + 1)
     }
   
     return (
       <div className="App">
         <button onClick={clickHandler}>{count}</button>
       </div>
     );
   }
   
   export default App;
   ```

## 修改對象狀態

對於對象類型的狀態變數，應該始終**傳給set方法**來進行修改

> [!important]
>
> 在React中，狀態被認為是**唯讀**的，我們應該**始終替換它而不是修改它**，直接修改狀態不能引發視圖更新
>
> ![ClShot 2025-09-12 at 00.22.46@2x](web_React.assets/ClShot 2025-09-12 at 00.22.46@2x.png)

---

> **直接修改對象值**
>
> ```jsx
> import {useState} from 'react';
> 
> function App() {
>   const [form, setForm] = useState({name: "James"});
> 
>   const changeForm = () => {
>     form.name = "Jack"
>   }
> 
>   return (
>     <div className="App">
>       <button onClick={changeForm}>{form.name}</button>
>     </div>
>   );
> }
> 
> export default App;
> ```
>
> _~Rd~_

> **呼叫set傳入新對象修改**
>
> ```jsx
> import {useState} from 'react';
> 
> function App() {
>   const [form, setForm] = useState({name: "James"});
> 
>   const changeForm = () => {
>     setForm({
>       ...form,
>       name: "Jack"
>     })
>   }
> 
>   return (
>     <div className="App">
>       <button onClick={changeForm}>{form.name}</button>
>     </div>
>   );
> }
> 
> export default App;
> ```
>
> _~Gn~_

*[<kbd>![](icon/logo.svg) bilibili練習  ![](icon/icon-more.svg?fill=text)</kbd>](#bilibili評論案例)*

## 控制表單狀態

使用 React 組件的狀態（useState）來控制表單的狀態

![ClShot 2025-09-15 at 22.02.58@2x](web_React.assets/ClShot 2025-09-15 at 22.02.58@2x.png)

1. 準備一個React狀態值，讓input標籤value屬性保持更新

2. 通過value屬性綁定狀態，通過onChange更新變量

```jsx   
import {useState} from "react";

function App() {

  const [value, setValue] = useState('');

  return (
    <div className="App">
    <input
      type="text"
      value={value}
      onChange={(e) => setValue(e.target.value)}/>
    </div>
  );
}

export default App;
```



# 練習

## bilibili評論案例

![ClShot 2025-09-13 at 16.12.13@2x](web_React.assets/ClShot 2025-09-13 at 16.12.13@2x.png)

1. 渲染評論列表

   * 使用useState來渲染評論列表
   * 使用map方法對列表資料進行遍歷渲染（別忘了加key）

   ```jsx
   const [commentList, setCommentList] = useState(defaultList)
   
   {/* 評論列表 */}
   <div className="reply-list">
     {/* 評論項 */}
     {commentList.map(item => (
       <div key={item.rpid} className="reply-item">
         {/* 頭像 */}
         <div className="root-reply-avatar">
           <div className="bili-avatar">
             <img
               className="bili-avatar-img"
               alt=""
               src={item.user.avatar}
             />
           </div>
         </div>
   
         <div className="content-wrap">
           {/* 用戶名 */}
           <div className="user-info">
             <div className="user-name">{item.user.uname}</div>
           </div>
           {/* 評論內容 */}
           <div className="root-reply">
             <span className="reply-content">{item.content}</span>
             <div className="reply-info">
               {/* 評論時間 */}
               <span className="reply-time">{item.ctime}</span>
               {/* 評論數量 */}
               <span className="reply-time">點讚數:{item.like}</span>
               <span className="delete-btn">
               刪除
             </span>
   
             </div>
           </div>
         </div>
       </div>
     ))}
   </div>
   ```

2. 刪除評論實現

   * 只有自己的評論才顯示刪除按鈕(條件過濾)

     ```jsx
     {/* 評論數量 */}
     <span className="reply-time">點讚數:{item.like}</span>
     {user.uid === item.user.uid &&
       <span className="delete-btn" onClick={() => handleDel(item.rpid)}>
         刪除
       </span>
     }
     ```

   * 點選刪除按鈕，刪除當前評論，列表中不再顯示

     ```jsx
     const handleDel = (rid) => {
       console.log(rid)
       setCommentList(commentList.filter((item) => item.rpid !== rid))
     }
     ```

3. 渲染導航Tab和高亮實現

   點誰就把誰的type（獨一無二的標識）記錄下來，然後和遍歷時的每一項的type做匹配，誰匹配到就設定負責高亮的類名

   ```jsx
   <li className="nav-sort">
     {/* 高亮類名： active */}
     {tabs.map(item => (
       <span key={item.type} className={`nav-item ${type === item.type && 'active'}`} onClick={() => handleTabChange(item.type)}>{item.text}</span>
     ))}
   </li>
   ```

   ```jsx
   const [type, setType] = useState("hot")
   
   const handleTabChange = (type) => {
     console.log(type)
     setType(type)
   }
   ```

   > [!note]
   >
   > className={nav-item ${type === item.type && 'active'}} 這樣的寫法不夠整潔，不好讀，可以用第三方套件**通過條件動態控制class類名的顯示**
   >
   > ![ClShot 2025-09-15 at 21.36.10@2x](web_React.assets/ClShot 2025-09-15 at 21.36.10@2x.png)
   >
   > ```bash
   > npm install classnames
   > ```
   >
   > ```jsx
   > <li className="nav-sort">
   >   {/* 高亮類名： active */}
   >   {tabs.map(item => (
   >     <span key={item.type} className={classNames("nav-item", {"active": type===item.type})} onClick={() => handleTabChange(item.type)}>{item.text}</span>
   >   ))}
   > </li>
   > ```
   >
   > 

4. 評論列表排序功能實現

   導入lodash第三方套件，完成排序功能(需要先 `npm install lodash`)

   ![ClShot 2025-09-15 at 21.28.15@2x](web_React.assets/ClShot 2025-09-15 at 21.28.15@2x.png)

   ```jsx
   import _ from 'lodash'
   ```

   ```jsx
   const [type, setType] = useState("hot")
   const handleTabChange = (type) => {
     console.log(type)
     setType(type)
     if (type === "hot") {
       // 根據點讚數量排序
       setCommentList(_.orderBy(commentList, 'like', 'desc'))
     } else {
       // 根據發布時間排序
       setCommentList(_.orderBy(commentList, 'ctime', 'desc'))
     }
   }
   ```



# The End<br>*Written by JamesZhan*<br><sub>若是內容有錯誤歡迎糾正 *[<kbd>![](icon/gmail.svg?fill=text) Email</kbd>](mailto:henry16801@gmail.com?subject="內容錯誤糾正(非錯誤糾正可自行更改標題)")*</sub>
