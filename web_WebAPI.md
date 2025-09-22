[TOC]

# 什麼是Web API

**Web API**（Web Application Programming Interface）是瀏覽器提供給 JavaScript 的一系列介面和功能，讓我們可以操作瀏覽器環境、DOM、網路請求等等

* **DOM**：**操作瀏覽器本身的功能**
* **BOM**：**操作網頁文件內容**

# 什麼是DOM

**DOM**（Document Object Model，文件物件模型）是瀏覽器將 HTML 文件轉換成 JavaScript 可以操作的**物件樹狀結構**

想像 HTML 是一棟房子的**藍圖**，DOM 就是根據藍圖蓋出來的**實體房子**，而 JavaScript 就是可以進入房子裡**重新裝潢**的工人

---

> **原始 HTML 文件**
>
> ```html
> <!DOCTYPE html>
> <html>
> <head>
>   <title>我的網頁</title>
> </head>
> <body>
>   <h1 id="title">歡迎來到我的網站</h1>
>   <p class="intro">這是一個段落</p>
>   <button onclick="sayHello()">點我</button>
> </body>
> </html>
> ```

> **轉換成 DOM 樹狀結構**
>
> ```html
> Document
> └── html
>     ├── head
>     │   └── title
>     │       └── "我的網頁"
>     └── body
>         ├── h1 (id="title")
>         │   └── "歡迎來到我的網站"
>         ├── p (class="intro")
>         │   └── "這是一個段落"
>         └── button (onclick="sayHello()")
>             └── "點我"
> ```

> [!important]
>
> 文件樹直觀的體現了標籤與標籤之間的關係

## DOM 物件的定義

==**DOM 物件**就是瀏覽器將每個 HTML 元素轉換成的 **JavaScript 物件**==

讓我們可以用程式碼操作網頁元素，可以把每一個的HTML標籤自動都看成是一個JavaScript的物件，網頁所有內容都在document裡面

![ClShot 2025-09-15 at 22.50.39@2x](web_WebAPI.assets/ClShot 2025-09-15 at 22.50.39@2x.png)

> [!TIP]
>
> body、head 標籤在HTML中是唯一的， 可以直接使用 `document.body`、`document.head` 直接得到JavaScript物件

## 獲取DOM元素

想要操作某個標籤肯定首先選中這個標籤，跟 CSS選擇器類似，選中標籤才能操作，操作DOM有兩種方式：

* **現代方式（較新的 API）**

  * 選取第一個符合的元素：`querySelector(CSS選擇器)`

    ```html
    <body>
      <div class="test">這是div標籤</div>
      <script>
        const d1 = document.querySelector('div')
        //const d1 = document.querySelector('.test')
        console.log(d1);
      </script>
    </body>
    ```

    > [!note]
    >
    > querySelector**只匹配第一個元素**，**可以直接進行修改操作**
    >
    > 回傳一個 HTMLElement對象，如果沒有匹配到，則返回null

  * 選取所有符合的元素：`querySelectorAll()`

    ```html
    <body>
      <ul>
        <li>test1</li>
        <li>test2</li>
        <li>test3</li>
      </ul>
      <script>
        const d1 = document.querySelectorAll('ul li')
        console.log(d1);
      </script>
    </body>
    ```

    >[!note]
    >
    >querySelectorAll**匹配所有相符元素**，不可以直接修改，需要for循環遍歷
    >
    >回傳一個NodeList物件偽陣列(沒有 pop()、push() 等陣列方法)，如果沒有匹配到，則返回NodeList[]空陣列

* 傳統方式（較舊的 API）

  * getElementById() - 透過 ID 選取
  * getElementsByClassName() - 透過 Class 選取
  * getElementsByTagName() - 透過標籤名稱選取
  * getElementsByName() - 透過 name 屬性選取

## 操作元素內容

DOM對象都是根據標籤生成的，所以操作標籤本質上就是操作DOM對象，使用的點語法：

* 物件.innerText 屬性

  ```html
  <body>
    <div class="test">測試</div>
    <script>
      const d1 = document.querySelector('div')
      console.log(d1.innerText);
      d1.innerText = '修改值'
      // d1.innerHTML = '<strong>修改值</strong>'  純文字顯示不會解析標籤
    </script>
  </body>
  ```

* 物件.innerHTML 屬性

  ```html
  <body>
    <div class="test">測試</div>
    <script>
      const d1 = document.querySelector('div')
      console.log(d1.innerHTML);
      d1.innerHTML = '<strong>修改值</strong>'
    </script>
  </body>
  ```

