# 快速部署指南 🚀

## 推荐方案：Railway (最简单)

Railway 提供免费额度，部署超级简单，5分钟搞定！

### 步骤：

1. **注册 Railway**
   - 访问 [railway.app](https://railway.app)
   - 用 GitHub 账号登录

2. **创建项目**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择你的 lovebird-api 仓库

3. **自动部署**
   - Railway 会自动检测 Python 项目
   - 读取 `requirements.txt` 安装依赖
   - 使用 `Procfile` 启动应用
   - 几分钟后就部署好了！

4. **获取 URL**
   - 点击项目 → Settings → Generate Domain
   - 你会得到类似：`https://your-app.up.railway.app`
   - 测试：`https://your-app.up.railway.app/bird`

### 免费额度
- 每月 $5 USD 免费额度
- 足够个人项目使用
- 超出额度才收费

---

## 方案2：Vercel (也很简单)

1. **安装 Vercel CLI**
```bash
npm install -g vercel
```

2. **在项目目录运行**
```bash
vercel login
vercel --prod
```

3. **完成！**
   - Vercel 会给你一个 URL
   - 支持自定义域名

---

## 方案3：自己的服务器 (VPS)

如果你有自己的服务器（腾讯云、阿里云等）：

### 1. 安装依赖
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip nginx

# 安装 Python 包
pip3 install -r requirements.txt
```

### 2. 运行应用
```bash
# 测试运行
python3 app.py

# 生产环境（用 gunicorn）
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### 3. 配置 Nginx（可选，用于域名访问）

创建 `/etc/nginx/sites-available/lovebird-api`：
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

启用配置：
```bash
sudo ln -s /etc/nginx/sites-available/lovebird-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 4. 设置开机自启（systemd）

创建 `/etc/systemd/system/lovebird-api.service`：
```ini
[Unit]
Description=Lovebird API
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/lovebird-api
ExecStart=/usr/local/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

启动服务：
```bash
sudo systemctl enable lovebird-api
sudo systemctl start lovebird-api
sudo systemctl status lovebird-api
```

---

## 替换成真实的牡丹鹦鹉图片 🦜

**重要！** 目前 `images/` 文件夹里是占位图片，需要替换成真实的牡丹鹦鹉照片。

### 下载图片：

1. **Pixabay** (免费，无需署名)
   - https://pixabay.com/images/search/lovebird/
   - 搜索 "lovebird" 或 "牡丹鹦鹉"
   - 下载高清图片

2. **Unsplash** (免费，高质量)
   - https://unsplash.com/s/photos/lovebird
   - 搜索 "lovebird parrot"

3. **Pexels** (免费)
   - https://www.pexels.com/search/lovebird/

### 替换步骤：

1. 下载 30+ 张牡丹鹦鹉图片
2. 重命名为：`lovebird_01.jpg`, `lovebird_02.jpg`, ...
3. 放到 `images/` 文件夹，替换现有文件
4. 支持 `.jpg` 和 `.png` 格式

---

## 测试 API

部署完成后，测试一下：

```bash
# 获取随机图片
curl https://your-domain.com/bird --output test.jpg

# 获取 JSON 信息
curl https://your-domain.com/bird?json=true

# 检查健康状态
curl https://your-domain.com/health

# 查看图片数量
curl https://your-domain.com/count
```

在浏览器直接访问：
```
https://your-domain.com/bird
```

每次刷新都会得到不同的牡丹鹦鹉照片！

---

## 问题排查

### 部署失败？
- 检查 `requirements.txt` 是否正确
- 确保 `Procfile` 存在
- 查看部署日志

### 图片不显示？
- 确保 `images/` 文件夹有图片
- 检查图片格式（支持 .jpg 和 .png）
- 查看 `/health` 端点显示的图片数量

### 需要帮助？
- Railway 文档: https://docs.railway.app/
- Vercel 文档: https://vercel.com/docs

---

祝部署顺利！ 🚀
