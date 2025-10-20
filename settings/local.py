"""
本地配置模块，用于从本地配置文件中加载配置
"""

import os
import json

# 配置文件路径
CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

# 默认配置
IS_CAPCUT_ENV = True

# 默认域名配置
DRAFT_DOMAIN = "https://www.install-ai-guider.top"

# 默认预览路由
PREVIEW_ROUTER = "/draft/downloader"

# 是否上传草稿文件
IS_UPLOAD_DRAFT = False

# 端口号
PORT = 9000

OSS_CONFIG = []
MP4_OSS_CONFIG=[]

# 新增：鉴权与限流默认配置
API_KEYS = []
ROUTE_POLICIES = {"default": {"protected": False}}
RATE_LIMIT = {"enabled": False, "requests": 100, "per_seconds": 60}

# 尝试加载本地配置文件
if os.path.exists(CONFIG_FILE_PATH):
    try:
        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            local_config = json.load(f)
            
            # 更新是否是国际版
            if "is_capcut_env" in local_config:
                IS_CAPCUT_ENV = local_config["is_capcut_env"]
            
            # 更新域名配置
            if "draft_domain" in local_config:
                DRAFT_DOMAIN = local_config["draft_domain"]

            # 更新端口号配置
            if "port" in local_config:
                PORT = local_config["port"]

            # 更新预览路由
            if "preview_router" in local_config:
                PREVIEW_ROUTER = local_config["preview_router"]
            
            # 更新是否上传草稿文件
            if "is_upload_draft" in local_config:
                IS_UPLOAD_DRAFT = local_config["is_upload_draft"]
                
            # 更新OSS配置
            if "oss_config" in local_config:
                OSS_CONFIG = local_config["oss_config"]
            
            # 更新MP4 OSS配置
            if "mp4_oss_config" in local_config:
                MP4_OSS_CONFIG = local_config["mp4_oss_config"]

            # 新增：更新 API Keys 白名单
            if "api_keys" in local_config:
                API_KEYS = local_config["api_keys"] or []
            
            # 新增：更新路由权限策略
            if "route_policies" in local_config:
                ROUTE_POLICIES = local_config["route_policies"] or {"default": {"protected": True}}
            
            # 新增：更新限流配置
            if "rate_limit" in local_config:
                RATE_LIMIT = local_config["rate_limit"] or {"enabled": False, "requests": 100, "per_seconds": 60}
    except (json.JSONDecodeError, IOError):
        # 配置文件加载失败，使用默认配置
        pass