> [!TIP]
>
> `元素.innerHTML` 屬性能識別文字，也能夠解析標籤，如果不知道要用哪一個，可以直接選擇innerHTML

## 操作元素屬性

可以透過：

```javascript
物件.屬性 = 值
```

修改常見的屬性href、title、src 等

```html
<body>
  <img src="./image/01.jpg">
  <script>
    const p1 = document.querySelector('img')
    // 更換圖片
    p1.src = './image/02.jpg'
    p1.title = 'test'
  </script>
</body>
```

## 修改元素樣式

可以透過：

* **通過 style 屬性操作CSS**

  ```javascript
  物件.style.樣式屬性 = 值
  ```

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dom</title>
    <style>
      div {
        width: 300px;
        height: 300px;
        background-color: pink;
      }
    </style>
  </head>
  
  <body>
    <div></div>
    <script>
      div = document.querySelector('div')
      div.style.width = '500px'
      // div.style.background-color = "black"
      div.style.backgroundColor = "black"
    </script>
  </body>
  
  </html>
  ```

  > [!caution]
  >
  > * 如果CSS屬性有**-連接符**，需要轉換為**小駝峰命名法**
  > * 賦值的時候，要加CSS單位

* **操作類名(className) 操作CSS**

  如果修改的樣式比較多，直接通過style屬性修改比較繁瑣，我們可以通過CSS類名的形式

  ```javascript
  物件.classname = 'CSS類名' 
  ```

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dom</title>
    <style>
      .test {
        width: 300px;
        height: 300px;
        background-color: pink;
      }
  
      .red {
        color: red;
      }
    </style>
  </head>
  
  <body>
    <div>123</div>
    <script>
      div = document.querySelector('div')
      div.className = 'test red'
    </script>
  </body>
  
  </html>
  ```

  > [!caution]
  >
  > * 由於class是關鍵字，所以使用className去代替
  > * className是使用**新值換舊值**，如果需要新增一個類，需要保留之前的類名

* **通過 classList 操作類控制CSS(推薦)**_~Rd~_

  為了解決className 容易覆蓋以前的類名，我們可以通過classList方式追加和刪除類名

  * add() - 添加類別

    ```javascript
    element.classList.add('new-class');
    element.classList.add('class1', 'class2', 'class3'); // 一次添加多個
    ```

  * remove() - 移除類別

    ```javascript
    element.classList.remove('old-class');
    element.classList.remove('class1', 'class2'); // 一次移除多個
    ```

  * toggle() - 切換類別

    ```javascript
    element.classList.toggle('active'); // 如果有就移除，沒有就添加
    ```

## 修改表單屬性

表單很多情況也需要修改屬性，比如點選眼睛可以看到密碼，本質是把密碼類型轉換為文字

```javascript
表單.value = '表單值'
表單.type = '表單類型'
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dom</title>
  <style>

  </style>
</head>

<body>
  <input type="password" value="123" />
</body>
<script>
  text = document.querySelector('input')
  text.type = 'text'
  text.value = '321'
</script>

</html>
```

表單屬性中新增效果、移除效果，一律使用布林值表示，比如： disabled、checked、selected

* true ：代表新增了該屬性
* false： 代表移除了該屬性

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dom</title>
  <style>

  </style>
</head>

<body>
  <input type="checkbox" value="123" />
</body>
<script>
  text = document.querySelector('input')
  // console.log(text.checked)
  text.checked = true
</script>

</html>
```

> [!caution]
>
> true是布林值，不是字串，**不要加雙引號**

## 自定義屬性

因為HTML 標準屬性有限，當我們需要儲存更多資訊時又想要有統一的格式就會使用自定義屬性

* **標準屬性**：標籤天生自帶的屬性，比如class、id、title等，可以直接使用點語法操作比如： disabled、checked、selected
* **自定義屬性**：在html5中推出專門的 `data-` 自訂屬性，在標籤上一律以data-開頭，DOM物件上一律以 `dataset` 對象方式獲取

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dom</title>
</head>

<body>
  <div data-id="1">1</div>
  <div data-id="2">2</div>
  <div data-id="3">3</div>
  <div data-id="4">4</div>
  <div data-id="5">5</div>
</body>
<script>
  data = document.querySelector('div')
  console.log(data.dataset.id); // 1
</script>

</html>
```

