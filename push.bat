REM 将所有新内容添加到Git
git add .

REM 获取当前时间
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set datetime=%%a
set "year=%datetime:~0,4%"
set "month=%datetime:~4,2%"
set "day=%datetime:~6,2%"
set "hour=%datetime:~8,2%"
set "minute=%datetime:~10,2%"
set "second=%datetime:~12,2%"

REM 提交并添加当前时间作为评论
set comment=Auto commit at %year%-%month%-%day% %hour%:%minute%:%second%
git commit -m "%comment%"

REM 推送到远程仓库
git push

endlocal
