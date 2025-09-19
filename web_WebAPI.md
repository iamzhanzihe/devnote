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