# 事件監聽

事件是程式設計中的一個基本概念，代表**在程式執行過程中發生的特定動作或狀況**，程式可以透過**事件監聽機制來偵測這些事件的發生**，並**執行相對應的處理函數來回應**用戶的操作或系統的變化，從而實現**互動式和響應式**的程式行為

語法：

```javascript
物件.addEventListener('事件類型', 要執行的函數)
```

事件監聽三要素：

* **事件源**：  那個dom元素被事件觸發了，要獲取dom元素   

* **事件類型**： 用什麼方式觸發，比如滑鼠點選 click、滑鼠經過 mouseover 等

  | 事件分類       | 事件名稱     | 觸發時機     | 常用場景             | 程式碼範例                                        |
  | -------------- | ------------ | ------------ | -------------------- | ------------------------------------------------- |
  | **🖱️ 鼠標事件** | `click`      | 鼠標點擊     | 按鈕點擊、連結導航   | `element.addEventListener('click', handler)`      |
  | :              | `mouseenter` | 鼠標經過     | 懸停效果、提示顯示   | `element.addEventListener('mouseenter', handler)` |
  | :              | `mouseleave` | 鼠標離開     | 隱藏提示、恢復狀態   | `element.addEventListener('mouseleave', handler)` |
  | **🎯 焦點事件** | `focus`      | 獲得焦點     | 輸入框激活、高亮顯示 | `input.addEventListener('focus', handler)`        |
  | :              | `blur`       | 失去焦點     | 驗證輸入、保存數據   | `input.addEventListener('blur', handler)`         |
  | **⌨️ 鍵盤事件** | `keydown`    | 鍵盤按下觸發 | 快捷鍵、即時響應     | `element.addEventListener('keydown', handler)`    |
  | :              | `keyup`      | 鍵盤抬起觸發 | 輸入完成檢測         | `element.addEventListener('keyup', handler)`      |
  | **📝 文本事件** | `input`      | 用戶輸入事件 | 即時搜索、表單驗證   | `input.addEventListener('input', handler)`        |

* **事件呼叫的函數**： 要做什麼事

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>事件監聽</title>
</head>

<body>
  <button>click me</button>
</body>
<script>
  const btn = document.querySelector('button')
  btn.addEventListener('click', () => {
    alert('clicked')
  })
</script>

