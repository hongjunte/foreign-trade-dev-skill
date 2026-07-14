@echo off
chcp 65001 >nul
title GCCS Trade Hunter · 外贸情报终端
cd /d "%~dp0"

echo ========================================
echo   GCCS Trade Hunter · 外贸情报终端
echo ========================================
echo.

:: 检查端口 8765 是否被占用
netstat -ano | findstr ":8765 " | findstr "LISTENING" >nul 2>&1
if %errorlevel% equ 0 (
    echo [!] 端口 8765 已被占用，可能已有实例在运行。
    echo     直接打开浏览器即可：http://localhost:8765/index.html
    echo.
    start "" "http://localhost:8765/index.html"
    timeout /t 3 /nobreak >nul
    exit /b 0
)

echo [1/2] 启动本地服务器 (端口 8765)...
start /b python -m http.server 8765

echo [2/2] 打开浏览器...
timeout /t 1 /nobreak >nul

:: 始终用 localhost（不是 127.0.0.1），保证 localStorage origin 一致
start "" "http://localhost:8765/index.html"

echo.
echo ✓ 已启动！浏览器应已自动打开。
echo.
echo ◎ 保持此窗口打开以维持服务。
echo ◎ 关闭服务：直接关闭此窗口或按 Ctrl+C。
echo ◎ 重要：始终用 http://localhost:8765 访问，不要用 127.0.0.1
echo    （否则历史记录和配置会丢失）
echo.
pause >nul
