# Dowmloader Middleware

## 作用
* 在scheduer调度处队列的Request发送到Downloader下载之前，也就是Request执行下载之前进行修改

* 在下载后生成的Response发送给Spider之前，也就是在Response被Spider解析之前对其进行修改

* 修改User-Agent,处理重定向、设置代理、失败重试、设置cookies等功能

## 笔记
* scrapy内置了很多DOWNLOADER_MIDDLEWARES_BASE变量，查看命令  
``scrapy settings --get=DOWNLOADER_MIDDLEWARES_BASE``
 
* 三个核心方法
  + process_request(request, spider)
  
  + process_response(request, response, spider)
  
  + process_exception(request, exception, spider)

* middlewares.py 里面添加RandomUserAgentMiddleware类，定义process_request方法，需要再调用Downloader Middleware，
在settings.py里面将DOWNLOADER MIDDLEWARES取消注释，设置为'xxx.RandomUserAgentMiddleware': 543