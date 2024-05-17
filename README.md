# Django練習
> * 創作日：2024/05/16
> * 最後日：2024/05/16
> * 使用系統：MacOS
> * 創作者：小黑
---
* ## 參考網站：
> #### [零度解說ＹＴ參考網站](https://www.youtube.com/watch?v=3LLUyaHP-3I&t=433s)
> #### [LangChain參考網站](https://python.langchain.com/v0.1/docs/get_started/introduction/)
> #### [WTF Academy LangChain參考網站](https://www.youtube.com/watch?v=UQuKSGPpZW0&list=PL2fGiugrNooiIOPokp4tCZ71kVOdjBcsu&index=1)
> #### [LangChain是什麼？AI開發者必須了解的LLM開源框架參考網站](https://tw.alphacamp.co/blog/langchain-intro)
> #### [大神參考網站](https://chatgpt.com/?oai-dm=1)
---


---
1. ### 確認有安裝python
`pythpn3 --version`

![python版本](https://hackmd.io/_uploads/r1ZWBXXmR.png)

---

2. ### 安裝django
`pip3 install django`

![django安裝](https://hackmd.io/_uploads/SygBU77XA.png)

---

3. ### 創立一個django的檔案
`django-admin startproject myproject`

![創立django資料夾](https://hackmd.io/_uploads/ryegPmQQA.png)

---

4. ### 創建一個healthcheck
`pytho3 mange.py startapp healthcheck`

![創建一個healthcheck](https://hackmd.io/_uploads/HyMou7mmC.png)

---

5. ### cd到myproject裡面，增加幾段程式碼

![新增myproject代碼](https://hackmd.io/_uploads/r19EnQ7m0.png)

![urls.py程式碼](https://hackmd.io/_uploads/rkc2L4mQ0.png)

---

6. ### cd ..回到myproject後，再cd到healthcheck裡面，增加view.py程式碼

![views.py程式碼](https://hackmd.io/_uploads/BJNHAX7QC.png)

![view.py程式碼](https://hackmd.io/_uploads/HkAY07XX0.png)

---

7. ### 在去增加一個urls.py的檔案，再增加程式碼
![healthcheck裡面的urls程式碼](https://hackmd.io/_uploads/HJj0xNQmR.png)

![healthcheckurl程式碼](https://hackmd.io/_uploads/rkC8Z4mQ0.png)


---

8. ### 回到myproject執行manage.py

![截圖 2024-05-16 下午3.37.39](https://hackmd.io/_uploads/Bk4RPEmmR.png)

![djangorunserver](https://hackmd.io/_uploads/ByxqwEQXR.png)

* 輸入http://127.0.0.1:8000/health/

![輸入localhost8000](https://hackmd.io/_uploads/HJ2cuE7QR.png)

9. 把這段練習上傳上去自己的GitHub(可以順便練習GitHub)
![github練習1（新增一個）](https://hackmd.io/_uploads/H1VGZwQXR.png)
![github練習2（內容）](https://hackmd.io/_uploads/H12zZDX7C.png)


# 切換到要上傳的目錄位置
`cd /Users/black/myproject`
* 在去初始化倉庫
`git init`

![初始化git倉庫](https://hackmd.io/_uploads/BJOAUBQQA.png)

* 可以使用指令查詢暫存區
`git status`

![git查詢暫存區](https://hackmd.io/_uploads/ry1PwBX7C.png)

* 上傳當下目錄所有東西到暫存區，上傳完成後再查詢一次
`git add .`

![git上傳所有到暫存區](https://hackmd.io/_uploads/HJoE_HX7A.png)

* 上傳
`git commit -m "Initial commit"`
![第一次提交git](https://hackmd.io/_uploads/B1wmOI770.png)


* 方便一點把電腦跟github連接再一起，就不用一直輸入帳號密碼
1. ssh-keygen -t ed25519 -C "your_email@example.com"(輸入自己的GitHub的mail)
2. cat ~/.ssh/id_ed25519.pub(把出現的密鑰複製下來在進行以下步驟)

![github密鑰連接方式1](https://hackmd.io/_uploads/r1-5C87XC.png)

![github密鑰連接方式2](https://hackmd.io/_uploads/r1HqR87mR.png)

![新增ＳＳＨ密要](https://hackmd.io/_uploads/ry99AUQmA.png)

![確認密鑰](https://hackmd.io/_uploads/r1A9AL7QA.png)

* 複製倉庫的URL

![複製倉庫的URL](https://hackmd.io/_uploads/ByC8FS77A.png)

* 執行一次遠端關聯倉庫
```
git remote add origin git@github.com:littleblackmann/Django-health-check.git
```

* 上傳
`git push -u origin main`

![上傳到github](https://hackmd.io/_uploads/BybzoIX7A.png)




* 如果之後要更新上傳失敗的話先進行pull在push
![上傳github失敗的話](https://hackmd.io/_uploads/rJqc05NQ0.png)

* 輸入這個先讓倉庫跟自己本地進度一樣
`git pull origin main`

![gitpull更新](https://hackmd.io/_uploads/HkCP1oN7R.png)

* 在去commit

![截圖 2024-05-17 下午5.19.16](https://hackmd.io/_uploads/Bk94bsN70.png)


* 在進行push
`git push -u origin main`

![更新後上傳到github](https://hackmd.io/_uploads/Bk_FZoNXA.png)

![成果圖](https://hackmd.io/_uploads/H1PbMiEmR.png)



