</html>
```

*[<kbd>![](icon/logo.svg) 隨機點名  ![](icon/icon-more.svg?fill=text)</kbd>](#隨機點名)*

## 事件監聽版本

* **DOM L0**：事件源.on事件 = function() { }

  ```javascript
  button.onclick = function() {
    console.log('第一個處理函數');
  };
  
  button.onclick = function() {
    console.log('第二個處理函數');
  };
  
  // 點擊按鈕只會輸出：第二個處理函數
  // 第一個被覆蓋了！
  ```

* **DOM L2**：事件源.addEventListener(事件， 事件處理函數)

  ```javascript
  button.addEventListener('click', function() {
    console.log('第一個處理函數');
  });
  
  button.addEventListener('click', function() {
    console.log('第二個處理函數');
  });
  
  // 點擊按鈕會輸出：
  // 第一個處理函數
  // 第二個處理函數
  // 兩個都會執行！✅
  ```

>[!tip]
>
>on方式會被覆蓋，addEventListener方式可以多次綁定，擁有事件更多特性，推薦使用

|     特性     | DOM L0 (on方式) | DOM L2 (addEventListener) |
| :----------: | :-------------: | :-----------------------: |
| **重複綁定** |   ❌ 會被覆蓋    |      ✅ 可以綁定多次       |
| **事件特性** |   ❌ 功能有限    |        ✅ 功能完整         |
|  **相容性**  |  ✅ 所有瀏覽器   |       ✅ 現代瀏覽器        |
|  **靈活性**  |     ❌ 較低      |          ✅ 較高           |
|  **推薦度**  |    ❌ 不推薦     |      ✅ **強烈推薦**       |

|      等級       | 年份  |     特色      |      事件處理      |
| :-------------: | :---: | :-----------: | :----------------: |
| **DOM Level 0** | 1990s | 最早期的 DOM  |   `on事件` 屬性    |
| **DOM Level 1** | 1998  | 基本 DOM 結構 |    沒有事件規範    |
| **DOM Level 2** | 2000  | 加入事件模型  | `addEventListener` |
| **DOM Level 3** | 2004  | 擴展事件類型  |    更多事件類型    |
| **DOM Level 4** | 2015+ | 現代 DOM API  |     持續演進中     |

## 事件物件

**事件物件**是當事件被觸發時，瀏覽器自動創建並傳遞給事件處理函數的一個**包含事件詳細資訊的物件**

- 🎯 **事件類型** (什麼事件)
- 📍 **事件目標** (發生在哪個元素)
- ⏰ **事件時間** (什麼時候發生)
- 📊 **事件詳情** (滑鼠位置、按鍵等)

```javascript
element.addEventListener('click', function(e) {
    // 這個 e 就是事件對象！
    console.log(event); // 包含了事件的所有資訊
});
```

![ClShot 2025-09-21 at 16.17.15](web_WebAPI.assets/ClShot 2025-09-21 at 16.17.15.png)

常用屬性：

|    屬性分類    |     屬性名稱      |                   描述                   | 適用事件類型 |        實際應用場景        |
| :------------: | :---------------: | :--------------------------------------: | :----------: | :------------------------: |
| **📋 基本屬性** |      `type`       |            獲取當前的事件類型            |   所有事件   |   判斷事件類型、條件處理   |
| **🖱️ 滑鼠座標** | `clientX/clientY` | 獲取光標相對於瀏覽器可見窗口左上角的位置 |   滑鼠事件   |   跟隨滑鼠效果、拖拽功能   |
| **🎯 元素座標** | `offsetX/offsetY` |  獲取光標相對於當前DOM元素左上角的位置   |   滑鼠事件   |  元素內精確定位、繪圖應用  |
| **⌨️ 鍵盤輸入** |       `key`       |           用戶按下的鍵盤鍵的值           |   鍵盤事件   | 快捷鍵、表單驗證、遊戲控制 |

*[<kbd>![](icon/logo.svg) 評論字數統計  ![](icon/icon-more.svg?fill=text)</kbd>](#評論字數統計)*

## 環境物件this

**`this`** 是 JavaScript 中的一個**特殊關鍵字**，它指向**當前執行環境的對象**。`this` 的值會根據**函數被調用的方式**而動態改變

```javascript
// this 就像是一個「代名詞」
// 它指向「誰在執行這個函數」

function test() {
  console.log(this);
}
test()
// window.tesst()

// 當函數獨立調用時，this 會採用「默認綁定」規則，指向window
```

![ClShot 2025-09-21 at 16.45.42](web_WebAPI.assets/ClShot 2025-09-21 at 16.45.42.png)

```javascript
const btn = document.querySelector('button')
btn.addEventListener('click', function () {
  console.log(this);
})
```

![ClShot 2025-09-21 at 16.48.35](web_WebAPI.assets/ClShot 2025-09-21 at 16.48.35.png)

>[!important]
>
>* **誰呼叫， this 就是誰**
>* 直接呼叫函數，其實相當於是 window.函數，所以 this 指 window
>* **箭頭函數沒有this**

## 回調函數

**回調函數**是一個**作為參數傳遞給另一個函數**的函數，並在**特定時機被調用**

* 設定定時器，當時間一到就會觸發某個函數
* 觸發事件時，執行某函數

```javascript
// 回調函數就是「稍後調用」的函數
function greet(name, callback) {
  console.log('Hello ' + name);
  callback(); // 在這裡調用回調函數
}

function sayGoodbye() {
  console.log('Goodbye!');
}

