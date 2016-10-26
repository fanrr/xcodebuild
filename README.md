# xcodebuild
Xcode打包脚本


# 怎么用它？
- clone 工程
- 打开终端cd到xcodebuild工程下执行
```shell
$python build.py
```
- 设置参数

```shell
您需要设置参数,您的参数如下:
=========================
mainPath          :None
targetName        :None
xcworkspaceName   :None
schemeName        :None
certificateName   :None
exportPath        :None
=========================
```
[具体参数对照](https://github.com/fanrr/xcodebuild/blob/master/help.jpeg)

###mainPath
  ```shell
  input mainPath:/Users/Raymond/Documents/Demo
  ```
###targetName
  ```shell
  input targetName:Demo
  ```
###xcworkspaceName
  ```shell
  input xcworkspaceName:Demo
  ```
###schemeName
  ```shell
  input schemeName:Demo
  ```
###certificateName
  ```shell
  input certificateName:iPhone Developer: xx xx (xxxxxxx)
  ```
###exportPath
  ```shell
  input exportPath:/Users/Raymond/Desk/IPA/
  ```
设置完参数，就等待IPA包的出现吧，傻瓜式的打包

- 修改参数
```shell
$python build.py -c
#or
$python build.py -config
#不输入默认不做修改
```
