 <img src="kindle.png" width=48px/> My kindle tools
 =======================

- [1. epub转mobi (epub2mobi.exe)](#1-epub转mobi-epub2mobiexe)
    - [1.1. 用法](#11-用法)
    - [1.2. mobi瘦身](#12-mobi瘦身)
- [2. 推送文件到Kindle (SendToKindle.exe)](#2-推送文件到kindle-sendtokindleexe)
    - [2.1. 用法](#21-用法)
    - [2.2. 为什么要一本书发一封邮件?](#22-为什么要一本书发一封邮件)
<br/>
<br/>

# 1. epub转mobi (epub2mobi.exe)
作用：
> 将传入的epub转换为kindle支持的mobi格式。并将mobi瘦身。
转换调用的是`lib`目录下amazon官方的mobi生成工具`kindlegen.exe`。

## 1.1. 用法
1. 下载`ebpu2mobi.exe`
2. 将你想要转换的`epub`文件拖拽到程序图标上
3. `mobi`文件自动生成在`epub`文件同一目录

## 1.2. mobi瘦身
>本工具转换调用的是`lib`目录下amazon官方的mobi生成工具`kindlegen.exe`。
><br/>但因为用`kindlegen.exe`工具生成的`mobi`文件体积很大，需要瘦身。所以工具生成`mobi`后会自动调用`lib`目录下的`kindlestrip.exe`对`mobi`进行瘦身。
  
<br/>
<br/>
    
# 2. 推送文件到Kindle (SendToKindle.exe)
作用：
>将文件以一个文件一封信件的形式发送到你的Kindle推送邮箱中。
## 2.1. 用法
1. 下载`sendToKindle.exe`
2. 运行`sendToKindle.exe`，第一次运行会要求你提供必要的信息，如：用来发邮箱的账号，密码等（建议单独申请一个邮箱用来推送书籍）
3.  配置完成后，如果有书籍要发送，就直接选中书籍，然后拖动到`sendToKindle.exe`上
4. 如果要变更邮箱设置，直接打开`EmailSetting.txt`编辑就行。
## 2.2. 为什么要一本书发一封邮件?

>  因为Kindle的推送邮箱只支持`50MB`大小附件。然后主流的邮件服务提供商(如：`Gmail`, `Yahoo`, `Hotmail` etc)大多只支持`25MB`附件。
> 
> 这意味着你如果要发送N本`mobi`小说的话（如一本轻小说就动不动`5MB`,  `8MB`大小)，就必须要分成好几封邮件，相当麻烦。所以直接一本书一封邮件发过去最好。
><br/>即便`QQ`，`163`邮箱支持`50MB`附件，但实际上尝试过一封邮件一次推送一堆书的人都知道，邮件会一直提示`投递中`，要很久才能kindle收到。