// sayGoodbye 就是回調函數
greet('Alice', sayGoodbye);
// 輸出：
// Hello Alice
// Goodbye!
```

>[!tip]
>
>* 回呼函數本質還是函數，只不過把它當成參數使用
>* 使用匿名函數做為回呼函數比較常見



# 練習

## 隨機點名

* 點選開始按鈕隨機抽取陣列的一個資料，放到頁面中
* 點選結束按鈕刪除陣列當前抽取的一個資料
* 當抽取到最後一個資料的時候，兩個按鈕同時停用（寫點開始裡面，只剩最後一個資料不用抽了）

![ClShot 2025-09-21 at 14.58.22](web_WebAPI.assets/ClShot 2025-09-21 at 14.58.22.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
      * {
          margin: 0;
          padding: 0;
      }

      h2 {
          text-align: center;
      }

      .box {
          width: 600px;
          margin: 50px auto;
          display: flex;
          font-size: 25px;
          line-height: 40px;
      }

      .qs {

          width: 450px;
          height: 40px;
          color: red;

      }

      .btns {
          text-align: center;
      }

      .btns button {
          width: 120px;
          height: 35px;
          margin: 0 50px;
      }
  </style>
</head>

<body>
  <h2>隨機點名</h2>
  <div class="box">
      <span>名字是：</span>
      <div class="qs">這裡顯示姓名</div>
  </div>
  <div class="btns">
      <button class="start">開始</button>
      <button class="end">結束</button>
  </div>

  <script>
      // 資料陣列
      const arr = ['馬超', '黃忠', '趙雲', '關羽', '張飛']
      const content = document.querySelector('.qs')
      let timer = 0
      let random = 0

      // 開始按鍵
      const start = document.querySelector('.start')
      start.addEventListener('click', () => {
          timer = setInterval(() => {
              random = parseInt(Math.random() * arr.length)
              content.innerHTML = arr[random]
          }, 50)

          if (arr.length === 1) {
              start.disabled = true
              end.disabled = true
          }
      })

      // 結束按鍵
      const end = document.querySelector('.end')
      end.addEventListener('click', () => {
          clearInterval(timer)

          // 抽選到的要刪除
          arr.splice(random, 1)
          console.log(arr);

      })
  </script>
</body>

</html>
```

## 評論字數統計

* 點擊textarea時，顯示字數總計：離開textarea時，隱藏字數總計
* 檢測輸入事件，並統計字數
* 按下Enter發布評論，並清空textarea

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>評論回車發佈</title>
  <style>
    .wrapper {
      min-width: 400px;
      max-width: 800px;
      display: flex;
      justify-content: flex-end;
    }

    .wrapper textarea {
      outline: none;
      border-color: transparent;
      resize: none;
      background: #f5f5f5;
      border-radius: 4px;
      flex: 1;
      padding: 10px;
      transition: all 0.5s;
      height: 30px;
    }

    .wrapper textarea:focus {
      border-color: #e4e4e4;
      background: #fff;
      height: 50px;
    }

    .wrapper button {
      background: #00aeec;
      color: #fff;
      border: none;
      border-radius: 4px;
      margin-left: 10px;
      width: 70px;
      cursor: pointer;
    }

    .wrapper .total {
      margin-right: 80px;
      color: #999;
      margin-top: 5px;
      opacity: 0;
      transition: all 0.5s;
    }

    .list {
      min-width: 400px;
      max-width: 800px;
      display: flex;
    }

    .list .item {
      width: 100%;
      display: flex;
    }

    .list .item .info {
      flex: 1;
      border-bottom: 1px dashed #e4e4e4;
      padding-bottom: 10px;
    }

    .list .item p {
      margin: 0;
    }

    .list .item .name {
      color: #FB7299;
      font-size: 14px;
      font-weight: bold;
    }

    .list .item .text {
      color: #333;
      padding: 10px 0;
    }

    .list .item .time {
      color: #999;
      font-size: 12px;
    }
  </style>
</head>

<body>
  <div class="wrapper">
    <textarea id="tx" placeholder="發一條友善的評論" rows="2" maxlength="200"></textarea>
    <button>發佈</button>
  </div>
  <div class="wrapper">
    <span class="total">0/200字</span>
  </div>
  <div class="list">
    <div class="item" style="display: none;">
      <div class="info">
        <p class="name">清風徐來</p>
        <p class="text">大家都辛苦啦，感謝各位大大的努力，能圓滿完成真是太好了[笑哭][支援]</p>
        <p class="time">2022-10-10 20:29:21</p>
      </div>
    </div>
  </div>
  <script>
    const text = document.querySelector('#tx')
    const total = document.querySelector('.total')
    const item = document.querySelector('.item')
    const infoText = document.querySelector('.text')


    // 點擊textarea時，顯示/隱藏字數總計
    text.addEventListener('focus', () => {
      total.style.opacity = 1
    })
    text.addEventListener('blur', () => {
      total.style.opacity = 0
    })

    // 檢測輸入事件
    tx.addEventListener('input', () => {
      total.innerHTML = `${tx.value.length}/200字`
    })

    // 按下Enter發布評論  
    tx.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') {
        // 輸入不為空才顯示和輸出
        if (tx.value.trim()) {
          item.style.display = 'block'
          infoText.innerHTML = tx.value
        }
        // 清空textarea 復原統計
        tx.value = ''
        total.innerHTML = '0/200字'
      }
    })
  </script>
</body>


</html>
```



